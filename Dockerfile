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
CMD ["python","/app/entrance.py","-h","0.0.0.0","-p",$PORT]