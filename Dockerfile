
FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y
EXPOSE 5000 
EXPOSE 8080
EXPOSE 5001
RUN apt-get update && pip install -r requirements.txt
CMD ["python3", "app.py","app_fastapi.py"]
#app

