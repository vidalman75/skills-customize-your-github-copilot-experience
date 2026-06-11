# 📘 Assignment: Building REST APIs with FastAPI Framework

## 🎯 Objective

Build a small REST API with FastAPI that manages a list of books or tasks. This assignment will help you practice defining routes, accepting JSON input, validating data, and returning clear API responses.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a basic FastAPI application with at least one health check endpoint and a route that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance.
- Add a GET route at `/health` that returns a JSON message such as `{"status": "ok"}`.
- Add a GET route at `/` that returns a friendly welcome message.
- Run the app locally with Uvicorn.

### 🛠️ Create REST Endpoints

#### Description
Extend the API so it can create and retrieve items using JSON payloads.

#### Requirements
Completed program should:

- Define a simple Pydantic model for an item, such as `id`, `name`, and `description`.
- Add a GET route to list all items.
- Add a POST route to create a new item.
- Return appropriate JSON responses and handle invalid input gracefully.

### 🛠️ Validate and Test the API

#### Description
Verify the API behavior by testing the endpoints with sample requests.

#### Requirements
Completed program should:

- Use `curl` or a browser to test the `/health` and `/items` endpoints.
- Confirm that POST requests create new items correctly.
- Show at least one example request and response in your notes.
