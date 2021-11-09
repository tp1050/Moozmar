from Price import *

class bonbastPrice(Price):
    def __init__(self,value=0,vaght=datetime.now(),jens='dool',conn='No'):
        self.refCurID=49
        self.refCur='fx_irr'
        self.src='bonbast'
        self.vaght=vaght
        self.value=value
        self.jens=jens



