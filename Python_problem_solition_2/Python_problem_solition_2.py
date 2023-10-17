#problem: 4 milyondan küçük fibonacci sayılarından çift olanları toplayan program

fibonacci= list()
fibonacci.append(1)
fibonacci.append(2)

i=2
while True:
     if fibonacci[i-2]+ fibonacci[i-1] < 400000:
        fibonacci.append(fibonacci[i-2]+ fibonacci[i-1])
        i+=1
     else:
         break 
sum=0
for i in fibonacci:
    if i% 2==0:
        
        sum+=i
print(sum)
print(len(fibonacci))


# 2. çözüm yolu:

a=1
b=2

sum=2
while True:
    c=a+b
    
    a=b
    b=c
    if  c%2==0:
        sum +=c
    if c>4000000:
        break
print(sum)    
    






























