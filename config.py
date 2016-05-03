import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

 
Base = declarative_base()
 
class Category(Base):
    __tablename__ = 'category'
    # Here we define columns for the table todo.
    id = Column(Integer, primary_key=True)
    category = Column(String(255), unique=True)

    def __repr__ (self):
    	return 'Category: {}'.format(self.category)

class Items(Base):
    __tablename__ = 'items'
    # Here we define columns for the table todo.
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer)
    items = Column(String(255))

    def __repr__ (self):
    	return 'Item: {}'.format(self.items)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)