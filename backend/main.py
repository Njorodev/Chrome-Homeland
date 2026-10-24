from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import auth, properties
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup safely
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Database initialization warning: {e}")
    yield

app = FastAPI(title="Chrome Homeland API", version="1.0.2", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500", 
        "http://localhost:5500",
        "http://127.0.0.1:8080", 
        "http://localhost:8080",
        "https://chrome-homeland.onrender.com",
        "https://chrome-homeland-backend.vercel.app"  # Your backend domain if making self-requests
        
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(auth.router)
app.include_router(properties.router)

@app.get("/")
def root():
    return {"message": "Chrome Homeland API is running"}

@app.get("/api/health")
def health():
    return {"status": "ok"}
