from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbPath = 'datafile.db'
engine = create_engine('sqlite:///%s' % dbPath)  # 創建數據庫引擎 (sqlite可以改成其他種)
metadata = MetaData(engine)

# Create Database
people = Table('people', metadata, Column('id', Integer, primary_key=True), Column(
    'name', String), Column('count', Integer))

Session = sessionmaker(bind=engine)  # 和引擎相連
session = Session()
metadata.create_all(engine)


Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count = Column(Integer)


# Insert data
new1 = People(name='Kevin', count=24)
new2 = People(name='Wang', count=48)
new3 = People(name='Lu', count=63)
session.add(new1)
session.add(new2)
session.add(new3)
session.commit()


# Update data
ray = session.query(People).filter_by(name='Ray').first()
ray.count = 19
session.commit()

# Delete data
melo = session.query(People).filter_by(name='Melo').first()
session.delete(melo)
session.commit()

# Select data
for r in session.query(People).all():
    print(r.id, r.name, r.count)
