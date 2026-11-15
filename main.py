from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import DateTime, String, Text, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# ---------- Database ----------
engine = create_async_engine("sqlite+aiosqlite:///./notes.db")
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


async def get_db():
    async with SessionLocal() as session:
        yield session


# ---------- Schemas ----------
class NoteIn(BaseModel):
    title: str
    content: str = ""


class NoteOut(NoteIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime


# ---------- App ----------
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Notes API", lifespan=lifespan)


@app.get("/")
async def root():
    return {"status": "ok", "docs": "/docs"}


@app.post("/notes", response_model=NoteOut, status_code=201)
async def create_note(data: NoteIn, db: AsyncSession = Depends(get_db)):
    note = Note(**data.model_dump())
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note


@app.get("/notes", response_model=list[NoteOut])
async def list_notes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Note).order_by(Note.id.desc()))
    return result.scalars().all()


@app.get("/notes/{note_id}", response_model=NoteOut)
async def get_note(note_id: int, db: AsyncSession = Depends(get_db)):
    note = await db.get(Note, note_id)
    if not note:
        raise HTTPException(404, "Note not found")
    return note


@app.put("/notes/{note_id}", response_model=NoteOut)
async def update_note(note_id: int, data: NoteIn, db: AsyncSession = Depends(get_db)):
    note = await db.get(Note, note_id)
    if not note:
        raise HTTPException(404, "Note not found")
    note.title, note.content = data.title, data.content
    await db.commit()
    await db.refresh(note)
    return note


@app.delete("/notes/{note_id}", status_code=204)
async def delete_note(note_id: int, db: AsyncSession = Depends(get_db)):
    note = await db.get(Note, note_id)
    if not note:
        raise HTTPException(404, "Note not found")
    await db.delete(note)
    await db.commit()