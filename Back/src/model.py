from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:1234@localhost:5433/cellcom"

db = create_engine(db_string)
base = declarative_base()


class User(base):
    __tablename__ = 'user'
    email = Column(String, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    identificationCard = Column(String)
    phone = Column(String)
    address = Column(String)
    password = Column(String)
    rol = Column(String)

class Lines(base):
    __tablename__ = 'lines'
    numberline=Column(String, primary_key=True)
    customerIdentification=Column(String)
    state=Column(String)

class Bill(base):
    __tablename__ = 'bills'
    value= Column(Integer,)
    collectionDay=Column(Date)
    customerIdentification=Column(String)
    numberLine=Column(String, primary_key=True)

class Customer(base):
    __tablename__= 'customer'
    namne=Column(String)
    lastname=Column(String)
    customerIdentification=Column(String, primary_key=True)
    line=Column(String)
    dateBorn=Column(Date)

class equipment(base):
    __tablename__= 'equipment'
    lineNumber=Column(String)
    serial=Column(String)
    imei=Column(String, primary_key=True)
    trademark=Column(String)
    state= Column(String)
    customerIdentification = Column(String)

    

Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)
