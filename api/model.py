from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, ForeignKey, CHAR, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root@localhost/Test")

Base = declarative_base(engine)

class Books(Base):
    __tablename__ = "Books"
    __table_args__ = {"autoload": True}