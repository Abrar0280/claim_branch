from elasticsearch import Elasticsearch
from datetime import timedelta
from datetime import datetime
import time
from pprint import pprint
import csv
es = Elasticsearch()
INDEX_NAME='cssss'
list=[]
list1=[]
list2=[]
list3=[]
base=datetime.today()
no_of_days=1826
date_list = [base - timedelta(days=x) for x in range(0, no_of_days)]
# pprint(date_list)
for date in date_list:
    # print(date)
    dat = date.strftime("%d-%m-%Y")
    list.append(dat)
    dat1 = date.strftime("%m-%d-%Y")
    list1.append(dat1)
    dat2 = date.strftime("%d-%b-%Y")
    list2.append(dat2)
    dat2 = date.strftime("%d-%B-%Y")
    list3.append(dat2)
    # print(type(dat2))
    with open("C:\\Users\\Mohamedabrar.A.WGS\\Desktop\\date_output.csv","w") as date_file:
        # writer = csv.writer(date_file, delimiter=' ',quotechar='', quoting=csv.QUOTE_MINIMAL)
        # for date in zip(list,list1,list2,list3):
        writer = csv.writer(date_file, delimiter=' ', quotechar=' ')
        writer.writerow(("Format1","Format2","Format3","Format4"))
        for date in zip(list,list1,list2,list3):
            writer.writerow(date)
            # print(date)
id_ref = 0
data_dict = {"a":list,"b":list1,"c":list2,"d":list3}
            # # print(data_dict)
print("creating '%s' index..." % (INDEX_NAME))
id_ref += 1
res = es.create(index=INDEX_NAME, doc_type="text", body=data_dict, id=id_ref)
print(" response: '%s'" % (res))
