import os,json
import MySQLdb
class dumb(object):
    def __init__(self):
        vcap_services=json.loads("{\"mysql\":[{\"name\":\"cjsoft-ez-infocollector\",\"label\":\"mysql\",\"tags\":[\"mysql\"],\"plan\":\"default\",\"credentials\":{\"hostname\":\"127.0.0.1\",\"port\":3306,\"name\":\"testdb\",\"username\":\"root\",\"password\":\"airport\",\"uri\":\"mysql://root:airport@10.9.1.188:3306/testdb?reconnect=true\",\"jdbcUrl\":\"jdbc:mysql://127.0.0.1:3306/testdb?user=root&password=airport\"}}]}".encode("utf8"))
        sqlservices=vcap_services[u"mysql"][0]
        self.name=sqlservices[u"credentials"][u"name"]
        self.hostname=sqlservices[u"credentials"][u"hostname"]
        self.port=sqlservices[u"credentials"][u"port"]
        self.username=sqlservices[u"credentials"][u"username"]
        self.password=sqlservices[u"credentials"][u"password"]
        self.uri=sqlservices[u"credentials"][u"uri"]
        self.jdbcUrl=sqlservices[u"credentials"][u"jdbcUrl"]
        #print os.getenv("VCAP_SERVICES")

sqlinfo=dumb()



def connect():
    global sqlinfo
    global sqlconnection
    global sql
    sqlconnection=MySQLdb.connect(host=sqlinfo.hostname,user=sqlinfo.username,passwd=sqlinfo.password,db=sqlinfo.name,port=sqlinfo.port)
    sql=sqlconnection.cursor()
    sqlconnection.select_db(sqlinfo.name)
    sqlconnection.set_character_set('utf8')
    #sql.execute("create table if not exists test(id int,info varchar(256))")
    #for i in range(100):
    #    sql.execute("insert into test values(%s,%s)",[i,"dasf%s"%i])
    #sqlconnection.commit()
    sql.execute("alter database %s character set utf8"%sqlinfo.name)
connect()
    
commit=sqlconnection.commit
execute=sql.execute

def close():
    sql.close()
    sqlconnection.close()