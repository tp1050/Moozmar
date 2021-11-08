from Javab import *
from anbar import getAnbar, exec, mySQLize
from Address import *
from noche import execSysCmd, sexyError, berin
from netnoche import getHTML
import json

def getLatestPrice():
    keys={}
    try:
        dirty=getHTML("https://api.accessban.com/v1/widget")
     ## clean up 2cp coding
        aa=dirty.splitlines()[0].encode('latin1', 'backslashreplace').decode('unicode-escape').replace("var tgju_data = ","")[:-1]
        jjj=json.loads(aa)
        for k in jjj:
            keys[k]=jjj[k]['p']



    except e:
        sexyError(e)
    print(keys)



def main():
    getLatestPrice()

if __name__== '__main__':
    main()
