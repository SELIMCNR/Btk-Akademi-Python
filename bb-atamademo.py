x,y,z = 2,5,10 
numbers = 1,5,10,7,6

#1 
s1=int(input("Sayi1: "))
s2=int(input("Sayi2: "))
carp=s1*s2
toplam=x+y+z 
fark = carp -toplam
print("sayilarin farki ",fark)

#2
kalansızbolum=y//x
print("Sayilarin kalansız bolumu: ",kalansızbolum)
#3
mod= toplam % 3
print("sayilarin modu",mod)
#4
kuvvet = y **x 
print(kuvvet)
#5 
x,*y,z = numbers 
#x 1.eleman ,y ortadaki elemanların hepsi,z son elemanı alır.
küp = z*z*z
print(küp)
#6 
topla=y[0]+y[1]+y[2]
print(y)
print(topla)
