FROM python:3.9.9-alpine3.14

WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN chmod +x ./env.sh
RUN ./env.sh
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN ["python", "manage.py", "test"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000