# Base SQLAlchemy declarative model shared by all modules.
# Every module's ORM model should inherit from Base.

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
