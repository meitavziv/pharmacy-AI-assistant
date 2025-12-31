FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /app/backend/
COPY frontend/ /app/frontend/
COPY backend/.env /app/backend/.env


EXPOSE 5000

ENV PYTHONUNBUFFERED=1

# Start the Flask server
CMD ["python", "backend/main.py"]
