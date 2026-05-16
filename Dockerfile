FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libopenblas-dev \
    libhdf5-dev \
    libprotobuf-dev \
    protobuf-compiler \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Install in editable mode (if needed)
RUN pip install --no-cache-dir -e .

# === IMPORTANT: Do NOT train here ===
# Remove or comment this line:
# RUN python pipeline/training_pipeline.py

EXPOSE 5000

CMD ["python", "application.py"]