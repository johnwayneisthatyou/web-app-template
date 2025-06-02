from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings

app = FastAPI(title="Web App API")

# CORS configuration - use the list property
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,  # Use the property
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Web App API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
