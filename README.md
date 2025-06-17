# User Management API (Django REST Framework)

This repository contains a Django project that implements a RESTful API for managing user resources. It includes features for creating, retrieving, updating, and deleting users.

The project also includes an optional management command to demonstrate making a gRPC request to a public API.

## Features

*   **User CRUD Operations:** Full Create, Read, Update, Delete functionality for users.
*   **API Endpoints:** Built with Django REST Framework using ViewSets and Routers.
*   **Custom User Model:** A simple, custom User model with `id`, `username`, `email`, `first_name`, `last_name`, and `date_joined`.
*   **gRPC Client Demo:** A Django management command to interact with the public Postman Echo gRPC service.

## Project Structure

```
.
├── UserManagement/      # Django project configuration
├── users/               # Django app for user management
├── grpc_requests/       # gRPC .proto file and generated client code
├── manage.py            # Django's command-line utility
├── requirements.txt     # Python package dependencies
└── README.md            # This file
```

## Setup and Installation

Follow these steps to set up and run the project locally.

### Prerequisites

*   Python 3.8+
*   `pip` and `venv`

### 1. Clone the Repository

```bash
git clone https://github.com/Lakshay-45/Dj-CRUD
cd django-assessment
```

### 2. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install all required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Create the database schema based on the models defined in the project.

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Usage

The API is browsable through Django REST Framework. The main endpoint is:

*   **`http://127.0.0.1:8000/api/users/`**

You can use a web browser or an API client like Postman to perform the following actions:

*   **`GET /api/users/`**: Retrieve a list of all users.
*   **`POST /api/users/`**: Create a new user. Required fields: `username`, `email`.
*   **`GET /api/users/{id}/`**: Retrieve the details of a specific user.
*   **`PUT /api/users/{id}/`**: Update all fields of a specific user.
*   **`PATCH /api/users/{id}/`**: Partially update the fields of a specific user.
*   **`DELETE /api/users/{id}/`**: Delete a specific user.

## Running the gRPC Request Script

This project includes a management command to make a gRPC request to a **locally hosted** gRPC server, demonstrating a full client-server interaction.

### Purpose

The `grpc_server.py` script runs a simple gRPC Greeter service. The Django management command `make_grpc_request` acts as the client, sending a request to the local server and printing its response.

### How to Run

This process requires two separate terminals running in the project's root directory.

**1. Install the Local gRPC Package**

Before you can run the server or client, you must install the `grpc_requests` directory as an editable Python package. This makes the generated gRPC code available to the rest of the project.

Make sure your virtual environment is active, then run:

```bash
pip install -e grpc_requests/
```

**2. Start the gRPC Server (Terminal 1)**

In your first terminal, start the gRPC server script. It will run and wait for incoming connections.

```bash
python grpc_server.py
```
You should see the message: `INFO:root:gRPC server started on port 50051...`

Leave this terminal running.

**3. Run the gRPC Client (Terminal 2)**

In a second terminal (with your virtual environment active), run the Django management command to send a request to the server you just started.

```bash
python manage.py make_grpc_request
```

### Sample Output

If the server is running correctly, you will see the following output in **Terminal 2**:

```
Attempting to make a gRPC request to the local server...
Sending request to localhost:50051 with name: 'Django'
gRPC Response Received Successfully!
Server responded: 'Hello, Django'
gRPC request process finished
```

Simultaneously, you will see a new log message appear in **Terminal 1**, confirming it received the request:

```
INFO:root:Received request for name: Django
```

This confirms the entire gRPC client-server flow is working correctly.
