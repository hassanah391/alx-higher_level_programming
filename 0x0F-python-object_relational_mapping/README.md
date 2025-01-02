# SQLAlchemy Project

This repository contains various Python scripts and SQL files for working with SQLAlchemy and MySQL databases. The scripts demonstrate different operations such as selecting, filtering, inserting, updating, and deleting records in the database.

## Project Structure

## Files Description

- `0-select_states.py`: Script to select states from the database.
- `0-select_states.sql`: SQL query for selecting states.
- `1-filter_states.py`: Script to filter states based on a condition.
- `10-model_state_my_get.py`: Script to get a specific state model.
- `100-relationship_states_cities.py`: Script to handle relationships between states and cities.
- `100-relationship_states_cities.sql`: SQL query for handling state-city relationships.
- `101-relationship_states_cities_list.py`: Script to list state-city relationships.
- `101-relationship_states_cities_list.sql`: SQL query for listing state-city relationships.
- `102-relationship_cities_states_list.py`: Script to list city-state relationships.
- `11-model_state_insert.py`: Script to insert a new state model.
- `12-model_state_update_id_2.py`: Script to update a state model with ID 2.
- `13-model_state_delete_a.py`: Script to delete a state model.
- `14-model_city_fetch_by_state.py`: Script to fetch cities by state.
- `14-model_city_fetch_by_state.sql`: SQL query for fetching cities by state.
- `2-my_filter_states.py`: Script to filter states based on a custom condition.

## Requirements

- Python 3.8.5
- SQLAlchemy 1.4.x
- MySQL 2.0.x

## Usage

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
    ```
    cd <project-directory>
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the desired script:
    ```
    python <script-name>.py
    ```

## License
Feel free to modify the content as needed!
