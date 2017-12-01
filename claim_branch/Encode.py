import xml.etree.ElementTree as et
from pprint import pprint
from elasticsearch import Elasticsearch
import re
es = Elasticsearch()
import pyodbc
file_name=open("C:\\Users\\Mohamedabrar.A.WGS\\Desktop\\BCBSNE ACA 2017_75909321.xml")
data = file_name.read()
front={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
# front={a:0,b:1,c:2,d:3,e:4,f:5,g:6,h:7,i:8,j:9}
reverse={"0":"a","1":"b","2":"c","3":"d","4":"e","5":"f","6":"g","7":"h","8":"i","9":"j"}
# print(data)
id_ref=100
INDEX_NAME = "combine_index"
document = et.fromstring(data.encode('utf-8'))
all_pages = document.findall("Page")
# pprint(all_pages)
total_document = {}
list=[]
for pg in all_pages:
    page_number = pg.find("PageNumber")
    # pprint(page_number.text)
    zone = pg.find("Zone")
    # pprint(zone)
    zone_number = zone.find("ZoneNumber")
    # pprint(zone_number)
    lines = zone.findall("Line")
    # pprint(lines)
#     list = []
    for number in lines:
        num_text = number.find("LineNumber")
        # pprint(num_text.text)
        ocr_text = number.find("OCRCharacters")
        # pprint(ocr_text.text)
        # pprint(page_number.text)
        page_num=[c for c in page_number.text]
        # print(page_num)
        # print(page_num[1])


        if len(page_num) == 1:
            encode = "XXX" + str(reverse[page_num[0]])
            # print(encode)
        elif len(page_num) == 2:
            encode = "XX" + str(reverse[page_num[0]]) + str(reverse[page_num[1]])
            # print(encode)


        #ZONE ENCODE
        zone_num = [c for c in zone_number.text]
        # print(zone_num)

        # print(len(temp))
        if len(zone_num) == 1:
            zone_encode = str(reverse[zone_num[0]])
            # print(zone_encode)

        # LINE ENCODE
        line_num = [c for c in num_text.text]
        # print(line_num)

        if len(line_num) == 1:
            line_encode = "XX" + str(reverse[line_num[0]])
            # print(line_encode)
        elif len(line_num) == 2:
            line_encode = "X" + str(reverse[line_num[0]]) + str(reverse[line_num[1]])
            # print(line_encode)

        # CLUBING ALL TOGETHER


        # list.append(ocr_text.text)
        # list.append("||")
        # list.append(encode)
        # list.append(zone_encode)
        # list.append(line_encode)
        # join = ' '.join(list)
        # list1.append(join)
        # print(list1)
        join = ocr_text.text + "   " + "||"
        join1 = join + " " + encode
        join2 = join1 + " " + zone_encode
        join3 = join2 + " " + line_encode
        list.append(join3)
# pprint(list)

#CREATING INDEX
# a={"a":list}
# id_ref+=1
# print("creating '%s' index..." % (INDEX_NAME))
# res = es.create(index=INDEX_NAME, doc_type="text",body=a,id=id_ref)
# print(" response: '%s'" % (res))
# print(type(list))
for str in list:
    # print(str,"sssssssssssss")
    string=str.split("|| ")
    ocr, code= string[0],string[1]
    val=code.replace("X","")
    # print(val)
    value=val.split(" ")
    Page=value[0]
    Zone=value[1]
    Line=value[2]
    # print(page,zone,line)
    # page,zone,line=value
    # print(page)
    # print(Line)
    # exit()
# val1=list[0]
# print(type(val1))
# ocr=val1[0:4]
# val3=val1[9:]
# val4=val3.replace("X","")
# page= val4[0]
# print (type(page))
# zone= val4[2]
# line= val4[4]
# val2=list[12:]
# print(val2)
# print(val5)

    #PAGE DECODE
    if len(Page) == 1:
        page_decode = front[Page[0]]
        # print(page_decode)
    elif len(Page) == 2:
        page_decode = front[Page[0]] + front[Page[1]]
        # print(page_decode)

    #ZONE DECODE
    if len(Zone) == 1:
        # print(Zone[0],"dfgdfgdgfgf")
        zone_decode = front[Zone[0]]
        # print(zone_decode)

    #LINE DECODE
    if len(Line) == 1:
        line_decode = front[Line[0]]
        # print(line_decode)
    elif len(Line) == 2:
        line_decode = front[Line[0]] + front[Line[1]]
        # print(line_decode)
        # print(ocr,page_decode,zone_decode,line_decode)

        db = pyodbc.connect('DRIVER={SQL Server};SERVER=WGSWST003;DATABASE=ElasticSearch;UID=pycacviewer;PWD=Welcome2wave')
        cursor = db.cursor()
        cursor.execute("INSERT INTO claims_001 (ID,F_Name,L_Name,Page,Zone,Line) VALUES (?,?,?,?,?,?)", (ocr,page_decode,zone_decode,line_decode))
        db.commit()
