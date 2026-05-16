FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
    PYTHONPATH="${PYTHONPATH}:/app"

RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    build-essential libopenblas-dev libhdf5-dev \
    libprotobuf-dev protobuf-compiler python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --no-cache-dir -e .

EXPOSE 5000

CMD ["python", "application.py"]