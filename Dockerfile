FROM python:3.8.7-slim-buster
WORKDIR /app
RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD uvicorn src.main:app --port 80 --host 0.0.0.0 --reload
