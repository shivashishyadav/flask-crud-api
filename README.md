# Flask CRUD API

A simple REST API built with **Flask** to practice basic CRUD (Create, Read, Update, Delete) operations.

---

## 📂 Project Structure
```
flask-crud-api/
   ├── app.py # Main Flask app
   ├── /static/
   |        |_style.css # Styles for frontend
   |
   ├── /templates/
   |        |_index.html # Homepage (basic explanation of CRUD)
   |
   ├── .gitignore
   ├── README.md
   └── env/ (ignored) # Virtual environment
```


---

## Features
- **GET** → Fetch all users or a single user by ID  
- **POST** → Add a new user  
- **PUT** → Update an existing user  
- **DELETE** → Remove a user  

---

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/shivashishyadav/flask-crud-api.git
   cd flask-crud-api

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows

3. Install dependencies
pip install flask

4. Run the flask app
python app.py