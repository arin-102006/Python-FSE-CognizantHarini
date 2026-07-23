# Hands-On 10: Microservices Communication

## Services

- Course Service (Port 5001)
- Student Service (Port 5002)
- API Gateway (Port 5000)

## Architecture

The application is decomposed into two independent microservices:
- Course Service manages course information.
- Student Service manages student information and enrollment.
- API Gateway acts as a single entry point for clients.

## Communication

- Synchronous communication is implemented using the Python `requests` library.
- Student Service calls Course Service to verify a course before enrolling a student.
- Connection errors are handled by returning HTTP 503 (Service Unavailable).

## Technologies Used

- Flask
- SQLite
- Requests
