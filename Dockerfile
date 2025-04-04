# Dockerfile
FROM python:3.10-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
# Install system dependencies
RUN apt-get update && apt-get install -y \
    espeak-ng \
    ffmpeg \
    git \
    build-essential \
    python3-dev \
    libffi-dev \
    libespeak-ng-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "ui/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
