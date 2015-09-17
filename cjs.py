from __future__ import unicode_literals
import os,json
import sys
import MySQLdb
import uuid
class dumb(object):
    def __init__(self):
        a=os.getenv("VCAP_SERVICES")
        #print a
        if(a is None):
            a="{\"mysql\":[{\"name\":\"cjsoft-ez-infocollector\",\"label\":\"mysql\",\"tags\":[\"mysql\"],\"plan\":\"default\",\"credentials\":{\"hostname\":\"127.0.0.1\",\"port\":3306,\"name\":\"testdb\",\"username\":\"root\",\"password\":\"airport\",\"uri\":\"mysql://root:airport@10.9.1.188:3306/testdb?reconnect=true\",\"jdbcUrl\":\"jdbc:mysql://127.0.0.1:3306/testdb?user=root&password=airport\"}}]}"
        vcap_services=json.loads(a.encode("utf8"))
        sqlservices=vcap_services[u"mysql"][0]
        self.name=sqlservices[u"credentials"][u"name"]
        #print vcap_services
        self.hostname=sqlservices[u"credentials"][u"hostname"]
        self.port=sqlservices[u"credentials"][u"port"]
        self.username=sqlservices[u"credentials"][u"username"]
        self.password=sqlservices[u"credentials"][u"password"]
        self.uri=sqlservices[u"credentials"][u"uri"]
        self.jdbcUrl=sqlservices[u"credentials"][u"jdbcUrl"]
        #print os.getenv("VCAP_SERVICES")

sqlinfo=dumb()



def connect():
    global sqlinfo,sqlconnection,sql
    global execute,commit
    sqlconnection=MySQLdb.connect(host=sqlinfo.hostname,user=sqlinfo.username,passwd=sqlinfo.password,db=sqlinfo.name,port=sqlinfo.port)
    sql=sqlconnection.cursor()
    sqlconnection.select_db(sqlinfo.name)
    sqlconnection.set_character_set('utf8')
    #sql.execute("create table if not exists test(id int,info varchar(256))")
    #for i in range(100):
    #    sql.execute("insert into test values(%s,%s)",[i,"dasf%s"%i])
    #sqlconnection.commit()
    sql.execute("alter database %s character set utf8"%sqlinfo.name)
    commit=sqlconnection.commit
    execute=sql.execute


def close():
    sql.close()
    sqlconnection.close()
    
def select():
    execute("select * from f2 into outfile \"/tmp/asd.xls\"")
    a=sql.fetchall()
    for i in a:
        print i[1].decode("utf8")

def export(dbname):
    if(False):
        ask="temp/ez-infocollector_%s.out"%uuid.uuid4()
        while(os.path.isfile(ask)):
            ask="temp/ez-infocollector_%s.out"%uuid.uuid4()
    else:
        if not(os.path.isdir(os.path.join(os.getcwd(),"tmp"))):
            os.makedirs(os.path.join(os.getcwd(),"tmp"))
        ask=os.path.join(os.getcwd(),"tmp","%s.out"%uuid.uuid4())
        while(os.path.isfile(ask)):
            ask=os.path.join(os.getcwd(),"tmp","%s.out"%uuid.uuid4())
    execute("select * from %s"%dbname)
    a=sql.fetchall()
    f=open(ask,"w")
    for i in a:
        for j,k in enumerate(i):
            if type(k) is str:
                f.write(str(k).encode("gb2312"))
            else:
                f.write(str(k).encode("gb2312"))
            if(j!=len(i)-1):
                f.write("\t".encode("gb2312"))
        f.write("\n".encode("gb2312"))
    f.close()
    return ask
