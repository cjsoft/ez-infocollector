from __future__ import unicode_literals
import os,json
import sys
import MySQLdb
import uuid,xlwt
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

def xlsstyle(bold=False,top=0,right=0,bottom=0,left=0):
    style=xlwt.XFStyle()
    borders=xlwt.Borders()
    borders.top=top
    borders.right=right
    borders.left=left
    borders.bottom=bottom
    font=xlwt.Font()
    font.bold=bold
    style.borders=borders
    style.font=font
    return style
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
    connect()
    workbook=xlwt.Workbook(encoding="utf-8")
    sheet=workbook.add_sheet("Sheet1",cell_overwrite_ok=True)
    execute("desc %s;"%dbname)
    structure=sql.fetchall()
    st=xlsstyle(True,1,1,1,1)
    ali=xlwt.Alignment()
    ali.horz=2
    st.alignment=ali
    sheet.write_merge(0,0,0,len(structure)-1,dbname,st)
    for i in range(len(structure)):
        sheet.write(1,i,structure[i][0],xlsstyle(True))
    cnt=2
    execute("select * from %s;"%dbname)
    a=sql.fetchall()
    st=xlsstyle()
    ali=xlwt.Alignment()
    ali.horz=1
    st.alignment=ali
    for i in a:
        for j in range(len(i)):
            sheet.write(cnt,j,i[j],st)
        cnt=cnt+1
    workbook.save(ask)
    close()
    # f=open(ask,"w")
    # for i in a:
    #     for j,k in enumerate(i):
    #         if type(k) is str:
    #             f.write(str(k).encode("gb2312"))
    #         else:
    #             f.write(str(k).encode("gb2312"))
    #         if(j!=len(i)-1):
    #             f.write("\t".encode("gb2312"))
    #     f.write("\n".encode("gb2312"))
    # f.close()
    return ask

# reload(sys)
# sys.setdefaultencoding('utf-8')