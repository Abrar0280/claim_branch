from elasticsearch import Elasticsearch
from datetime import timedelta
from datetime import datetime
import time
from pprint import pprint
import csv
es = Elasticsearch()
INDEX_NAME='csv_index'
list=[]
list1=[]
list2=[]
list3=[]
base=datetime.today()
no_of_days=1825
date_list = [base - timedelta(days=x) for x in range(0, no_of_days)]
# pprint(date_list)

with open("C:\\Users\\Mohamedabrar.A.WGS\\Desktop\\date_output.csv","w") as date_file:
    # writer = csv.writer(date_file, delimiter=' ',quotechar='', quoting=csv.QUOTE_MINIMAL)
    # for date in zip(list,list1,list2,list3):
    writer = csv.writer(date_file, delimiter=' ', quotechar=' ')
    # writer.writerow(["Format1","Format2","Format3","Format4"])

    for date in zip(list,list1,list2,list3):
        writer.writerow(date)
        # id_ref = 0
        # data_dict = {"Format1": date[0], "Format2": date[1], "Format3": date[2], "Format4": date[3]}
        # # print(data_dict)
        # print("creating '%s' index..." % (INDEX_NAME))
        # id_ref += 1
        # res = es.create(index=INDEX_NAME, doc_type="text", body=data_dict, id=id_ref)
        # print(" response: '%s'" % (res))
