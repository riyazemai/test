FROM python:3.12.3-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8111

CMD ["python", "run.py"]