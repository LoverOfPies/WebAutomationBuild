# python3 base image
FROM python:3
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_URL postgresql://sysdb:masterkey@db:5432/automation_build
RUN apt-get update -y && apt-get install -y build-essential
COPY . /app
WORKDIR /app 
# install dependencies
RUN pip install -r requirements.txt
# expose port outside container
# EXPOSE 1337
# run flask
ENTRYPOINT ["python3"]
CMD ["main.py"]