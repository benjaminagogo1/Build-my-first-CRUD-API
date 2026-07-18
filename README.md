Phase 0 — Understand the destination

Before writing a single line of code, we answer one question:

What exactly are we building?

At the end of this phase, you should be able to explain to someone:

"A CRUD API is a server that waits for HTTP requests. Depending on the request, it creates, reads, updates, or deletes tasks and sends back an HTTP response."

No coding yet.

Phase 1 — List every concept we need

Instead of jumping into Stage 0 of the assignment, we'll extract the concepts hidden inside it.

Something like this:

What is the Internet?
What is the Web?
What is HTTP?
Client vs Server
Request vs Response
URL
Endpoint
Route
HTTP Methods (GET, POST, PUT, DELETE)
Status Codes
JSON
REST
CRUD
FastAPI
Swagger
Path Parameters
Request Body
Validation
Git workflow

Notice something?

Most of these are ideas, not programming.

Phase 2 — Learn only what Stage 0 needs

The assignment starts with:

Hello, Server

But before that, we should know:

What is a server?
Why does it keep running?
Why localhost?
Why port 8000?
What happens when you open a browser?

Only then will we build the first FastAPI program.

Phase 3 — Build incrementally

Exactly as FlyRank suggests.

Instead of writing a whole CRUD API, we'll celebrate tiny milestones.

For example:

Day 1

Browser
     ↓
localhost:8000
     ↓
FastAPI
     ↓
"Hello World"

That's success.

Day 2

GET /

returns

{
  "name": "Task API"
}

Another success.

Day 3

GET /health

returns

{
  "status": "ok"
}



HTTP is the set of rules that tells a client and a server how to communicate.
HTTP is a communication protocol.

What is a protocol?

A protocol is simply:

An agreed set of rules for communication.

The method tells the server what action the client wants to perform.


What is JSON?

Think of JSON as a standard way of writing data so that different programming languages can understand each other.
JSON = JSON (JavaScript Object Notation).


HTTP tells us how to communicate.
GET tells us what action we want.
/tasks tells us which resource we're talking about.
JSON is the format used to exchange the data.



How does Uvicorn know about my FastAPI application?

The answer lies in this command:

uvicorn main:app --reload









                You press Enter
                       │
                       ▼
                 Browser (Client)
                       │
        Creates an HTTP Request
                       │
                       ▼
                  Uvicorn (Server)
        "Someone is making a request."
                       │
                       ▼
                  FastAPI
        "Which function handles GET /tasks?"
                       │
                       ▼
              Python Interpreter
        "Run get_tasks()."
                       │
                       ▼
              Your Python Function

def get_tasks():
    return tasks
                       │
                       ▼
              Python returns a list
                       │
                       ▼
                  FastAPI
 Converts the Python list/dictionaries into JSON
 Creates the HTTP response
                       │
                       ▼
                  Uvicorn
 Sends the HTTP response over the network
                       │
                       ▼
                 Browser
 Displays the result