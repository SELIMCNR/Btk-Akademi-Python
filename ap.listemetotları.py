numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

#max min 
val = min(numbers) #minumum değer gelir
val = max(numbers) #maximum değeri gelir

val = max(letters) 
val = min(letters)
#dilimleme
val = numbers[3:6] #[başla:bitiş:artış]
val = numbers[:3]
val = numbers[4:]
#ekleme
numbers[4] = 40
numbers.append(49) # append=ekle
numbers.append(59)
numbers.insert(3,78) #3.indise ekle 
numbers.insert(-1,52) #sona ekle
#silme
numbers.pop() #siler
numbers.pop(-1)

numbers.remove(59)
#sıralama
numbers.sort() #sıralar
letters.sort()
letters.reverse() # tersten sıralar

print(numbers)
#len uzunluğunu söyler
print(len(numbers))  #numbers değişkeninin uzunluğu ne 
print(len(letters))
#kaçıncı sırada
print(numbers.count(10)) #numbers 10 nolu değişken nerede 
print(letters.count('a'))

numbers.clear() # tüm listeyi siler
