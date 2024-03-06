
# Python MySQL and SQLAlchemy Project Files

This repository contains a series of Python scripts that interact with a MySQL database, some using the MySQLdb module and others using SQLAlchemy ORM. Here's a brief overview of each file:

- **0-select_states.py**: Connects to a MySQL database and lists all states.
- **1-filter_states.py**: Lists all states with names starting with 'N'.
- **2-my_filter_states.py**: Lists states based on a user-provided name.
- **3-my_safe_filter_states.py**: Safely lists states based on a user-provided name to prevent SQL injection.
- **4-cities_by_state.py**: Lists all cities along with their state names.
- **5-filter_cities.py**: Lists cities of a specific state provided by the user.
- **6-model_state.py**: Defines a State model and creates a states table in the database using SQLAlchemy.
- **7-model_state_fetch_all.py**: Lists all State objects from the database.
- **8-model_state_fetch_first.py**: Prints the first State object from the database.
- **9-model_state_filter_a.py**: Lists all State objects containing the letter 'a'.
- **10-model_state_my_get.py**: Prints the State object with a name matching the user input.
- **11-model_state_insert.py**: Adds a new State object "Louisiana" to the database and prints its id.
- **12-model_state_update_id_2.py**: Updates the name of the State with id = 2 to "New Mexico".
- **13-model_state_delete_a.py**: Deletes all State objects with names containing the letter 'a'.
- **model_state.py**: Contains the class definition of a State.
- **model_city.py**: Contains the class definition of a City, related to the State.
- **14-model_city_fetch_by_state.py**: Prints all City objects from the database, sorted by their state and city id.

Each script demonstrates a specific interaction with the database, from basic SQL queries to ORM usage.
