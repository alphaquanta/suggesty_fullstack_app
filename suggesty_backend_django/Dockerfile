FROM python:3.9.9-alpine3.14
WORKDIR /backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000

