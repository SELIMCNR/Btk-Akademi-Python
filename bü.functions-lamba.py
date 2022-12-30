# map metodu liste içerisinde değerleri map(fonksiyon,liste) 
# fonksiyonda döndürür ve liste olarak yazdırır 
def square (num):
    return num **2 

numbers = [1,3,5,9]
#map metodu yazdırma yöntemleri 
result = list(map(square,numbers)) # map metodunu ya liste ile 
                                  # yada for döngüsü ile çalıştırırsın
print(result)

for item in map(square,numbers):
    print(item)

    
    
#lambda isimli yada isimsiz fonksiyon oluşturur.
result = list(map(lambda num:num**2,numbers))
print(result)

# isimli lambda fonksiyonu 
square = lambda num : num ** 2  
result = list(map(square,numbers))
print(result)

#filter işlemi filtrele fonksiyonu filter(fonksiyon,liste)
numbers=[1,2,3,4,5,6,7]
def check_even(num):
    return num%2==0  

result = list(filter(check_even,numbers)) 
print(result)


#lambda ile kullanım 
result = list(filter(lambda num: num %2 ==0,numbers))
print(result)

lambdascheck_even= lambda num: num % 2 ==0
result = list(filter(lambdascheck_even,numbers))
print(result)

# global ve local değişkenlerle fonksiyonlar 
x="Global x"
def function():
    x= "local x"
    print(x)
    
function() # local x değişkeni gelir
print(x) #global x değişkeni gelir.

#gloabal scope
name = "Çınar"
def changName(new_name):
    #local scope
    global name
    name = new_name
    print(name)
changName("ada") # local değişkene atanan parametre değeri gelir.
print(name)  # gloabal değişken değeri gelir 


#########################################
#İçe içe fonksiyon kullanımı
#global scope
name = "global string" 
def greeting():
    #local scope
    name = "Çınar"
    def hello():
        #name = "ada" olsaydı bu alan yazdırılırdı
        print("Hello"+name)
    hello() # local alanda name gelir
greeting() # global alanda name gelir 

x = 50 
def text(x):
    #global x değeri global yapar 
    print(f"x:  {x}" ) 
    
    x=100
    print(f"changed x to {x}"  )

text(x)    
print(x) #global alanda değer gelir.    
        




    


