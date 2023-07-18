import datetime as dt

list_date_str = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
list_revenue = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]

list_date = []
for i in list_date_str:
    date = dt.datetime.strptime(i, '%Y-%m-%d')
    list_date.append(int(date.month))

list1 = zip(list_date, list_revenue)
rev_november = [x[1] for x in list1 if x[0] == 11]
sum = 0 
for i in rev_november:
    sum += i

def rev_to_month(key:list, value:list):
    rev = zip(key, value)
    print(key)
    for i in rev:
        for j in key:              
            if i[0] == j:
                print(i, j)
            

rev_to_month(list_date, list_revenue)