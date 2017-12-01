import xml.etree.ElementTree as et
from pprint import pprint
import glob
from elasticsearch import Elasticsearch
from datetime import timedelta
from datetime import datetime
import pyodbc
import time
import re
import os
import shutil
es = Elasticsearch()
import threading
def thread():
    # threading.Timer(300.0, thread).start()
    # file_name = "C:\\Users\\Mohamedabrar.A.WGS\\Desktop\\XML/**/*.xml"£
    id_ref = 1000
    INDEX_NAME = 'xml_traversess'
    file = r"C:\Users\Mohamedabrar.A.WGS\Desktop\des/**/*.xml"
    source = r"C:\Users\Mohamedabrar.A.WGS\Desktop\des"
    Destination = r"C:\Users\Mohamedabrar.A.WGS\Desktop\src"
    for xml in glob.iglob(file, recursive=True):
        # print(xml)
        print(file)
        exit()
        xml_file=open(xml)
        # print(xml_file)
        data = xml_file.read()
        xml_file.close()
        # print(data)
        document = et.fromstring(data.encode('utf-8'))
        # pprint(document)
        all_pages = document.findall("Page")
        # pprint(all_pages)
        list = []
        for pg in all_pages:
            page_number = pg.find("PageNumber")
            # pprint(page_number.text)
            zone = pg.find("Zone")
            # pprint(zone)
            lines = zone.findall("Line")
            # pprint(lines)
            for number in lines:
                num_text = number.find("LineNumber")
                # pprint(num_text.text)
                ocr_text = number.find("OCRCharacters")
                # pprint(ocr_text.text)
                list.append(ocr_text.text)
        # pprint(list)
    #     #Creating
    #     a={"a":list}
    #     print("creating '%s' index..." % (INDEX_NAME))
    #     id_ref+= 1
    #     res = es.create(index=INDEX_NAME, doc_type="text", body=a,id=id_ref)
    #     print(" response: '%s'" % (res))

        print("gdfgg",xml)
        try:
            os.remove(xml)
        except:
            pass
        shutil.move(xml, Destination)
        print("dgfgdfgdf")
    # base=datetime.today()
    # no_of_days=1000
    # date_list = [base - timedelta(days=x) for x in range(0, no_of_days)]
    # # print(date_list)
    # for date in date_list:
    #     # print(date)
    #     dat = date.strftime("%m/%d/%Y")
    #     # print(dat)
    #     body = {
    #             "query":{
    #                 "match_phrase": {
    #                     "a": dat
    #                 }
    #         },
    #         "highlight": {
    #             "fields": {
    #                 "a": {"number_of_fragments": 0,
    #                             "fragment_size": 0,
    #                             "type": "plain"
    #                             }
    #                 }
    #             }
    #         }
    #     res = es.search(index=INDEX_NAME, body=body)
    #     # print("Got %d Hits:" % res['hits']['total'])
    #     for hit in res['hits']['hits']:
    #         # pprint(hit)
    #         Id = hit['_id']
    #         data_input = hit['highlight']['a'][0:]
    #         pprint(hit['highlight']['a'][0])
    #
    #         response = re.findall(r'<em>(.*?<em>.*?<em>.*?)</em>', str(data_input))
    #         # print(response,Id)
    #         db = pyodbc.connect('DRIVER={SQL Server};SERVER=WGSWST003;DATABASE=ElasticSearch;UID=pycacviewer;PWD=Welcome2wave')
    #         cursor = db.cursor()
    #         # # print(Id)
    #         # # print(resp)
    #         for each in response:
    #             each = each.replace('<em>', '').replace('</em>', '')
    #             cursor.execute("INSERT INTO Date_agg (ID_VALUE,Date) VALUES (?,?)", (Id, each))
    #         db.commit()

# if __name__ == "__main__":
thread()