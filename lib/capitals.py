

def SPLIT(s,sep=' ',remove=None):
    if remove:
        return [x for x in s.split(sep) if not x==remove]
    else:
        return [x for x in s.split(sep) if x]
def iSPLIT(s,sep=' ',remove=None):
    if not isinstance(sep,list):sep=[sep]
    ret=SPLIT(s,sep=sep.pop(),remove=remove)
    
    for sp in sep:
        ret.extend()
        
        
    _ret=[]
    if isinstance(s,str) and isinstance(sep,str):
        _ret.extend(SPLIT(s,sep=sep,remove=remove))
    if isinstance(s,list):
        _work=[]
    for sp in sep:
        _work.extend(SPLIT(s,sep=sp,remove=remove))
        
def GMAP(latitude=None,longitude=None):
    import urllib.parse
    base_url = "https://www.google.com/maps/search/?api=1"
    params = {
            'query': f'{latitude},{longitude}' 
            }
    url_params = urllib.parse.urlencode(params)
    return f"{base_url}&{url_params}"
def OSM(latitude=None,longitude=None):
    import urllib.parse
    base_url = "https://www.openstreetmap.org/?mlat={}&mlon={}&zoom=18#map=18/{}/{}"
    return base_url.format(latitude,longitude,latitude,longitude)
    

def WAME(mobile):
    import urllib.parse
    base_url = f"https://wa.me/{P98( mobile)}"
    return base_url


def GSERP(q):
    import urllib.parse
    import random
    base_url = "https://www.google.com/search"
    params = {
        'q': q,
        'oq': q,
        'aqs': 'chrome..69i57.1673j0j1',
        'sourceid': 'chrome',
        'ie': 'UTF-8'
    }

    letters = 'abcdefghijklmnopqrstuvwxyz'
    params['client'] = ''.join(random.sample(letters, 8))

    url_params = urllib.parse.urlencode(params)
    return f"{base_url}?{url_params}"



def MOBILE(text):
    import re
    pattern = r"\b09[19034]\d{8}\b"
    matches = re.findall(pattern, text)
    return matches

def P98(mobile):
    return "+98"+(MOBILE(mobile)[0])[1:]
def iWAME(text):
   return [WAME(m) for m in MOBILE(text)]
def TME(phone):
    return f"https://t.me/{P98(phone)}"
def iTME(phone):
    return [TME(p) for p in MOBILE(phone)]

def VCF(s=None,j=None,k=None,l=None):
    if j:
        VCF_TEMPLATE='''
        {_BEGIN}
        {_CONACTNAME}
        {_NAME}
        {_TELL}
        {_ADDR}
        {_INSTAGRAM}
        {_NOTE}
        {_CATEGORIES}
        {_ORG}
        {_TITLE}
        {_END}
        '''
        _BEGIN="BEGIN:VCARD\nVERSION:3.0\n".strip()
        _CONTACTNAME=f"FN:{j['name']['fullname_fa']}"
        _CONTACTNAME=_CONTACTNAME+f"\nN:{j['name']['lastname']};{j['name']['firstname']};;{j['name']['prefix']}"
        _TELL=''
        for t in j['phones']:
            _TELL=_TELL+f"\nTEL;TYPE=main:{t}"
        _ADDR=''
        for a in j['addresses']:
            _ADDR=_ADDR+f"\nADR: ; {a['city']};{a['address']};{a['state']};IR;"
        _URL=''
        for u in j['urls']:
            _URL=_URL+f"\nURL:{u}"
        _=','.join(j['specializations'])
        _CATEGOURIES=f"\nCATEGORIES:{_}"
        _PHOTO=f"PHOTO;TYPE=PNG;VALUE=URI:{j['img'][0]}"
        _PHOTO=f"PHOTO:{j['img'][0]}"
        _NOTE=f"NOTE:Nezam:{j['nezam']}"
        _END="END:VCARD"
        ret= _BEGIN+"\n"+_CONTACTNAME+"\n"+_TELL+"\n"+_ADDR+"\n"+_URL+"\n"+_CATEGOURIES+"\n"+_PHOTO+"\n"+_NOTE+"\n"+_END+"\n"
        return ret

                