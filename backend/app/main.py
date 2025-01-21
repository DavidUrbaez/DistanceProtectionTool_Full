from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI(
    title="Your API",
    description="Your API Description",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Hello World from FastAPI on Vercel!"}


@app.get("/api/some-route")
async def some_route():
    return {"message": "Some route"}


# Handler for Vercel serverless
handler = Mangum(app, lifespan="off")
