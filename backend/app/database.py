from sqlmodel import Session, create_engine, SQLModel
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    from .models.job import Job

    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
