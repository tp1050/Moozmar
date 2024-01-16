from copy import copy


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
            "country":""
            },
        ],
    "phones":[],
    "urls":[],
    "images":[]
    
}


# class PersianDoctor:
#     def __init__(self,prefix="دکتر"
#                  firstname="",
#                  lastname='',
#                  nezam='',
#                  addresses=None,
#                  phones=None,
#                  id_index=0,
#                  **v)
#         self.dr=dr.copy()
#         self.dr['firstname']=firstname
#         self.dr['lastname']=lastname
#         self.dr['nezam']=nezam
#         self.dr['index']=id_index
#         self.dr['addresses']=address or []
#         self.dr['phone']=phone

# class Name:
#     def __init__(self,
#                  prefix="",
#                  firstname="",
#                  lastname='',
#                  suffix='',
#                  id_index=0
#                  ,**v) -> None:
#         self.firstname=firstname
#         self.lastname=lastname
#         self.suffix=suffix
#         self.prefix=prefix
#         self.index=id_index
 



# class Person:
#     def __init__(self,
#                  firstname="",
#                  lastname='',
#                  nezam='',
#                  address='',
#                  phone='',
#                  id_index=0,
#                  **v) -> None:
#         self.firstname=firstname
#         self.lastname=lastname
#         self.nezam=nezam
#         self.addresses=address or []
#         self.phone=phone
#         self.index=id_index



