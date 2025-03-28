# 🔐 Sudoku Authentication Service – Secure Access Made Simple

Welcome to the authentication module of the Sudoku Solver project. This FastAPI-powered service provides secure user registration and login using JWT (HS256) encryption, MongoDB Atlas, and robust password hashing with bcrypt. It seamlessly integrates with the other modules of the project to ensure that user data remains safe and secure.

---

## 🔍 What It Does

- **User Registration:**  
  New users can sign up securely. Passwords are hashed with bcrypt before storage in MongoDB.

- **User Login & Authentication:**  
  Validates user credentials and issues a JWT token for accessing protected endpoints across the system.

- **Secure Environment Configuration:**  
  Utilizes environment variables (with dotenv support for local development) to manage sensitive information such as the MongoDB URI and JWT secret key.

---

## ✨ Features

- **Robust Security:**  
  - Passwords are hashed using bcrypt (via Passlib).  
  - JWT tokens ensure stateless, secure authentication.

- **Scalable Database Connection:**  
  Asynchronous operations with Motor provide high performance with MongoDB Atlas.

- **Easy Integration:**  
  Part of the larger Sudoku Solver ecosystem, it works in harmony with the client, server, and aggregator modules.

---

## 🛠️ Tech Stack

| Component               | Technology                             |
| ----------------------- | -------------------------------------- |
| **Web Framework**       | FastAPI                                |
| **Database**            | MongoDB Atlas (accessed via Motor)     |
| **Authentication**      | JWT (HS256), Passlib with bcrypt         |
| **Environment Management** | python-dotenv                       |

---

## 📁 Project Structure

```plaintext
auth/
├── .gitignore          # Git ignore rules for Python, virtual environments, and IDE files
├── __init__.py         # Package initialization file
├── auth_service.py     # Core authentication logic (registration, login, token generation)
├── database.py         # MongoDB connection setup using Motor
├── main.py             # FastAPI application entry point
├── models.py           # Pydantic models for request and response validation
└── requirements.txt    # Python dependencies for the auth service

### Prerequisites

- **Python 3.9+**
- **FastAPI & Uvicorn**
- A running instance of MongoDB Atlas (or local MongoDB for development)

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/davideblesse/sudoku-auth.git
    cd sudoku-auth
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables:**

    Create a `.env` file in the root directory with the following variables:
    - `MONGO_URI` – Your MongoDB connection string.
    - `JWT_SECRET_KEY` – A secret key for JWT token encoding.

4. **Run the Service:**

    ```bash
    uvicorn main:app --reload
    ```

    The service will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/davideblesse/sudoku-auth) if you have suggestions, improvements, or bug fixes.

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).