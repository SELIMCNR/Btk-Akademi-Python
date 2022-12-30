# belirtilen kelimeyi istenen şekilde gösterme
a= input("Kelimeyi giriniz: ")
b=int (input("Kaç kez gösterilsin"))
def kelimegöster(a,b):
    print(a*b)

kelimegöster(a,b)    

#kendine gönderilen sınırsız sayıdaki parametreyi listeye çevirme

def func(*params):
       print(list(params))
func(10,20,30,40,50,60)  

# gönderilen 2 sayı arasındaki tüm asal sayıları bulma 
sayi= int(input("Sayi1 "))
sayi2 = int(input("Sayi2 "))
def asalbul(sayi,sayi2):
    for sayi in range(sayi,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if(sayi % i ==0):
                    break
            else:
                print(sayi)     
asalbul(sayi,sayi2)


# Tam bolenleri bul 
def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2,sayi):
        if(sayi %i == 0):
            tamBolenler.append(i)
    return tamBolenler 
print(tamBolenleriBul(10))       
            
            
            