from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:549024@localhost:3306/annular?charset=utf8',
                       encoding='utf-8',
                       convert_unicode=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)