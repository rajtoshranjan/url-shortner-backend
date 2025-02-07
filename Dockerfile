FROM python:3.12-slim

WORKDIR /app

ENV FLASK_APP=src/api.py

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "-c", "gunicorn_config.py", "src.api:app"]
