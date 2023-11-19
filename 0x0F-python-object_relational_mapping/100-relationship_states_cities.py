#!/usr/bin/python3
"""
a script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import State, Base
from relationship_city  import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database of the states
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cali_state = State(name='California')
    sanfr_city = City(name='San Francisco')
    cali_state.cities.append(sanfr_city)

    session.add(cali_state)
    session.commit()
    session.close()
