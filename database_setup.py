import os
import csv
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database file path
database_file = 'lifestyle_sleep_data.sqlite'

# Create the SQLAlchemy engine
engine = create_engine(f'sqlite:///{database_file}', echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define the model for the table


class LifestyleSleepData(Base):
    __tablename__ = 'lifestyle_sleep_data'
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(String)
    age = Column(Integer)
    occupation = Column(String)
    sleep_duration = Column(Float)
    quality_of_sleep = Column(Integer)
    physical_activity_level = Column(Integer)
    stress_level = Column(Integer)
    BMI_category = Column(String)
    blood_pressure = Column(String)
    heart_rate = Column(Integer)
    daily_steps = Column(Integer)
    sleep_disorder = Column(String)


# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

with open(os.path.join('data', 'Sleep_health_mk1.csv'), encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    # skip header row
    next(csv_reader)
    for csv_row in csv_reader:
        person_id, gender, age, occupation, sleep_duration, quality_of_sleep, physical_activity_level, stress_level, BMI_category, blood_pressure, heart_rate, daily_steps, sleep_disorder = csv_row
        db_row = LifestyleSleepData(person_id=person_id, gender=gender, age=age, occupation=occupation, sleep_duration=sleep_duration, quality_of_sleep=quality_of_sleep,
                                    physical_activity_level=physical_activity_level, stress_level=stress_level, BMI_category=BMI_category, blood_pressure=blood_pressure,
                                    heart_rate=heart_rate, daily_steps=daily_steps, sleep_disorder=sleep_disorder)
        session.add(db_row)

session.commit()

# test query on database
test = session.query(LifestyleSleepData).filter(
    LifestyleSleepData.gender == 'Male').all()

for result in test:
    print(result.age, result.sleep_duration)

session.close()
