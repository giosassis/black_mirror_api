# Black Mirror API

API to manage and display information about the episodes of *Black Mirror*. It includes a ranking of episodes based on their ratings and allows filtering episodes by season.

## Technologies

- **FastAPI**: A framework to build fast and modern APIs with Python.
- **SQLite**: Lightweight database to store episode data.
- **Jinja2**: Template engine for rendering dynamic HTML templates.
- **JavaScript**: For interactivity on the frontend (season filtering).
- **CSS**: Styling for the table and page.

## Features

- **Episode Ranking**: Displays episodes ranked by their rating.
- **API Endpoints**:
    - **`GET /episodes`**: Returns all episodes of the series.
    - **`GET /ranking`**: Displays episodes in a table format with filtering capabilities.

## Folder Structure

├── app │ 
    ├── controllers.py │ 
    ├── models.py │
    ├── schemas.py │ 
    ├── routers │ 
    ├── database.py │ 
    ├── deletedatabase.py 
    │ └── main.py 
    ├── templates 
    │ └── table_template.html 
    ├── static 
    │ ├── css │ 
        │ └── style.css 
      │ └── js 
        │ └── main.js 
    ├── requirements.txt 
└── README.md
└── .gitignore

## How to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/black-mirror-api.git
   cd black-mirror-api

2. **Create and activate a virtual environment**:
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows

3. **Run the CSV to DB Script**:
    Before running the application, you need to load the episode data into the SQLite database from the CSV file. To do this, run the following script:
    ```bash
    python app/utils/csv_to_db.py

4. **Install the dependencies**:
    pip install -r requirements.txt

5. **Run the local server**:
    uvicorn app.main:app --reload
    The server will be available at http://127.0.0.1:8000.

## How to Use the API:

- Go to http://127.0.0.1:8000/ranking to see the table with the ranking of episodes.

## Database:
- The SQLite database is created automatically when the application runs for the first time, with episode data imported from a CSV file.