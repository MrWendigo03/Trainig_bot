from aiogram.types import message
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from bot import text1


engine = create_engine("postgresql://postgres:postgres@localhost:5432/transactions")
Base = declarative_base(bind=engine)


class Students(Base):

    __tablename__ = "Ученик"

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)

    def __str__(self):
        return f"Students: {self.id}"

    def __repr__(self):
        return f"Students: {self.id}"

class Object(Base):

    __tablename__ = "Предметы"

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return f"Object: {self.id}"

    def __repr__(self):
        return f"Object: {self.id}"

class Train(Base):

    __tablename__ == "Обучение"
