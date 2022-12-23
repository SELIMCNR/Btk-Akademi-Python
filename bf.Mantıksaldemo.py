#1 0ile100 arasında
sayi= int(input("Sayi gir "))
arasındamı =   0<sayi<100
result = f"Sayi : {sayi} 0 ile 100 arasındamı {arasındamı}"

#2 pozitif çift 
pozitif = sayi>0 
çift = sayi %2 ==0 
result= f"Sayi : {sayi} pozitifmi  {pozitif}  çiftmi {çift}"

#3 Email-parola
emaildeger=input("Email degeri: ")
passworddeger=int(input("Passwordd: "))

email = "Btk@gmail.com"
password=1234
result =(f"Giriş durumu : {email==emaildeger and password == passworddeger}")



#4 girilen 3 sayiyi büyüklük olarak karşılaştır 
sayi1=int(input("sayi1 gir: "))
sayi2=int(input("Sayi2 gir: "))
sayi3=int(input("Sayi3 gir: "))
result=(f"Sayi1 en büyükmü{sayi1>sayi2 and sayi2>sayi3}") 
print(result)

#5 2 vize ve final notu ile ortalama hesapla 
vize= int(input("vize : "))
final=int(input("final: "))
ort=(vize*0.4)+(final *0.6)
result= f"Ortalama:{ort} geçti:{ort>50} kaldı:{ort<50}"
result= f"Ortalama:{ort} geçti: {final>=50 and ort>50}"
result= f"Ortalama:{ort} geçti:{final>70 or ort>50}"
print(result)

#6
ad=input("adınız: ")
kg=float(input("kilonuz: "))
boy=float(input("Boyunuz: "))
kgindex=(kg/(boy*boy))

result=f"Zayıf:{kgindex<18.4},Normal:{18.5<kgindex<24.9} Fazlo kilolu: {25<kgindex<29.9} Şişman: {30<kgindex<34.9}"
print(result)


