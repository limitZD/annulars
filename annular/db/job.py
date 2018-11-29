'''
import sys
sys.path.append('/home/shiyanlou/Annular/annular/db/base')
import base
'''
from annular.db.base import Base
from sqlalchemy import Column, String, Integer

class JobModel(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    city = Column(String(16))
    salary_lower = Column(Integer)
    salary_upper = Column(Integer)

    experience_lower = Column(Integer)
    experience_upper = Column(Integer)
    education = Column(String(16))
    tags = Column(String(156))
    company = Column(String(32))

'''
if __name__ == '__main__':
     Base.metadata.create_all(engine)
'''