#-*- coding=utf-8 -*-
import sys,getopt,shutil
import os,flask,json,cjs
from flask import Flask
from flask import Response
from flask import request
app=Flask(__name__)

def readfile(path):
    f=open(path,"r")
    tmp=f.read()
    f.close()
    return tmp

def makesqlstr(alist):
    if type(alist) is int:
        s=list()
        for i in range(alist):
            s.append("%s")
        return ",".join(s)
    if(type(alist)is list):
        return ",".join(map(str,alist))

def makeform(alist):
    return "<form method=\"post\">%s<br><br><input type=\"submit\" value=\"提交\"></form>"%alist
    tempstr=""
    for i in alist:
        if "value" in i:
            tempstr+="%s<input type=\"%s\" name=\"%s\" value=\"%s\" />%s<br>"%(i.get(u"precaption",""),i.get(u"type",""),i.get(u"name",""),i.get(u"value",""),i.get(u"poscaption",""))
        else:
            tempstr+="%s<input type=\"%s\" name=\"%s\" />%s<br>"%(i.get(u"precaption",""),i.get(u"type",""),i.get(u"name",""),i.get(u"poscaption",""))
    return "<form method=\"post\">%s<br><br><input type=\"submit\" value=\"提交\"></form>"%tempstr

def getpath(rph):
    return os.path.join(os.getcwd(),rph);

@app.route("/")
def root():
    if os.path.exists("index.html"):
        return app.send_static_file("index.html")
    elif os.path.exists("index.htm"):
        return app.send_static_file("index.htm")
# @app.route("/<path:path>")
# def sta(path):
#     #return "hello"
#     print "!!!"
    
#     if(len(os.path.splitext(path)[1])>0):
#         return app.send_static_file(path)
#     else:
#         return app.send_static_file(os.path.join(path,"index.html"))
@app.route("/form")
@app.route("/form/<formname>",methods=["POST","GET"])
def mfr(formname=None):
    try:
        if request.method=="GET":
            if formname==None:
                lst=os.listdir(getpath("infoforms"))
                st=""
                for i in lst:
                    if(os.path.isdir(getpath("infoforms/" + i))):
                        if(os.path.isfile(getpath(os.path.join("infoforms",i,"main.cjsx")))):
                            st+="<a href=form/%s>%s</a><br>"%(i,i)
                return flask.render_template("template.html",content=flask.render_template("formlist.html",content=st))
            else:
                if not(os.path.isfile(getpath("infoforms/%s/db.lock"%formname))):
                    sqlstr=makesqlstr(json.loads(readfile(getpath("infoforms/%s/main.cjsx"%formname))))
                    cjs.execute("drop table if exists %s"%formname)
                    # print ("create table %s(%s)"%(formname,sqlstr))
                    cjs.execute("create table %s(%s)"%(formname,sqlstr))
                    cjs.sqlconnection.commit
                    f=open("infoforms/%s/db.lock"%formname,"w")
                    f.write("lock")
                    f.close()
                if os.path.isfile(getpath("infoforms/%s/main.cjsx"%formname)):
                    f=open(getpath("infoforms/%s/main.cjsx"%formname),"r")
                    a=json.loads(f.read().decode("utf8"))
                return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form>返回</a><br><br>%s"%(formname,makeform(readfile(getpath("infoforms/%s/form.html"%formname))))).decode("utf-8"))
        else:
            form=request.form.to_dict()
            alist=list()
            blist=[i for i in form]
            for i in form:
                alist.append(form[i])
            # print "insert into %s values(%s)"%(formname,makesqlstr(alist))
            cjs.execute("insert into %s(%s) values(%s)"%(formname,makesqlstr(blist),makesqlstr(len(alist))),alist)
            cjs.commit()

            # form=request.form.to_dict()
            # alist=list()
            # blist=json.loads(readfile(getpath("infoforms/%s/main.cjsx"%formname)))
            # for i in blist:
            #     alist.append(form.get(i.split(" ")[0],""))
            # print "insert into %s values(%s)"%(formname,makesqlstr(alist))
            # cjs.execute("insert into %s values(%s)"%(formname,makesqlstr(len(alist))),alist)
            # cjs.commit()
            
            return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form>返回</a><br><br>成功"%str(request.form)))
    except ZeroDivisionError:
            pass
    except AttributeError,e:
        print e
        return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form>返回</a><br><br>唔，看起来这个表单无法渲染"%formname).decode("utf-8"))
    except BaseException,e:
        print e
        return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form>返回</a><br><br>唔，遇到了一点错误,这极有可能是表单编写不规范造成的"%formname).decode("utf-8"))
por=8080
addres="0.0.0.0"
opts,args=getopt.getopt(sys.argv[1:],"h:p:")
for op,value in opts:
    if(op=="-h"):
        addres=value
    elif(op=="-p"):
        por=int(value)

reload(sys)
#cjs.connect()
sys.setdefaultencoding('utf-8')
app.debug=True
app.run(host=addres,port=por)