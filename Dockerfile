FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system deps
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    build-essential libopenblas-dev libhdf5-dev \
    libprotobuf-dev protobuf-compiler python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install requirements first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the code
COPY . .

# Install your project in editable mode
RUN pip install --no-cache-dir -e .

EXPOSE 5000

CMD ["python", "-m", "application"]