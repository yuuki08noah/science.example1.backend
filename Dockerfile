FROM python:3.12
WORKDIR app

COPY . /app

RUN ["pip", "install", "-r", "requirements.txt", "--no-cache-dir"]
CMD ["python3", "main.py"]
EXPOSE 8000