#!/usr/bin/python
#-*- coding=utf-8 -*-

aucode="cjsoft"
maxuploadlimit=20*1024*1024
secretkey="s%#$ra4$^q3$^25w&rae24s"

import sys,getopt,shutil
import os,flask,json,cjs
import uuid,recapcha
import export
from flask import url_for
from flask import Flask
from flask import Response
from flask import request
from werkzeug import SharedDataMiddleware
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
        print  ",".join(s)
        return ",".join(s)
    if(type(alist)is list):
        return ",".join(map(str,alist))

def makeform(alist):
    return "%s<br><br>%s<br><input type=\"submit\" value=\"提交\"></form>"%(alist,flask.render_template("recaptcha.html",recaptcha="true"))
    tempstr=""
    for i in alist:
        if "value" in i:
            tempstr+="%s<input type=\"%s\" name=\"%s\" value=\"%s\" />%s<br>"%(i.get(u"precaption",""),i.get(u"type",""),i.get(u"name",""),i.get(u"value",""),i.get(u"poscaption",""))
        else:
            tempstr+="%s<input type=\"%s\" name=\"%s\" />%s<br>"%(i.get(u"precaption",""),i.get(u"type",""),i.get(u"name",""),i.get(u"poscaption",""))
    return "<form method=\"post\">%s<br>%s<br><input type=\"submit\" value=\"提交\"></form>"%(tempstr,flask.render_template("recaptcha.html",recaptcha="true"))

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
                    if(os.path.isdir(getpath(os.path.join("infoforms" , i)))):
                        if(os.path.isfile(getpath(os.path.join("infoforms",i,"main.cjsx")))):
                            st+="<a href=form/%s>%s</a><br>"%(i,i)
                return flask.render_template("template.html",content=flask.render_template("formlist.html",content=st))
            else:
                if not os.path.isdir(getpath(os.path.join("infoforms" , formname))):
                    return ''
                if not(os.path.isfile(getpath(os.path.join("infoforms",formname,"db.lock")))):
                    sqlstr=makesqlstr(json.loads(readfile(getpath(os.path.join("infoforms",formname,"main.cjsx")))))
                    cjs.connect()
                    cjs.execute("drop table if exists %s"%formname)
                    # print ("create table %s(%s)"%(formname,sqlstr))
                    cjs.execute("create table %s(%s)"%(formname,sqlstr))
                    cjs.commit()
                    cjs.close()
                    f=open(os.path.join("infoforms",formname,"db.lock"),"w")
                    f.write("lock")
                    f.close()
                if os.path.isfile(os.path.join("infoforms",formname,"main.cjsx")):
                    f=open(getpath(os.path.join("infoforms",formname,"main.cjsx")),"r")
                    a=json.loads(f.read().decode("utf8"))
                return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form style=\"font-size:18px\">返回</a><br><br>%s"%(formname,makeform(readfile(getpath("infoforms/%s/form.html"%formname))))).decode("utf-8"))
        else:
            files= request.files.to_dict()
            form=request.form.to_dict()
            print form["recaptcha"].upper(), flask.session.get("recap").upper()
            if (form["recaptcha"].upper()!=flask.session.get("recap").upper() or flask.session.get("recap")==""):
                return flask.render_template("template.html",title="CJSoft Info Collector",content="%s<br><br>%s<br><input type=\"submit\" value=\"提交\"></form>"%(readfile(getpath("infoforms/%s/form.html"%formname)),flask.render_template("recaptcha.html",recaptcha="true",inrecap="true")))
            del form["recaptcha"]
            flask.session["recap"]="never post again"
            if not os.path.isdir(getpath(os.path.join("upload",formname))):
                os.makedirs(getpath(os.path.join("upload",formname)))
            
            for i in files:
                ask=os.path.join("upload",formname,str(uuid.uuid4())+os.path.splitext(request.files[i].filename)[1])
                while(os.path.isfile(ask)):
                    ask=os.path.join("upload",formname,str(uuid.uuid4())+os.path.splitext(request.files[i].filename)[1])
                request.files[i].save(getpath(ask))
                if(os.path.getsize(getpath(ask))==0):
                	os.remove(getpath(ask))
                	form[i]=""
                else:
                	form[i]=ask
            
            alist=list()
            blist=[i for i in form]
            for i in form:
                alist.append(form[i])
            # print "insert into %s values(%s)"%(formname,makesqlstr(alist))
            cjs.connect()
            cjs.execute("insert into %s(%s) values(%s)"%(formname,makesqlstr(blist),makesqlstr(len(alist))),alist)
            cjs.commit()
            cjs.close()
            return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>成功，对象</h2><h2>%s</h2><h2>已加入数据库，文件（若有）已被上传并索引</h2><a href=/form style=\"font-size:18px\">返回</a>"%str(form)))
    except ZeroDivisionError:
        pass
    except AttributeError,e:
        print e
        return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form style=\"font-size:18px\">返回</a><br><br>唔，看起来这个表单无法渲染"%formname).decode("utf-8"))
    except BaseException,e:
        print e
        return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form style=\"font-size:18px\">返回</a><br><br>唔，遇到了一点错误,你是不是写错了格式？"%formname).decode("utf-8"))
@app.route("/export/<dbname>",methods=["POST","GET"])
def exportresults(dbname):
    if request.method=="GET":
        return flask.render_template("template.html",title="CJSoft Info Collector",content=flask.render_template("au.html",fn=dbname,extra=""))
    else:
        global aucode
        if request.form.to_dict()["aucode"]==aucode:
            if(os.path.isfile(getpath(os.path.join("infoforms",dbname,"db.lock")))):
                sqlpath=cjs.export(dbname)
                rstr=export.collect_uploads(dbname,sqlpath)
                psplit=os.path.split(rstr)
                f= flask.send_from_directory(psplit[0],psplit[1])
                os.remove(rstr)
                return f
            else:
                return flask.render_template("template.html",title="CJSoft Info Collector",content=("<h2>导出失败，没有可供导出的数据</h2>").decode("utf8"))
        else:
            return flask.render_template("template.html",title="CJSoft Info Collector",content=flask.render_template("au.html",fn=dbname,extra="鉴权码错误".decode("utf8")))
@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

@app.route("/recapcha.py")
@app.route("/recapcha.py/<iii>")
def recap(iii=None):
    a,b=recapcha.create_validate_code()
    flask.session["recap"]=b
    print b
    temp=a.read()
    a.close()
    return flask.Response(temp, mimetype='image/jpeg')
por=8080
addres="0.0.0.0"
opts,args=getopt.getopt(sys.argv[1:],"h:p:o:")
for op,value in opts:
    if(op=="-h"):
        addres=value
    elif(op=="-p"):
        por=int(value)
    elif(op=="-o"):
        pass

reload(sys)
app.secret_key=secretkey
sys.setdefaultencoding('utf-8')
app.config['MAX_CONTENT_LENGTH'] = maxuploadlimit

app.debug=False
app.run(host=addres,port=por)

