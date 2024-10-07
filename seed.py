from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models import Base, Student, Group, Teacher, Subject, Grade

fake = Faker()
engine = create_engine('postgresql://postgres:11111@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

try:
    groups = [Group(name=fake.word()) for _ in range(3)]
    session.add_all(groups)
    
    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)

    subjects = [Subject(name=fake.word(), teacher_id=random.choice(teachers).id) for _ in range(8)]
    session.add_all(subjects)

    students = []
    grades = []
    
    for _ in range(30):
        student = Student(fullname=fake.name(), group_id=random.choice(groups).id)
        students.append(student)
        
        for subject in subjects:
            for _ in range(random.randint(1, 20)):
                grade = Grade(
                    grade=random.uniform(1, 10),
                    student_id=student.id,
                    subject_id=subject.id,
                    date=fake.date_this_decade()
                )
                grades.append(grade)
    
    session.add_all(students)
    session.add_all(grades)
    session.commit()

except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()