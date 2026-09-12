from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.models import Page

def create_page(db: Session, url: str, title: str, content: str):
    page = Page(
        url=url,
        title=title,
        content=content
    )

    db.add(page)
    db.commit()
    return page

def get_page_by_url(db: Session, url: str):
    stmt = select(Page).where(Page.url == url)
    result = db.execute(stmt)
    return result.scalar_one_or_none()