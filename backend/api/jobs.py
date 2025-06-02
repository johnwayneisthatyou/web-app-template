# Router & Service

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from ..models.job import Job
from ..database import get_session  # function that yields a DB session

router = APIRouter()


@router.post("/", response_model=Job)
async def create_job(job: Job, session: Session = Depends(get_session)):
    session.add(job)
    session.commit()
    session.refresh(job)
    return job


@router.get("/{job_id}", response_model=Job)
async def read_job(job_id: int, session: Session = Depends(get_session)):
    result = session.exec(select(Job).where(Job.id == job_id)).first()
    if not result:
        raise HTTPException(status_code=404, detail="Job not found")
    return result
