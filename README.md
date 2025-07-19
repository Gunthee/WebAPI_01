# 🧡 Let's play with api
https://687a2c36abb83744b7ebbdfe.mockapi.io/api/bu-summar-camp


# Magic-8ball game API

The 8Ball game is a game that provides random answers, similar to the one found at https://magic-8ball.com/.

---

## What is API?

An **API (Application Programming Interface)** is a set of rules and protocols for building and interacting with software applications.

---

## What is FastAPI?

**FastAPI** is a modern, fast web framework for building APIs with Python. It's known for its speed, automatic interactive API documentation, and ease of use, making API development efficient and enjoyable.

---

## What is DevContainer?

A **DevContainer (Development Container)** is a Docker container configured specifically for development purposes. It allows you to define a consistent, reproducible, and isolated development environment for your project. This means that all developers working on the project will have the exact same tools, dependencies, and configurations, regardless of their local machine setup, eliminating "it works on my machine" issues.

### How to start with DevContainer?

To start with a DevContainer, you typically need:

1.  **Docker:** To run the containers.
2.  **A code editor with DevContainer support:** Visual Studio Code is a popular choice with excellent DevContainer integration (via the "Remote - Containers" extension).
3.  **A `.devcontainer` folder in your project:** This folder contains configuration files (like `devcontainer.json` and optionally `Dockerfile`) that define your development environment (e.g., base image, extensions to install, ports to forward, etc.).

Once set up, your IDE will detect the DevContainer configuration and allow you to open your project directly within the containerized environment.

---

## SQLite

**SQLite** is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. It is the most used database engine in the world. It's an excellent choice for doing exercises and local development due to its lightweight nature and file-based storage.

### Table design for saving data

Here's a simple table design for storing answers in SQLite:

| Column | Type    | Description          |
|--------|---------|----------------------|
| `id`   | INTEGER | Primary Key, Auto-incrementing |
| `answer` | TEXT    | The 8-ball answer    |

Example data:

| id | answer |
|----|--------|
| 1  | "YES"  |
| 2  | "NO"   |
| 3  | "MAYBE" |

---

## 8ball API Requirements

Here are the requirements for the 8ball API:

* **`GET /8ball`**: When a `GET` request is made to this endpoint, the API will randomly select an answer from the list of available answers and return it in the HTTP response body as plain text.

* **`POST /8ball`**: When a `POST` request is made to this endpoint, it will allow you to add new answers to the list of available answers, which will then be saved in the SQLite database.

* **`PUT /8ball/{id}`**: When a `PUT` request is made to this endpoint with a specific `id` in the URL path, it will update the answer associated with that `id` in the SQLite database.

* **`DELETE /8ball/{id}`**: When a `DELETE` request is made to this endpoint with a specific `id` in the URL path, it will remove the answer associated with that `id` from the SQLite database.