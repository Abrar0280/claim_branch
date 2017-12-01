from pprint import pprint
def date_func(my_dict):
    # print(my_dict,"fdsds")
    all_date=[]
    count = 0
    for k,v in my_dict.items():
        if int(k.split('/')[-1]) < 2000:
            all_date.append(str(k))
        #     count = count + 1
        # pprint(type(all_date))
    final_dates=set(all_date)
    print(final_dates)
    # for each_dates in all_date:

    if len(final_dates) >=2:
        print('mixed')
    else:
        print('single')

my_dict = {'01/20/2016': [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6],
'06/20/1942': [1, 5],
'06/20/1945': [1, 2],
'06/20/1941': [1, 5, 4, 5]}
date_func(my_dict)