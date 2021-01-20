from sqlalchemy.orm import sessionmaker, Session
from models import Base, Staff, Faculty, FGroup, Student, Exam, Exam_record, HR_record
from sqlalchemy import create_engine

# Открытие базы данных 
engine = create_engine('sqlite:///C:/Users/MoonLover/Desktop/myuniverdb/univer.db')
Session = sessionmaker(bind=engine)
session = Session() 

# Тестовые запросы
len1 = len(session.query(Student).join(Exam_record).all())
len2 = len(session.query(Exam_record).join(Exam).filter(Exam.discipline.like('Math')).all())
len3 = len(session.query(Exam_record).join(Exam).join(Staff).filter(Staff.last_name.like('Gavrilova')).all())

# Результат для проверки
print(len1*len2*len3)