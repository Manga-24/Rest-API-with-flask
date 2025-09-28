# Task 4: Build a REST API with Flask

### Objective
[cite_start]The objective of this task was to create a REST API that manages user data[cite: 50]. [cite_start]The outcome is to understand API development fundamentals[cite: 56].

### Tools Used
* [cite_start]Python [cite: 51]
* [cite_start]Flask [cite: 51]
* [cite_start]Postman or Curl (for testing the API) [cite: 51]

### Deliverables
[cite_start]This repository contains a Flask application with `GET`, `POST`, `PUT`, and `DELETE` routes[cite: 52].

### How to Run and Test the API
1.  **Install the required library**:
    ```bash
    pip install Flask
    ```
2.  **Run the Flask application** from your terminal:
    ```bash
    python app.py
    ```
    The server will start and run on `http://127.0.0.1:5000`.

3.  **Test the API** using a tool like Postman or Curl:
    * `GET` all users: `http://127.0.0.1:5000/users`
    * `GET` a specific user: `http://127.0.0.1:5000/users/1`
    * `POST` to create a new user: `http://127.0.0.1:5000/users` (with JSON data in the body)
    * `PUT` to update a user: `http://127.0.0.1:5000/users/1` (with JSON data in the body)
    * `DELETE` a user: `http://127.0.0.1:5000/users/1`

### Key Concepts
This task covered the following key concepts:
* [cite_start]REST [cite: 69]
* [cite_start]HTTP Methods [cite: 69]
* [cite_start]Flask [cite: 69]
