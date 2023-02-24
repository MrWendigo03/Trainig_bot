from datetime import datetime, date

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, and_, or_, not_, func, select, desc
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost:5432/transactions")
Base = declarative_base(bind=engine)


class Students(Base):

    __tablename__ = "Обучаемый"

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(50), unique=True, nullable=False)
    object_studied = Column(String(50), nullable=False)

    def __str__(self):
        return f"Author: {self.id}"

    def __repr__(self):
        return f"Author: {self.id}"