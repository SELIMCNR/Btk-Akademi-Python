def changeName(n):
    n="Selim" #bu değer şuan geçersiz

name="yiğit" # bu değer parametreye verilir

changeName(name)    
print(name)


def change(n):
    n[0] = "İstanbul" # listeye bu eleman eklenir
    
sehirler = ["Ankara","İzmir"]
change(sehirler) # sehirler dizisinin ilk elemanı İstanbul olur 
print(sehirler)

change(sehirler[:]) # listenin kopyasını oluşturur slicing işlemi ile.
print(sehirler)


n = sehirler 
n= sehirler[:] # slicing işlemi 
n[0] = 'istanbul'
print(sehirler)


def add(a,b):
    return sum((a,b))           #sum gömülü fonksiyon 
print(add(10,20))

#Params kullanımı
def add(*params):  # params çoklu değer girişi sağlar 
    print(params[0]) # paramsda ilk indisi getir.
    print(params[1]) # paramsda ikinci indisi getir.
    return sum((params))
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40,50,60,70,80))


##* params tuple,list fonksiyon 
def add(*params):  #(*params ) ->tek yıldız tuple,list değer alır
    print(type(params))
    sum = 0 
    for n in params:
        sum = sum + n 
    return sum     

print(add(10,20,30,40,50,60,70,80))



##** args dictonary fonksiyon 
def displayUser(**args):  # **args = **params -> çift yıldız dictionary değer alır
    print(type(args))
    for key,value  in args.items():
        print("{} is {}".format(key,value))
    
displayUser(name="Çınar",age=2,city="İstanbul")
displayUser(name = "Ada",age=12,city="Kocaeli",phone="1234",)    
displayUser(name = "Yiğit",age=14,city="Kahramanmaraş",phone="1234",email="yigit@gmail.com")


def myfunc(a,b,c,*args,**kwargs):
    print(a) # a parametresi
    print(b) # b parametresi
    print(c) # c parametresi
    print(args) # args içerisinde liste
    print(kwargs) # kwargs içerisinde sözlük
 
myfunc(10,20,30,40,50,60,70,key1 = "value1",key2="value2")
    
