import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

 
Base = declarative_base()
 
class ToDo(Base):
    __tablename__ = 'todos'
    # Here we define columns for the table todo.
    id = Column(Integer, primary_key=True)
    category = Column(String(255), unique=True)
    items = Column(String(250), unique=True)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)