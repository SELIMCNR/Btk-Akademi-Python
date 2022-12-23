#1-
isim=input("isim giriniz: ")
yaş=int(input("Yaş giriniz: "))
eğitim=input("Eğitim bilgileri ")

result = f"ehliyet alabilmedurum: {yaş>=18 and (eğitim=='lise' or eğitim=='üniversite')}"

if(yaş>=18 and (eğitim=="lise" or eğitim=="üniversite")):
    result="Ehliyet alabilir"
else :
    result="Ehliyet alamaz"


print(result)


#2- 2 yazılı bir sözlü notu ile ortalamaya göre not bilgisi 
yazılı=int(input("Yazılı: "))
yazılı2=int(input("Yazılı2: "))
sözlü=int(input("Sözlü 1: "))
ortalama=(yazılı+yazılı2+sözlü) / 3 
result=ortalama
print(result)

if(ortalama<24):
    result="Not karşılığı 0"
elif (ortalama>25 and ortalama<44):
    result="Not karşılığı 1"
elif (ortalama>45 and ortalama<54):
    result="Not karşılığı 2"
elif (ortalama>55 and ortalama <69):
    result="Not karşılığı 3"
elif (ortalama>70 and ortalama <84):
    result="Not karşılığı 4"
elif (ortalama>85 and ortalama<=100):
    result="Not karşılığı 5"                
print(result)    

#3- Trafiğe cıkış tarihi alınan bir aracın servis zamanını hesapla.
import datetime 
tarih=input("aracınız hangi tarihte trafiğe çıktı (2019/8/9)")
tarih=tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now
fark=simdi-trafigeCikis
days=fark.days 

if  days<=365:
    print("1.servis aralığı")
elif days>365 and days<=365*2:
    print("2.servis aralığı") 
elif days>365*2 and days <= 365*3:
    print("3.servis aralığı")
else:
    print("Hatalı süre.")
    
""" 
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
"""              
sayi = float(input("sayı :"))
if (sayi>0) and (sayi<100):
    result = "Sayi 0 ile 100 arasında"
else:
    result = "Sayi 0 ile 100 arasında değil"
    
""" 2- Girilen sayi pozitif çift sayi mi 
"""            
if(sayi>0) and (sayi%2==0):
    result= "Sayi çift ve pozitif"
else:
    result= "Sayi çift değil"
print(result)    

"""3-Email ve parol bilgileri ile giriş kontrolü 

"""
email = "email@scinar.com"
password='abc123'

girilenEmail = input('email: ')
girilenPassword = input("password: ")

if email==girilenEmail and password==girilenPassword:
    print("Giriş başarılı")
else:
    print("Giriş hatalı")

'''
    4- Girilen 3 sayıyı büyüklük olarak karşılaştır
'''
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if a>b and a>c:
    print("En büyük olan",a)
elif b>a and b>c:
    print("En büyük olan ",b)
elif c>a and c>b:
    print("En büyük olan",c) 

'''
    5-Kullanıcıdan 2 vize ve final notu alıp ortalama hesapla.
    ort> 50 ? geçti : kaldı  
    b-) final>70 ortalama önemi yok
'''    
vize1 = float(input('vize 1: '))
vize2 = float(input ('vize 2:'))
final = float(input('final : '))

ortalama= ((vize1 + vize2)/2)*0.6 + (final *0.4)
if ortalama > 50 :
    result = "Geçti "
else :
    result = "kaldı"

#
if ortalama>=50 and final >50:
    result="Geçti"
else:
    result ="kaldı"

#
if (final>70) or (ortalama>50): 
    result = "Geçti"
else:
    result = "Kaldı"
print(result)

'''
ad,kilo ve boy bilgileri ile kilo indexlerini hesapla
0-18.5  => zayıf 18.5-24.9 => normal  25.0 - 29.9 => fazla kilolu 30.0-34.9 => şişman 
'''    

ad = input("adınız : ")
kg = float(input("kilonuz : "))
hg = float(input("boyunuz "))
index =(kg) / (hg **2)

if index <18.4:
    result=f"{name} indexin Zayıf "
elif  18.5<index <24.9:
    result=f"{name} indexin Normal"
elif  25.0<index <29.9:
    result=f"{name} indexin kilolu"
elif  30.0<index <45.9:
    result=f"{name} indexin (obez)"
    
    
               
        
    
                
       
    
