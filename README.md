# Web App Template

A modern web application template with Next.js frontend and Python FastAPI backend.

## Tech Stack

### Frontend
- Next.js 15 with App Router
- TypeScript
- Tailwind CSS
- Shadcn UI
- TanStack Query
- React Hook Form
- Zod

### Backend
- FastAPI
- SQLAlchemy
- Alembic
- Prisma
- PostgreSQL

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL

### Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd your-project
```

2. Setup Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your database credentials
alembic upgrade head
```

3. Setup Frontend
```bash
cd frontend
npm install
cp .env.example .env.local
# Edit .env.local with your API URL
```

4. Run the application
```bash
# Terminal 1 - Backend
cd backend
uvicorn src.main:app --reload

# Terminal 2 - Frontend
cd frontend
npm run dev
```

Visit http://localhost:3000

## Development

### Database Migrations
```bash
cd backend
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

### Testing
```bash
# Frontend
cd frontend
npm test

# Backend
cd backend
pytest
```

## Deployment

[Add your deployment instructions here]

## Contributing

[Add your contributing guidelines here]