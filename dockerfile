# python3 base image
FROM python:3
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV IS_CONTAINER 1
ENV POSTGRES_URL postgresql://sysdb:masterkey@db:5432/automation_build

# get image updates
RUN apt-get update -y && apt-get install -y build-essential apt-utils

# copy project files to container workdir
COPY ./app .

# install dependencies
RUN pip install -r requirements.txt

# run flask
ENTRYPOINT ["python3"]
CMD ["main.py"]