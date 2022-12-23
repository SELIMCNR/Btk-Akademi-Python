#range rastgele sayı yazdırır
list = [1,2,3]

for item in range(2,20) :    #range rastgele sayı yazdırır.
    print(item)            #range(başlangıc,bitis,artırma)




#enumerate index ve value şekline dönderir.
#enumarete(index,value)'dir 
index = 0
gretting= "Hello there "
for letter in gretting:
    print(f"index : {index} letter: {gretting[index]}")
    index +=1
#
for index,item in enumerate(gretting):
    print(f'index: {index} letter: {item}') 

       
#zip birleştirme işlemi yapar key value olarak
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']



for item in zip(list1,list2):
    print(item)
    
# for ve while denk diğer döngü

for x in range(10):
    print(x)

numbers = [x for x in range(10)] 
print(numbers)

for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x%3==0] 
print(numbers)

myString = 'Hello'          
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList =[letter for letter in myString]
print(myList)

years = [1983,1999,2008,1956,1986]
ages = [2019 - year for year in years]
print(ages) 

results = [x if x%2 ==0 else 'Tek' for x in range(1,10)] 
print(results) 

#iki aynı sonucu dönen farklı örnekler
result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
        
numbers = [(x,y) for x in range(3) for y in range(3)] 
print(numbers)             
    
    
    