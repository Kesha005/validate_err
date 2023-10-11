from sqlalchemy import Column, String, Integer, Date

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    email = Column(String(120), unique=True)
    data_birth = (Date)
    
    
class Password(Base):
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Culumn(String(120))
    username = Culumn(String(120))
    password = Columng(String(150))
    email  = Column(String(120))
    
    
