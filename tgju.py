from Javab import *
from anbar import getAnbar, exec, mySQLize
from Address import *
from noche import berin
from noche import execSysCmd
from netnoche import getHTML
import json

def getLatestPrice():
    dirty=getHTML("https://api.accessban.com/v1/widget")
    ## clean up 2cp coding
    aa=dirty.splitlines()[0].encode('latin1', 'backslashreplace').decode('unicode-escape').replace("var tgju_data = ","")
    berin(1)
    print(aa[:-1])
    jjj=json.loads(aa)
    print(jjj)


def main():
    getLatestPrice()

if __name__== '__main__':
    main()
#
# for key in jjj:
#     jaj=jjj[key]
#     price=jaj['p']
#     print(key, '  ', price)
# #print(a)