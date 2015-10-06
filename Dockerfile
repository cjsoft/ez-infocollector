FROM ubuntu
RUN apt-get install -y python
RUN apt-get install -y mysql-server zlib1g-dev
RUN apt-get install -y libmysqld-dev libmysqlclient-dev
RUN apt-get install -y python-dev python-pip build-essential

EXPOSE 80
EXPOSE 8080
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","entrance.py","-h 0.0.0.0 -p 80"]