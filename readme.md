# FastAPI Docker App

## Features
- Simple FastAPI backend
- GET and POST APIs
- Dockerized application

## How to run

### Without Docker
python -m uvicorn main:app --reload

### With Docker
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app

## Endpoints
- GET /
- GET /items
- POST /items