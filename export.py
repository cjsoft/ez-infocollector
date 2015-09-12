import zipfile
import uuid,os
# import chardet
def collect_uploads(dbname,sqlpath):
    if not(os.path.isdir(os.path.join(os.getcwd(),"export"))):
        os.makedirs(os.path.join(os.getcwd(),"export"))
    ask=os.path.join(os.getcwd(),"export",str(uuid.uuid4())+".zip")
    if os.path.isfile(ask):
        ask=os.path.join(os.getcwd(),"export",str(uuid.uuid4())+".zip")    
    zipf=zipfile.ZipFile(ask,mode="w",compression=zipfile.ZIP_STORED)
    if(os.path.isfile(sqlpath)):

        zipf.write(sqlpath,"export.xls")
        
    if(os.path.isdir(os.path.join(os.getcwd(),"upload",dbname))):
        flist=os.listdir(os.path.join(os.getcwd(),"upload",dbname))
    else:
        flist=list()
    for i in flist:
        zipf.write(os.path.join(os.getcwd(),"upload",dbname,i),os.path.join("upload",dbname,i))
    zipf.close()
    os.remove(sqlpath)
    return ask