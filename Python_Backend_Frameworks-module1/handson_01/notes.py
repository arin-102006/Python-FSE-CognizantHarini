"""
Task 1 - Web Framework Foundations

1. Request-Response Cycle
Browser
   ↓
URL Router
   ↓
View
   ↓
Model (Database)
   ↓
Response
   ↓
Browser

2. Middleware
- SecurityMiddleware: Adds security features.
- SessionMiddleware: Handles user sessions.

3. WSGI vs ASGI
- WSGI handles synchronous requests.
- ASGI handles asynchronous requests.
- Django uses WSGI by default.
- ASGI is preferred for WebSockets and async applications.

4. MVC vs MVT
MVC            Django MVT
--------------------------
Model     ->   Model
View      ->   Template
Controller->   View
"""