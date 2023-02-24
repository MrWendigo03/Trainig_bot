from aiogram.types import message
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, and_, or_, not_, func, select, desc
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.functions import user


engine = create_engine("postgresql://postgres:postgres@localhost:5432/transactions")
Base = declarative_base(bind=engine)


class Students(Base):

    __tablename__ = f"Обучаемый {message.from_user.username}"

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)

    def __str__(self):
        return f"Author: {self.id}"

    def __repr__(self):
        return f"Author: {self.id}"
