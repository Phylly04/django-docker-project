from python:3.9-slim
WORKDIR ./app
COPY . /app
CMD ["python", "manage.py", "runserver"]