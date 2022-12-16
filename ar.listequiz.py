names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]


names=names.append('Cenk') #liste sonuna eklendi

names=names.insert(0,'Sena') #liste başına eklendi
names=names.insert(-1,'mehmet')
names=names.insert(len(names),'Mehmet')

names = names.remove('Deniz') #yazılı isim silindi
names=names.pop() #silme yapıldı
names=names.pop(1)

index=names.index('Deniz') #index al 
names.pop(index)  #indexe göre sil

result = 'Ali' in names # names içinde ali varmı
result2= names.index('Ali')

print(result)

names=names.reverse() # liste elemanlarını ters çevir

names=names.sort() #sıralam işlemi yapar

str= "Chevrolet,Dacia"
listeyeçevirme= str.split(',') #listeye çevirdi

minumum=min(years)
maximum=max(years)
print(minumum,maximum)

kaçtane=years.count(1998) #kaçtane 1998 değeri var

years=years.clear() # tüm elemanları siler

markalar= [] 
marka= input("marka: ") # dışardan değer alma
markalar.append(marka)
print(markalar)


