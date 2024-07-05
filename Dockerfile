FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy your Python script and any required files into the container
COPY src/main.py /app/
COPY src/playlistMusicDownloader.py /app/
COPY src/playlistVideoDownloader.py /app/
COPY requirements.txt /app/

# Install any required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define an entry point (the script to run when the container starts)
ENTRYPOINT ["python", "main.py"]