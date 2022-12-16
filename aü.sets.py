fruits = {'orange','apple','banana'}

#print(fruits[0])  setler indekslenemez

for x in fruits : 
    print(x)
    
fruits.add('cherry')
fruits.update(['mango','grape','apple'])

print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList)) # tekrarlanan elemanlar set oldundan silinir.

#silme
fruits.remove('mango')
fruits.discard('apple')
fruits.pop() #herhangi bir elemanı siler
fruits.clear() # bütün elemanlar


