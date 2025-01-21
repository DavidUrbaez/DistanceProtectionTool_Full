from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS2
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://davidurbaez.github.io", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World from FastAPI on Vercel!"}


@app.get("/api/hello")
def hello_api():
    return {"message": "Hello from API route!"}
