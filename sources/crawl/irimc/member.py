# preamble:{
#     Example URL: https://membersearch.irimc.org/member/profile?id=af601d95-5a2d-4c92-8792-e8a01440655f
#     main location:
#         <div class="row clearfix">
#         </div>
#     name & specialization & nezam:
#         <div class="u_name">
#             <h1>
#                 <strong>دکتر همایون آرام</strong>
#             </h1>
#             <h5>تخصص بیماری‌های پوست (درماتولوژی)</h5>
#             <span class="mcCode">شماره نظام پزشکی: 9213</span>
#         </div>       
#     addresses:
#             <table class="table m-b-0 table-hover">
#                 <thead>
#                     <tr>
#                         <th>نوع</th>
#                         <th>آدرس</th>
#                         <th>کد پستی</th>
#                         <th>تلفن</th>
#                         <th></th>
#                         <th>تصویر تابلو</th>
#                     </tr>
#                 </thead>
#                 <tbody>
#                         <tr>
#                             <td>
#                                 <span class="badge badge-success">مطب</span>
#                             </td>
#                             <td class="project-title">
#                                 <h6>تهران</h6>
#                                 <small>خ ایران نوین- م ایران نوین- ک کامران- پ9</small>
#                             </td>
#                             <td>
#                                 <h6></h6>
#                             </td>
#                             <td>
#                                 <h6></h6>
#                                 <small></small>
#                             </td>
#                             <td class="project-actio                                                   </td>
#                             <td class="text-center">
#                             <span>---</span>
#                             </td>
#                         </tr>

#                 </tbody>
#             </table>

    
# }




html="""
    <div class="row clearfix">
    </div>
   
        <div class="u_name">
            <h1>
                <strong>دکتر همایون آرام</strong>
            </h1>
            <h5>تخصص بیماری‌های پوست (درماتولوژی)</h5>
            <span class="mcCode">شماره نظام پزشکی: 9213</span>
        </div>       
    
            <table class="table m-b-0 table-hover">
                <thead>
                    <tr>
                        <th>نوع</th>
                        <th>آدرس</th>
                        <th>کد پستی</th>
                        <th>تلفن</th>
                        <th></th>
                        <th>تصویر تابلو</th>
                    </tr>
                </thead>
                <tbody>
                        <tr>
                            <td>
                                <span class="badge badge-success">مطب</span>
                            </td>
                            <td class="project-title">
                                <h6>تهران</h6>
                                <small>خ ایران نوین- م ایران نوین- ک کامران- پ9</small>
                            </td>
                            <td>
                                <h6></h6>
                            </td>
                            <td>
                                <h6></h6>
                                <small></small>
                            </td>
                            <td class="project-actio                                                   </td>
                            <td class="text-center">
                            <span>---</span>
                            </td>
                        </tr>

                </tbody>
            </table>
            
    
    </div>




"""

dr={
    'title':'دکتر',
    'firstname': '',
    'lastname': '',
    'nezam': '',
    'specializations': '',
    'img':[],
    'addresses': [],
    'phones': [],
}
from bs4 import BeautifulSoup as BS4 
from pathlib import Path
from Moozmar.lib.capitals import SPLIT
html=Path('assets/2.html').read_text()


soup=BS4(html,features="lxml")
tds=soup.find_all('td')

details=soup.select_one(selector='.u_name').text
if details:
    name, specialization, nezam=details.strip().split('\n')
    name=name.replace('دکتر','').strip()
    dr['firstname']=name
    nezam=nezam.split(':')[1].strip()
    dr['nezam']=nezam
    
details2=soup.select_one("table.m-b-0.table-hover").tbody.find_all('tr')
if details:
    for tr in details2:
        tds=tr.find_all('td')
        # specialization=tds[1].h6.text.strip()
        city=tds[1].small.text.strip()
        address=tds[1].h6.text.strip()
        dr['addresses'].append((city,address))
        phone=SPLIT(tds[3].h6.text.strip(),'-')
        dr['phones'].extend(phone)
        # print(name,'\n', specialization,'\n', nezam, '\n',address,'\n', phone ,'\n', city)

# tds=details2.find_all('td')
dr['specializations']=soup.select_one("body > section:nth-child(5) > div > div > div:nth-child(2) > div.col-sm-12.col-md-12.col-lg-4 > div:nth-child(1) > div > div > div.col-12.col-xl-8 > h4").text.strip()
dr['img']="https://membersearch.irimc.org"+soup.body.select_one(".user_pic.rounded.img-raised")['src']
from pprint import pprint
pprint(dr)
