from aiogram.types import message
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, and_, or_, not_, func, select, desc
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("postgresql://postgres:postgres@localhost:5432/transactions")
Base = declarative_base(bind=engine)


class Students(Base):

    __tablename__ = "Обучаемый"

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)
    subject = Column(ForeignKey("o_id"), nullable=False)

    def __str__(self):
        return f"Students: {self.id}"

    def __repr__(self):
        return f"Students: {self.id}"

class Object(Base):

    __tablename__ = "Предметы"

    o_id = Column(Integer(), primary_key=True)
    name = Column(String(150), nullable=False)

    def __str__(self):
        return f"Object: {self.id}"

    def __repr__(self):
        return f"Object: {self.id}"
