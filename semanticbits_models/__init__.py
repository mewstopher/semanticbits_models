from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, Text, DateTime, Float
from sqlalchemy.sql import func

Base = declarative_base()

class Health(Base):
    __tablename__ = 'health'
    id = Column('id', Integer, primary_key=True)
    state = Column('state', Text)
    county = Column('county', Text)
    state_code = Column('state_code', Integer)
    county_code = Column('county_code', Integer)
    year_span = Column('year_span', Text)
    measure_name = Column('measure_name', Text)
    measure_id = Column('measure_id', Integer)
    numerator = Column('numerator', Float)
    denominator = Column('denominator', Float)
    raw_value = Column('raw_value', Float)
    confidence_interval_lower_bound = Column('confidence_interval_lower_bound', Float)
    confidence_interval_upper_bound = Column('confidence_interval_upper_bound', Float)
    date_release_year = Column('date_release_year', Integer)
    fipscode = Column('fipscode', Integer)
    dt_updated = Column('dt_updated', DateTime, server_default=func.now())
