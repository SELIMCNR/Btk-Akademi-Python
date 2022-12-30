#geriye değer döndüren fonksiyon
def sayHello(name = "user"):
    print("Hello "+name)
    
sayHello("Selim")    
sayHello("Yusuf")        
sayHello("Çınar")    
sayHello()

#geriye değer döndürmeyen fonksiyon
def sayHello(name = "user"):
    return "Hello" + name

msg = sayHello("Selim")
msg = sayHello("Çınar")
print(msg)

def total(num1,num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)


def yasHesapla(dogumYili):
    return 2022 - dogumYili
ageCinar = yasHesapla(2000)
ageYusuf = yasHesapla(2013)
ageName = yasHesapla(1999)

def EmekliligeKacYilKaldi(dogumYili,isim):
    """_summary_

    Args:
        dogumYili (_type_): Input girişi gerekli
        isim (bool): Input girişi gerekli
    """
    yas = yasHesapla(dogumYili)
    Emeklilik = 65 - yas 
    if Emeklilik > 0 :
        print(f"Emekliliğinize {Emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")

EmekliligeKacYilKaldi(1983,"Ali")
EmekliligeKacYilKaldi(1950,"Ahmet")
EmekliligeKacYilKaldi(2000,"Selim")

print(help(EmekliligeKacYilKaldi)) 

list = [1,2,3]
print(help(list.append)) # bilgi verir fonksiyon hakkında


