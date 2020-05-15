def problema1():
    import time
    import datetime  
    print("Dia y fecha: " , datetime.datetime.now())
    print("AÑO: ", datetime.date.today().strftime("%Y"))
    print("mes del año: ", datetime.date.today().strftime("%B"))
    print("dia del mes de año: ", datetime.date.today().strftime("%W"))
    print("mes del año: ", datetime.date.today().strftime("%w"))
    print("dia del año: ", datetime.date.today().strftime("%j"))
    print("dia del mes : ", datetime.date.today().strftime("%d"))
    print("dia del mes: ", datetime.date.today().strftime("%A"))


def problema2(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False

def problema3():
    from datetime import datetime
    date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
    print(date_object)
    
def problema4():
    import datetime
    print(datetime.datetime.now().time())

def problema5():
    from datetime import date, timedelta
    dt = date.today() - timedelta(5)
    print('Current Date :',date.today())
    print('5 days before Current Date :',dt)
    
def problema6():
    import datetime
    print(
        datetime.datetime.fromtimestamp(
            int("1284105682")
        ).strftime('%Y-%m-%d %H:%M:%S')
        )

def problema7():
    import datetime 
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)
    tomorrow = today + datetime.timedelta(days = 1) 
    print('Yesterday : ',yesterday)
    print('Today : ',today)
    print('Tomorrow : ',tomorrow)
    
def problema8():
    from datetime import date
    from datetime import datetime
    dt = date.today()
    print(datetime.combine(dt, datetime.min.time()))
    
def problema9():
    import datetime
    base = datetime.datetime.today()
    for x in range(0, 5):
        print(base + datetime.timedelta(days=x))
        
def problema10():
    import datetime
    x= datetime.datetime.now()
    y = x + datetime.timedelta(0,5)
    print(x.time())
    print(y.time())
    
def problema11():
    import datetime
    today = datetime.datetime.now()
    day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
    print(day_of_year)

def problema12():
    import time
    milli_sec = int(round(time.time() * 1000))
    print(milli_sec)

def problema13():
    import time
    milli_sec = int(round(time.time() * 1000))
    print(milli_sec)
    
def problema14():
    import time
    print(time.asctime(time.strptime('2015 50 1', '%Y %W %w')))
    
from datetime import date, timedelta

def problema15(year):
    dt = date(year, 1, 1)
    dt += timedelta(days = 6 - dt.weekday())  
    while dt.year == year:
        yield dt
        dt += timedelta(days = 7)
          
for s in problema15(2020):
    print(s)

import datetime
from datetime import date

def problema16(d, years):
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

def problema17():
    import datetime
    dt = datetime.datetime.today().replace(microsecond=0)
    print()
    print(dt)
    print()

def problema18():
    from datetime import date
    a = date(2000,2,28)
    b = date(2001,2,28)
    print(b-a)

def problema19():
    from datetime import date
    from datetime import timedelta
    today = date.today()
    offset = (today.weekday() - 1) % 7
    last_tuesday = today - timedelta(days=offset)
    print(last_tuesday)
    
from datetime import datetime 

def problema20(s):
    d = datetime.strptime(s, '%b %d, %Y')
    return d.weekday() == 1 and 14 < d.day < 22


#problema1()
#print(problema2(1900))
#print(problema2(2004))
#problema3()
#problema4()
#problema5()
#problema6()
#problema7()
#problema8()
#problema9()
#problema10()
#problema11()
#problema12()
#problema13()
#problema14()
#print(problema16(datetime.date(2015,1,1), -1))
#print(problema16(datetime.date(2015,1,1), 0))
#print(problema16(datetime.date(2015,1,1), 2))
#print(problema16(datetime.date(2000,2,29),1))
#problema17()
#problema18()
#problema19()
print(problema20('Jun 23, 2015')) #False
print(problema20('Jun 16, 2015')) #True 
print(problema20('Jul 21, 2015')) #False
