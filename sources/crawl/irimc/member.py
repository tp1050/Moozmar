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


from bs4 import BeautifulSoup as BS4 
from pathlib import Path
html=Path('assets/2.html').read_text()

soup=BS4(html,features="lxml")
tds=soup.find_all('td')

details=soup.select_one(selector='.u_name').text
if details:
    name, specialization, nezam=details.strip().split('\n')
    name=name.replace('دکتر','').strip()
    city=tds[5].h6.text.strip()
    address=tds[5].small.text.strip()
    phone=tds[7].h6.text.strip()
    nezam=nezam.split(':')[1].strip()
    
details2=soup.select_one("table.m-b-0.table-hover").tbody.find_all('tr')
# tds=details2.find_all('td')


print(name,'\n', specialization,'\n', nezam, '\n',address,'\n', phone ,'\n', city)
