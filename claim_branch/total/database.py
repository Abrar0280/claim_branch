import xml.etree.ElementTree as et
from pprint import pprint
import glob
from elasticsearch import Elasticsearch
from datetime import timedelta
import datefinder
import pyodbc
import re
es = Elasticsearch()
# file_name="C:\\Users\\Mohamedabrar.A.WGS\\Desktop\\XML FIles/**/*.xml"
# id_ref = 1000
# dates=[]
# for xml in glob.iglob(file_name, recursive=True):
#     # print(xml)
#     xml_file=open(xml)
#     # print(xml_file)
INDEX_NAME = 'date_highlights'
#     data = xml_file.read()
#     # print(data)
#
#     document = et.fromstring(data.encode('utf-8'))
#     # pprint(document)
#     all_pages = document.findall("Page")
#     # pprint(all_pages)
#
#     total_document = {}
#     list = []
#
#     for pg in all_pages:
#         page_number = pg.find("PageNumber")
#         # pprint(page_number.text)
#
#         zone = pg.find("Zone")
#         # pprint(zone)
#
#         lines = zone.findall("Line")
#         # pprint(lines)
#
#         for number in lines:
#             num_text = number.find("LineNumber")
#             # pprint(num_text.text)
#             ocr_text = number.find("OCRCharacters")
#             # pprint(ocr_text.text)
#
#             list.append(ocr_text.text)
#     # pprint(list)
#
#     #Creating
#     a={"a":list}
#     print("creating '%s' index..." % (INDEX_NAME))
#     id_ref+= 1
#     res = es.create(index=INDEX_NAME, doc_type="text", body=a,id=id_ref)
#     print(" response: '%s'" % (res))
#     string=str(a)
#     dates.append(a)
#     match=datefinder.find_dates(text=string, index=res)
#     for mat in match:
#         print(mat)

from datetime import datetime
base=datetime.today()
no_of_days=1000
date_list = [base - timedelta(days=x) for x in range(0, no_of_days)]
# print(date_list)
for date in date_list:
    # print(date)
    dat = date.strftime("%d/%m/%Y")
    # print(dat)

    body = {
        "query":{
            "match_phrase": {
                "a": dat
            }
    },
    "highlight": {
        "fields": {
            "a": {"number_of_fragments": 0,
                        "fragment_size": 0,
                        "type": "plain"
                        }
            }
        }
    }
    res = es.search(index=INDEX_NAME, body=body)
    print("Got %d Hits:" % res['hits']['total'])

    for hit in res['hits']['hits']:
        # pprint(hit)
        Id = hit['_id']
        data_input = hit['highlight']['a'][0:]
        pprint(hit['highlight']['a'][0])
        response = re.findall(r'<em>(.*?<em>.*?<em>.*?)</em>', str(data_input))
        # print(response,Id)
        db = pyodbc.connect('DRIVER={SQL Server};SERVER=WGSWST003;DATABASE=ElasticSearch;UID=pycacviewer;PWD=Welcome2wave')
        cursor = db.cursor()
        for each in response:
            each=each.replace('<em>','').replace('</em>','')
            # cursor.execute("INSERT INTO date_in (ID_NO,RESPONSE) VALUES (?,?)", (Id, each))
            cursor.execute("Declare @outpu nvarchar(200) Exec dum 1003,@outpu output select @outpu from date_in")
            val = cursor.fetchall()
            # print(val)
            for each_value in val:
                print(each_value)
        # db.commit()