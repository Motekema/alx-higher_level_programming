#!/usr/bin/python3
"""Script that lists all State objects and corresponding City objects contained in the database hbtn_0e_101_usa"""

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

    # Query to retrieve all State and City objects
    result = session.query(State, City).filter(State.id == City.state_id).order_by(State.id, City.id).all()

    # Iterate through the result and display information
    for state, city in result:
        if city is None:
            print("{}: {}".format(state.id, state.name))
        else:
            print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()
