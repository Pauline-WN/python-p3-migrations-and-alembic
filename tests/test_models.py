import sys
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base, Student

@pytest.fixture(scope='module')
def test_db():
    # Set up the database for testing
    engine = create_engine('sqlite:///migrations_test.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_create_student(test_db):
    student = Student(name='Pauline Nguru')
    test_db.add(student)
    test_db.commit()
    assert student.id is not None  