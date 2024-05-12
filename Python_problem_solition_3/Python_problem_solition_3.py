# 1 ocak 1901'den 31 aralık 2000'e kadar kaç sefer ayın ilk günü pazar olur?

from datetime import date,datetime,timedelta

pazar_sayısı=0
for yıl in range(1901,2001):
    for ay in range(1,13):
        if datetime(yıl,ay,1).weekday()==6:
            pazar_sayısı=pazar_sayısı+1
            
print(pazar_sayısı)
            

