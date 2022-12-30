import random 
sayi = random.randint(1,100)
can=int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac=0
while hak>0:
    hak -=1 
    sayac +=1
    tahmin = int(input("Tahmin: "))
    
    if sayi == tahmin :
        print(f"Tebrikler {sayac}.defada bildiniz. Toplam puanınız: {100-(20)*(sayac-1)}")
        break 
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")
    
    if hak == 0 :
        print(f"Hakkınız bitti . Tutulan sayı : {sayi}")
        
'''
Asal sayı hesapla 
'''                     

sayi1 =int (input('sayı: '))
asalmi = True

if sayi ==1:
    asalmi=False

for i in range(2,sayi):
    if(sayi % i==0):
        asalmi = False
        break
    
if asalmi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.") 
    
    
    
           
    
    
    
    