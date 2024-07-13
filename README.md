# CT-Introduction-to-Object-relational-Mappers-ORM-
# Fitness Center Management

## Setup

1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your database connection in `app/config.py`.

4. Run the application:
    ```bash
    python run.py
    ```

## API Endpoints

- **Members**
  - `POST /members`: Add a new member
  - `GET /members/<id>`: Retrieve a member by ID
  - `PUT /members/<id>`: Update a member by ID
  - `DELETE /members/<id>`: Delete a member by ID

- **Workout Sessions**
  - `POST /workouts`: Add a new workout session
  - `PUT /workouts/<id>`: Update a workout session by ID
  - `GET /workouts/<id>`: Retrieve a workout session by ID
  - `DELETE /workouts/<id>`: Delete a workout session by ID
  - `GET /members/<member_id>/workouts`: Retrieve all workout sessions for a specific member
