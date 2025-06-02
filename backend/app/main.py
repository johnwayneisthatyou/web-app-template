from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load .env (DATABASE_URL, JWT_SECRET, etc.)
load_dotenv()

app = FastAPI(title="Template Web App API")

# CORS – allow Next.js localhost (port 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
async def health_check():
    return {"status": "ok"}


# Later: include routers, e.g.
# from .api.jobs import router as jobs_router
# app.include_router(jobs_router, prefix="/jobs", tags=["Jobs"])
