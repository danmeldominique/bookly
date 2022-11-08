FROM python:3.11

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Add a /app volume
VOLUME ["/app"]

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "80", "--reload"]