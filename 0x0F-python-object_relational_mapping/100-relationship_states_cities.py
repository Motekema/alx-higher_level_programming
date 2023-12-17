#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = Session(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State with the City
    new_state = State(name="California", cities=[City(name="San Francisco")])

    # Add the new State to the session
    session.add(new_state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
