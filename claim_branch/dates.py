from pprint import pprint
def date_aggregation(total_dict):
    total=36
    # pprint(total_dict)
    length=len(total_dict[0])
    d2=0
    d1=[]
    for each in total_dict[0]:
        # print(each)
        count_each=len(d1)
        Start_Page=total_dict[0][each]["start_page"]
        if count_each<len(total_dict[0])-2:
            End_Page=total_dict[0][each+1]["start_page"]-1
        else:
            pass
        # End_page=total
        # print(Start_Page,End_Page)
        Current_Date=total_dict[0][each]["date"]
        # print(Current_Date)
        if int(length) == int(each):
            d1.append({"start_page":Start_Page,"end_page":total,"date": Current_Date})
            # print(d1)
        else:
            d2+=1
            if d2>=2:
                if str(Current_Date) == str(d1[-1]['date']):
                    page = d1[-1]['start_page']
                    End_Page = total_dict[0][each + 1]["start_page"]-1
                    del (d1[-1])
                    d1.append({"start_page": page,"end_page": End_Page,"date": Current_Date})
                else:
                    End_page = total_dict[0][each+1]["start_page"]-1
                    d1.append({"start_page": Start_Page,"end_page": End_Page,"date": Current_Date})
            elif d2 == 1:
                d1.append({"start_page": Start_Page,"end_page": End_Page,"date": Current_Date})
    pprint(d1)

total_dict=[{1:{"start_page":1,"end_page":None,"date":"02/12/2014"},
             2:{"start_page":4,"end_page":None,"date":"03/12/2014"},
             3:{"start_page":12,"end_page":None,"date":"21/12/2015"},
             4:{"start_page":15,"end_page":None,"date":"21/12/2015"},
             5:{"start_page":20,"end_page":None,"date":"21/12/2017"},
             6:{"start_page":25,"end_page":None,"date":"25/11/2017"},
             7:{"start_page":28,"end_page":None,"date":"25/11/2017"}}]
date_aggregation(total_dict)