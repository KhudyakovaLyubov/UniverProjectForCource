from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Staff(Base):
    __tablename__ = 'Staff'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __repr__(self):
        return "<Staff('%s', '%s')>" % (self.first_name, self.last_name)

class Faculty(Base):
    __tablename__ = 'Faculty'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<Faculty('%s)>" % (self.name)

class FGroup(Base):
    __tablename__ = 'FGroup'
    id = Column(Integer, primary_key=True)
    faculty_id = Column(Integer, ForeignKey('Faculty.id'))

    def __init__(self, faculty_id):
        self.faculty_id = faculty_id
    def __repr__(self):
        return "<FGroup('%s')>" % (self.faculty_id)

class Student(Base):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    group_id = Column(Integer, ForeignKey('FGroup.id'))

    def __init__(self, first_name, last_name, group_id):
        self.first_name = first_name
        self.last_name = last_name
        self.group_id = group_id
    def __repr__(self):
        return "<Student('%s', '%s', '%s')>" % (self.first_name, self.last_name, self.group_id)

class Exam(Base):
    __tablename__ = 'Exam'
    id = Column(Integer, primary_key=True)
    discipline = Column(String)
    staff_id = Column(Integer, ForeignKey('Staff.id'))

    def __init__(self, discipline, staff_id):
        self.discipline = discipline
        self.staff_id = staff_id
    def __repr__(self):
        return "<Exam('%s', '%s')>" % (self.discipline, self.staff_id)

class Exam_record(Base):
    __tablename__ = 'Exam_record'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Student.id'))
    exam_id = Column(Integer, ForeignKey('Exam.id'))
    grade = Column(Integer)
    date = Column(String)

    def __init__(self, student_id, exam_id, grade, date):
        self.student_id = student_id
        self.exam_id = exam_id
        self.grade = grade
        self.date = date
    def __repr__(self):
        return "<Exam_record('%s', '%s', '%s', '%s')>" % (self.student_id, self.exam_id, self.grade, self.date)

class HR_record(Base):
    __tablename__ = 'HR_record'
    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey('Staff.id'))
    faculty_id = Column(Integer, ForeignKey('Faculty.id'))
    position = Column(String)

    def __init__(self,staff_id, faculty_id, position):
        self.staff_id = staff_id
        self.faculty_id = faculty_id
        self.position = position
    def __repr__(self):
        return "<HR_record('%s', '%s', '%s')>" % (self.staff_id, self.faculty_id, self.position)