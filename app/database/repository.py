from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import Page


def create_page(
    db: Session,
    url: str,
    job_title: str,
    description: str,
    company: str | None = None,
    company_name: str | None = None,
    location: str | None = None,
    candidate_required_location: str | None = None,
    skills: str | None = None,
    tags: str | None = None,
    category: str | None = None,
    salary: str | None = None,
    job_type: str | None = None,
    source: str | None = None,
    published_at: str | None = None,
    publication_date: str | None = None,
    raw_data: str | None = None,
    job_id: str | None = None,
    extracted_at: datetime | None = None,
):
    page = Page(
        url=url,
        job_id=job_id,
        job_title=job_title,
        company=company,
        company_name=company_name,
        location=location,
        candidate_required_location=candidate_required_location,
        description=description,
        skills=skills,
        tags=tags,
        category=category,
        salary=salary,
        job_type=job_type,
        source=source,
        published_at=published_at,
        publication_date=publication_date,
        raw_data=raw_data,
        extracted_at=extracted_at or datetime.utcnow(),
    )

    db.add(page)
    db.commit()
    db.refresh(page)
    return page


def get_page_by_url(db: Session, url: str):
    stmt = select(Page).where(Page.url == url)
    result = db.execute(stmt)
    return result.scalar_one_or_none()