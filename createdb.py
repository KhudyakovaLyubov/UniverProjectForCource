from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Staff, Faculty, FGroup, Student, Exam, Exam_record, HR_record
import sqlite3

def create_db():
    engine = create_engine('sqlite:///C:/Users/MoonLover/Desktop/myuniverdb/univer.db', echo=True)
    Base.metadata.create_all(engine)

def insert_data():
    with open('C:/Users/MoonLover/Desktop/myuniverdb/insert_data.sql', 'r') as f:
        schema = f.read()

    conn =  sqlite3.connect('C:/Users/MoonLover/Desktop/myuniverdb/univer.db')
    cursor = conn.cursor()
    cursor.executescript(schema)
    print('Данные добавлены')
    conn.commit()
    conn.close()

create_db()
insert_data()