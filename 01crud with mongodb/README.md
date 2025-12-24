# 🚀 FastAPI & MongoDB CRUD Application

A modern, highly efficient asynchronous CRUD API built with **FastAPI** and **MongoDB Atlas**. This project demonstrates best practices for integrating a NoSQL database with a Python backend, featuring robust data serialization and clean architecture.

## 🛠️ Technology Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High performance, async support)
- **Database:** [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (Cloud-hosted NoSQL)
- **Client:** [PyMongo](https://pymongo.readthedocs.io/) (Official Python driver)
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/) (Strict type checking)
- **Dependency Management:** [uv](https://github.com/astral-sh/uv) (Fast Python package installer)

## ✨ Features

- **✅ Create:** Add new tasks to the MongoDB collection.
- **✅ Read:** Retrieve all tasks with proper ID serialization.
- **✅ Update:** Modify existing tasks using their unique `ObjectId`.
- **✅ Delete:** Remove tasks from the database securely.
- **🔒 Secure Connections:** Integrated with `certifi` for trusted SSL handshakes on Windows.

## 📁 Project Structure

```text
00fastapi/
├── config/
│   └── database.py   # Connection logic & MongoDB client
├── models/
│   └── todo.py       # Pydantic data schemas
├── routes/
│   └── routes.py     # API endpoint definitions
├── schema/
│   └── schema.py     # Data serialization (BSON to JSON)
├── main.py           # Application entry point
├── pyproject.toml    # Project dependencies
└── .env              # Environment secrets
```

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have [uv](https://github.com/astral-sh/uv) or `pip` installed.

### 2. Configure MongoDB
1. Create a cluster on [MongoDB Atlas](https://www.mongodb.com/).
2. Add your IP address to the **Network Access** list.
3. Obtain your connection string.

### 3. Setup Environment
Update the `url` in `config/database.py` or create a `.env` file:
```ini
MONGODB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/
```

### 4. Install Dependencies
```powershell
uv sync
```

### 5. Run the Application
```powershell
uv run uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/` | Welcome message |
| **GET** | `/get_todos` | Fetch all todo items |
| **POST** | `/` | Create a new todo item |
| **PUT** | `/{id}` | Update an existing todo by ID |
| **DELETE** | `/{id}` | Delete a todo item by ID |

## 🛠️ Development & Debugging

If you encounter **SSL handshake errors** on Windows, this project specifically includes `certifi` and `tlsCAFile` configuration in `config/database.py` to handle CA certificate verification issues common in Python environments.

---

Built with ❤️ using FastAPI and MongoDB.
