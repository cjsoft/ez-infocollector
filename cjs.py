import os,json
import MySQLdb
class dumb(object):
	def __init__(self):
		vcap_services=json.loads(os.getenv("VCAP_SERVICES").encode("utf8"))
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
    sql.execute("create table if not exists test(id int,info varchar(256))")
    for i in range(100):
        sql.execute("insert into test values(%s,%s)",[i,"dasf%s"%i])
    sqlconnection.commit()
    sql.close()
    sqlconnection.close()
connect()
    