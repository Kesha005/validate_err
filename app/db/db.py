from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

from app.models.models import Base


URL = "mysql+mysqlconnector://root@localhost:3306/laravel"


ENGINE = create_engine(URL)

Session = sessionmaker(bind=ENGINE)

def recreate_base():
    Base.metadata.create_all(ENGINE)
    print(f'Database is migrated')


def clear_base():
    Base.metadata.clear_all(ENGINE)