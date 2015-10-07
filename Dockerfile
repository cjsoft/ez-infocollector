# FROM ubuntu
 
# RUN apt-get update
# RUN apt-get install -y python-setuptools build-essential
# RUN apt-get install -y mysql-client
# RUN apt-get install -y libmysqld-dev libmysqlclient-dev
# RUN easy_install pip

# EXPOSE 8080
# EXPOSE 80
# RUN mkdir -p /app
# COPY . /app
# WORKDIR /app
# RUN ls -al
# RUN pip install -r requirements.txt
# CMD ["python", "./entrance.py", "-h 0.0.0.0 -p 80"]

FROM daocloud.io/python:2-onbuild
RUN apt-get update


RUN apt-get install -y mysql-client
RUN apt-get install -y libmysqld-dev libmysqlclient-dev


EXPOSE 80
EXPOSE 8080
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","./a.py"]