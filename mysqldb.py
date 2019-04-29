from datetime import date
#from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy import *
engine = create_engine('mysql+pymysql://root:kennedy1986@localhost/njoku.db?charset=utf8&use_unicode=0', pool_recycle=3600)


conn=engine.connect()
meta=MetaData()

person=Table('Person2',meta,
             Column('id',Integer, primary_key=True),
             Column('name',String),
             Column('dob',Date))


meta.create_all(engine)
per=person.insert().values(name="Tarkesh",dob=date.today())

print(per)
#print(per.compile().params)
#     #Person("Tarkesh",'2019-01-01')
conn.execute(per)