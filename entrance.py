#-*- coding=utf-8 -*-
import sys,getopt
import os,flask,json
from flask import Flask
from flask import Response
from flask import request
app=Flask(__name__)

def makeform(alist):
    tempstr=""
    for i in alist:
        if "value" in i:
            tempstr+="%s<input type=\"%s\" name=\"%s\" value=\"%s\" />%s<br>"%(i.get("precaption",""),i.get("type",""),i.get("name",""),i.get("value",""),i.get("poscaption",""))
        else:
            tempstr+="%s<input type=\"%s\" name=\"%s\" />%s<br>"%(i.get("precaption",""),i.get("type",""),i.get("name",""),i.get("poscaption",""))
    return "<form>%s</form>"%tempstr

def getpath(rph):
    return os.path.join(os.getcwd(),rph);

@app.route("/")
def root():
    return app.send_static_file('index.html')
    if os.path.exists("index.html"):
        return app.send_static_file("index.html")
    elif os.path.exists("index.htm"):
        return app.send_static_file("index.htm")
@app.route("/form")
@app.route("/form/<formname>",methods=["POST","GET"])
def mfr(formname=None):
    a=list()
    a.append({"type":"text","name":"inputbox1","precaption":"please input","poscaption":"666"})
    a.append({"type":"text","name":"inputbox2","precaption":"please input","value":"hello","poscaption":"667"})
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
            if os.path.isfile(getpath("infoforms/%s/main.cjsx"%formname)):
                f=open(getpath("infoforms/%s/main.cjsx"%formname),"r")
                a=json.loads(f.read())
                print a
            return flask.render_template("template.html",title="CJSoft Info Collector/%s"%formname,content=("<h2>%s</h2><a href=/form>返回</a><br>%s"%(formname,makeform(a))).decode("utf-8"))
por=8080
addres="0.0.0.0"
opts,args=getopt.getopt(sys.argv[1:],"h:p:")
for op,value in opts:
    if(op=="-h"):
        addres=value
    elif(op=="-p"):
        por=int(value)


reload(sys)
sys.setdefaultencoding('utf-8')
app.debug=True
app.run(host=addres,port=por)