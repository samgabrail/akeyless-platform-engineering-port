FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/
COPY run.py .

CMD ["python", "-u", "run.py"]