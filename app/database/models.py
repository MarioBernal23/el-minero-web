import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Page(Base):
    __tablename__ = "pages"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(sqlalchemy.String(500))
    title: Mapped[str] = mapped_column(sqlalchemy.String(255))
    content: Mapped[str] = mapped_column(sqlalchemy.Text)