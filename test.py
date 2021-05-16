import requests
import sys
import os
import subprocess
import webbrowser

def getdata(cmd):
    
    process=subprocess.Popen([sys.executable,cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,error=process.communicate()
    return output,error
def made_requests(errortype):
    
    r=requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(errortype))
    return r.json()
def get_urls(js):
    url_links=[]
    c=0
    for i in js["items"]:
        if(i["is_answered"]):
            url_links.append(i["link"])
            c=c+1
        if(c==5):
            break
    for i in url_links:
        webbrowser.open(i)
if __name__== "__main__":
    output,error=getdata("sample.py")
error=error.decode("utf-8")
if(error==""):
    print("NO ERRORS FOUND")
else:
    err=error.split("\n",3)
    errmsg=err[3].split(":",1)
    errortype=errmsg[0]
    errormsg=errmsg[1].strip()
js1=made_requests(errortype)
js2=made_requests(errormsg)
js3=made_requests(err[3])
get_urls(js1)
get_urls(js2)
get_urls(js3)
