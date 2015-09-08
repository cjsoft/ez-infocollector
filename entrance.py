# coding=gbk
import sys,getopt
import os,flask
from flask import Flask
from flask import Response
from flask import request
app=Flask(__name__)

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
            return flask.render_template("template.html",content=formname)
por=8080
addres="0.0.0.0"
opts,args=getopt.getopt(sys.argv[1:],"h:p:")
for op,value in opts:
    if(op=="-h"):
        addres=value
    elif(op=="-p"):
        por=int(value)

app.debug=True
app.run(host=addres,port=por)