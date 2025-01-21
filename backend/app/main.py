from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI application
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World from FastAPI on Vercel!"}


# Your existing routes can be kept here
# For example:
# @app.get("/api/some-route")
# def some_route():
#     return {"message": "Some route"}
