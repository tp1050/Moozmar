class doctor:
    def __init__(self,
                 firstname="",
                 lastname='',
                 nezam='',
                 address='',
                 phone='') -> None:
        self.firstname=firstname
        self.lastname=lastname
        self.nezam=nezam
        self.address=address
        self.phone=phone
        

dr={
    'firstname': '',
    'lastname': '',
    'fullname_en': '',
    'fullname_fa': '',
    'nezam': '',
    'specializations': [],
    'addresses': [],
    'phones': [],
    'urls':[]
}


from bs4 import BeautifulSoup as BS4 
from pathlib import Path
from Moozmar.lib.capitals import GSERP, MOBILE, P98, SPLIT,GMAP, VCF, WAME, iTME, iWAME
# html=Path('/home/c/Code/gh/Moozmar/sources/crawl/doctorto/assets/doctorto-10.html').read_text(encoding='utf-8')

# for i in range(1,31):
# with open(f"/home/c/Code/gh/Moozmar/sources/crawl/paziresh24/work/a.html", 'r',encoding="utf-8") as f:
#     html=f.read()

# soup=BS4(html,features="lxml",from_encoding="utf-8")
# script=(soup.find_all('script')[-1]).text
import json
# script=json.loads(script)
# script=script['props']['pageProps']['dehydratedState']['queries']['results']
# Path('data.json').write_text(json.dumps(script,ensure_ascii=False))
with open('work/a.json') as p:
    script=json.load(p)
script=script['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['search']['result']
Path('data.json').write_text(json.dumps(script,ensure_ascii=False))
Path('0.json').write_text(json.dumps(script[0],ensure_ascii=False))

for doc in script:
    dr={
    "name":{
        "prefix":"",
        "firstname":"",
        "lastname":"",
        "suffix":"",
        "fullname_en":"",
        "fullname_fa":"",
        },
    "nezam":"",
    "specializations":[],
    "addresses":[
        {
            "address":"",
            "city":"",
            "state":"",
            "fulladdress":"",
            "country":"",
            "latitude":0,
            "longitude":0,
            },
        ],
    "phones":[],
    "urls":[],
    "img":[]
    
}


    empty_coordinates={'latitude':0,'longitude':0}
    dr['name']['prefix']=doc['prefix']
    dr['name']['fullname_fa']=doc['display_name']

    dr['specializations']=doc['display_expertise'].split(',')
    dr['specializations'].append('moozi')
    dr['addresses'].pop()
    for address in doc['centers']:
        if not address['display_number']: continue
        dr['addresses'].append(
            {"address":address['address'],
             "city":address['city_name'],
             "state":address['province_name'],
             "latitude":address['map']['lat'],
             "longitude":address['map']['lon']
             
             })
        
        dr['phones'].extend(["021"+p for p in SPLIT(address['display_number'])])
        dr['urls'].append(GMAP(latitude=address['map']['lat'],longitude=address['map']['lon']))
    dr['gender']=doc['gender']
    dr['nezam']=doc['medical_code']
    dr['img']=["https://paziresh24.com"+doc['image'].replace('?size=150','')]
    dr['urls'].extend(iWAME(" ".join(dr['phones'])))
    dr['urls'].extend(iTME(" ".join(dr['phones'])))
    dr['urls'].append(f"https://www.paziresh24.com/dr/{doc['slug']}")
    dr['urls'].append(GSERP("\""+dr['name']['fullname_fa']+"\""))  
    dr['urls'].append(GSERP("\"نظام پزشکی "+dr['nezam']+"\"")) 

    _temp=[]
    for p in dr['phones']:
        if MOBILE(p):_temp.append(P98(p))
        else: _temp.append(p)
    dr['phones']=_temp
    dr['urls'].append(dr['img'][0] ) 
    if len( dr['phones'])>0:
        with open(''+dr['name']['fullname_fa']+'a.json', 'w',encoding="utf-8") as f:
            json.dump(dr, f,ensure_ascii=False)
        with open(''+dr['name']['fullname_fa']+'a.vcf', 'w',encoding="utf-8") as f:
            f.write(VCF(j=dr)+"\n")


# script=script['pr']





from pprint import pprint
pprint(script)
