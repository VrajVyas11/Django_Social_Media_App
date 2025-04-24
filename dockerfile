# Use a multi-stage build for smaller image size
# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim

WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /root/.local /root/.local

# Copy project files
COPY . .

# Collect static files for WhiteNoise
RUN python manage.py collectstatic --no-input

# Expose port (Render uses 10000 by default)
EXPOSE 10000

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Run migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn 04_Social_Media_App/SocialMedia/SocialMedia/wsgi.py:application --bind=0.0.0.0:10000"]