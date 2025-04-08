# Flask Docker Application

A simple Flask application containerized with Docker.

## Build and Run

Build the Docker image:
```bash
docker build -t flask-app .
```

Run the container:
```bash
docker run -p 5000:5000 flask-app
```

Access the application at: http://localhost:5000