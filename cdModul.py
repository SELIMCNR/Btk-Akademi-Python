#Module 
#1-Kendi modüllerimiz olabilir
#2-Hazır modüller 
""" 
     A-Standart Kütühane modülleri
     B-Üçüncü Şahıs modülleri 
     PyPI hazır modüller bulunur.
     Örnek Django
     pip install Django
"""

#Hazır modül kullanımı 
import math          # matemetik modülü eklendi projeye

value = dir(math) # math modülü metotlarını bilgilerini gösterir.
value = help(math) # math modülü hakkında bilgiler verir.
value = help(math.factorial) # Math modülü içinde  faktoryel metodunu çalıştırır.

value = math.sqrt(49)   # karekök alır
value = math.factorial(5) #faktoriyel hesaplar.
value = math.floor(5.9) # aşağı yuvarlar
value = math.ceil(5.9) # yukarıya yuvarlar

print(value)
#cls consolu terminali temizler.

#Yöntem 1
import math as islem   # modulun adi islem oldu
value=islem.factorial(5)

#Yöntem 2 
from math import *     # math kütüphanesinden hepsini import eder.

value = factorial(5)
value = sqrt(9)
print(value)

#Yöntem 3 
from math import floor,ceil  # math kütüphanesinden floor ve ceil i seç 
value = floor (4.4)
value = ceil (4.9)
print(value)

def sqrt(x):
    print('x : ' + str(x))


'''
    Random modülü 
'''
import random         # random  kütüphanesi eklendi
result = dir(random)   
result = help(random)  

result = random.random() #0.0 - 1.0
result = random.random() * 100 #0.0 - 100.0
result = int(random.uniform(10,100)) #10 - 100 
result = random.randint(1,100) #1 - 100

names = ['ali','yağmur','deniz','cenk']
result = names[random.randint(0,len(names)-1)] #listeyi yazdırır.
greeting = 'hello there'
result = random.choices(names)   # karaterleri yazdırır.
result = random.choice(greeting)    

liste = list(range(10))
random.shuffle(liste)  # random olarak liste elemanları gelir.
result = liste

liste = range(100)

result = random.sample(liste,3) #rastgele listeden 3 eleaman getir.
result = random.sample(names,2)
print(result)


#Modül Hazırlama import cdModul yaz diğer pytona ekle
'''
    Modül hakkında bilgilendirme
'''
number = 10 

numbers = [1,2,3]

person = {
    'name' : 'Ali',
    'age'  : '25',
    'city' : 'istanbul'
}

def func(x):
    '''
        Fonksiyon hakkında bilgilendirme
    '''

print(result)





