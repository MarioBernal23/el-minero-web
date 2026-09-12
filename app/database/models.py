import sqlalchemy
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Page(Base):
    __tablename__ = "pages"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(sqlalchemy.String(500), unique=True, nullable=False)
    job_id: Mapped[str | None] = mapped_column(sqlalchemy.String(100), nullable=True)
    job_title: Mapped[str] = mapped_column(sqlalchemy.String(255), nullable=False)
    company: Mapped[str | None] = mapped_column(sqlalchemy.String(255), nullable=True)
    company_name: Mapped[str | None] = mapped_column(sqlalchemy.String(255), nullable=True)
    location: Mapped[str | None] = mapped_column(sqlalchemy.String(255), nullable=True)
    candidate_required_location: Mapped[str | None] = mapped_column(sqlalchemy.String(255), nullable=True)
    description: Mapped[str] = mapped_column(sqlalchemy.Text, nullable=False)
    skills: Mapped[str | None] = mapped_column(sqlalchemy.Text, nullable=True)
    tags: Mapped[str | None] = mapped_column(sqlalchemy.Text, nullable=True)
    category: Mapped[str | None] = mapped_column(sqlalchemy.String(100), nullable=True)
    salary: Mapped[str | None] = mapped_column(sqlalchemy.String(100), nullable=True)
    job_type: Mapped[str | None] = mapped_column(sqlalchemy.String(100), nullable=True)
    source: Mapped[str | None] = mapped_column(sqlalchemy.String(100), nullable=True)
    published_at: Mapped[str | None] = mapped_column(sqlalchemy.String(50), nullable=True)
    publication_date: Mapped[str | None] = mapped_column(sqlalchemy.String(50), nullable=True)
    raw_data: Mapped[str | None] = mapped_column(sqlalchemy.Text, nullable=True)
    extracted_at: Mapped[datetime] = mapped_column(
        sqlalchemy.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
