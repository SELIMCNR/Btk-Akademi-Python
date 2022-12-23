numbers = [1,2,3,4,5]

for num in numbers:
    print('Hello')
  #listelerde for  
names = ["cinar","selim","sadık"]

for name in names:
    print(f'my name is {name}')    
    
 #stringde for  
name1 = "Selim Çınar"
for n in name1:
    print(n)

 #tuplerda for  
tuple =[(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(a,b)    
    
 #sözlüklerde for   
d= {'k1': 1 , 'k2': 2, 'k3':3}

for key,value in d.items():
    print(key,value)    
    
#Uygulamalar
#3 ün katı olan sayılar
sayilar = [1,3,5,7,9,12,19,21]
for s in sayilar:
    if s%3==0:
        print(sayilar)
        


#sayıların toplamı    
toplam =0
for s in sayilar:
    toplam+=s         
print(toplam)    

#sayilarin karesi
for s in sayilar:
    if(s%2==1):
        print=s*s
       

sehirler = ["koceli","İstanbul","Ankara","İzmir","Rize"]
# en fazla 5 karakterli olanlar
for s in sehirler:
    if len(s) <=5 :
        print(s) 


urunler = [
    {'name':'samsung s6','price':'3000'},
     {'name':'samsung s7','price':'4000'},
      {'name':'samsung s8','price':'5000'},
       {'name':'samsung s9','price':'6000'},
        {'name':'samsung s10','price':'7000'}
]

# ürünlerin fiyaları toplamı ? 
toplam =0 
for urun in urunler:
    fiyat = int (urun['price'])
    toplam+=fiyat
print(toplam)    
    
# En fazla fiyatı 5000 olan ürünler
for urun in urunler:
    if(int(urun['fiyat'])<5000):
        print(urun['name'])
        
        
    