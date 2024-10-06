import argparse
from models import Student, Group, Teacher, Subject
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:mysecurepassword@localhost/mydatabase')
Session = sessionmaker(bind=engine)
session = Session()

def create_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for database operations")
    parser.add_argument('--action', '-a', required=True, help="CRUD action")
    parser.add_argument('--model', '-m', required=True, help="Model to operate on")
    parser.add_argument('--name', '-n', help="Name for creation")
    parser.add_argument('--id', type=int, help="ID for update/remove")

    args = parser.parse_args()

    if args.action == 'create' and args.model == 'Teacher':
        create_teacher(args.name)
