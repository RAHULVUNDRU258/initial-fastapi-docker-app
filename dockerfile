from python:3.10
workdir /app
copy . .
run pip install -r requirements.txt
cmd ["python","-m","uvicorn","main:app","--host","0.0.0.0","--port","8000"]
