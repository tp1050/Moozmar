from Javab import *
from Price import *
from anbar import getAnbar, exec, mySQLize,getSymID,getDicID,begir,bezar
from Address import *
from noche import execSysCmd, sexyError, berin,ffloat
from netnoche import getHTML
import json
from DegbanStatic import *


class TGJuPrice(Price):
    def __init__(self, value, jens,jensID=0,conn='NO',vaght=datetime.now()):
        self.dic= {'com_gold_18_ct_gram': ('fx_irr',49), 'com_gold_24_ct_gram': ('fx_irr',49), 'com_gold_mesghal': ('fx_irr',49),
           'com_irgc': ('fx_irr',49), 'com_irgc_emami': ('fx_irr',49), 'com_irgc_gram': ('fx_irr',49), 'com_irgc_half': ('fx_irr',49),
           'com_irgc_quarter': ('fx_irr',49), 'com_gold_ounce': ('fx_usd',17), 'com_oil': ('fx_usd',17), 'com_oil_brent': ('fx_usd',17),
           'com_oil_opec': ('fx_usd',17), 'com_palladium': ('fx_usd',17), 'com_platinum': ('fx_usd',17), 'com_silver':('fx_usd',17),'fx_usd':('fx_irr',49),'fx_eur':('fx_irr',49),'fx_gbp':('fx_irr',49),'fx_aed':('fx_irr',49),'fx_jpy':('fx_irr',49)}
        self.vaght = vaght
        self.value = value
        self.src = 'tgju'
        self.exact = 1
        self.jens = jens
        self.refCurrency,self.refCurID = self.dic[jens]
        self.dic=''
        self.conn = conn
        if self.conn == 'NO':
            conn = getAnbar(base0LAN)
        self.jensID = jensID
        if jensID == 0:
            self.jensID = getSymID(self.jens, conn)
    def setJensID():
            setJensID(getSymID(self.jens,conn))
    def setJensID(jensID):
            self.jensID = jensID
    def getDic(self):
            return vars(self)
    def sabt(self):
            bezar('price','absVal,jensID,refCurID,timestamp','{},{},{},"{}"'.format(self.value,self.jensID,self.refCurID,self.vaght),self.conn)

def getLatestPrice():
    prices={}
    try:
        dirty=getHTML("https://api.accessban.com/v1/widget")
        vaght=datetime.now()
        ## clean up 2cp coding
        jjj=json.loads(dirty.splitlines()[0].encode('latin1', 'backslashreplace').decode('unicode-escape').replace("var tgju_data = ","")[:-1])
        for jens in jjj:
            prices[jens]=ffloat(jjj[jens]['p'])
    except Exception as e:
        sexyError(e)
    conn=getAnbar(base0LAN)
    priceArray=[]
    for p in prices:
        id,eq=getDicID(p, conn)
        try:
            priceArray.append(TGJuPrice(value=prices[p],jens=eq,conn=conn))
        except Exception as e:
            sexyError(e)
    return priceArray



def main():
    p=getLatestPrice()
    for pp in p:
        print(pp.getDic())
        pp.sabt()


if __name__== '__main__':
    main()
