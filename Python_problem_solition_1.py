
# 3'e veya 5'e bölünebilen 1000'den küçük sayıları topla
def check(x): #x denemek istediğimiz sayı
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False

sum=0

for i in range(1,1000):
    if check(i)==True: #if check(i)==True demektir aslında
        sum *= i
        
print(sum)

