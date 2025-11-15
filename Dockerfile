FROM python:3.12-slim

# Install pipenv
RUN pip install pipenv

# Set working directory
WORKDIR /app

# Copy dependency files first (better for caching)
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install all dependencies system-wide
RUN pipenv install --system --deploy

# Copy your app code and model
COPY ["notebooks/predict.py", "notebooks/model_pipeline.bin", "./"]

# Expose the port Gunicorn will use
EXPOSE 9696

# Launch app with Gunicorn (uses predict:app)
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
