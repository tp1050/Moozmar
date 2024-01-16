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

for i in range(1,31):
  with open(f"/home/c/Code/gh/Moozmar/sources/crawl/doctorto/assets/work/doctorto-{i}.html", 'r',encoding="utf-8") as f:
    html=f.read()
  
  soup=BS4(html,features="lxml",from_encoding="utf-8")
  script=(soup.find_all('script')[-1]).text
  import json
  script=json.loads(script)
  script=script['props']['pageProps']['dehydratedState']['queries'][3]['state']['data']['data']
  Path('data.json').write_text(json.dumps(script,ensure_ascii=False))
  for doc in script:
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
    empty_coordinates={'latitude':0,'longitude':0}
    dr['fullname_en']=doc['slug']
    dr['fullname_fa']=doc['fullName']
    dr['nezam']=doc['medicalNumber']
    dr['specializations']=[s['fullName'] for s in doc['specialities']]
    dr['img']=doc['avatar']
    for address in doc['consultations']:
      if not address['place']: continue
      # print(address.keys())
      dr['addresses'].append(address['place']['address'])
      dr['city']=address['place']['city']['name']
      dr['phones'].extend(address['place']['phone'] or [])
      
      ##URLS:
      #gmap
      #
      #wa.me for whatsapp
      dr['urls'].append(GMAP(**(address['place']['coordinates'] or empty_coordinates)))
    
    dr['urls'].extend(iWAME(" ".join(dr['phones'])))
    dr['urls'].extend(iTME(" ".join(dr['phones'])))
    dr['urls'].append(f"https://doctoreto.com/doctor/{doc['slug']}/{doc['id']}")
    dr['urls'].append(GSERP("\""+dr['fullname_fa']+"\""))  
    dr['urls'].append(GSERP("\"\"نظام پزشکی "+"\""+dr['nezam']+"\"")) 
    
    _temp=[]
    for p in dr['phones']:
      if MOBILE(p):_temp.append(P98(p))
      else: _temp.append(p)
    dr['phones']=_temp
    dr['urls'].append(dr['img'] ) 
        
    with open('assets/done/'+dr['fullname_en']+'a.json', 'w',encoding="utf-8") as f:
      json.dump(dr, f,ensure_ascii=False)
    with open('assets/done/'+dr['fullname_en']+'a.vcf', 'w',encoding="utf-8") as f:
      f.write(VCF(j=dr))
  

# script=script['pr']





from pprint import pprint
pprint(script)
