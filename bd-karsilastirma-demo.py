#1 
a=int(input("a: "))
b=int(input("b: "))
result = a>b
print(f"A:{a} b: {b} den büyüktür: {result}")

#2 
vize1 = float(input("1.vize: "))
vize2 = float(input("2.vize: "))
final = float(input("final: "))
ortalama= (((vize1+vize2)*0.6)/2) + (final *0.4)

print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz{ortalama>50}")

#3
sayi = int (input("sayı : "))
tekcift = (sayi %2 ==0) 
print(f"girilen sayı çift olma durumu : {tekcift}")

#4
sayi = int(input("sayı: "))
pozitifmi = (sayi>0)

print(f"girilen sayının pozitif olma durumu : {pozitifmi}")

#5
email = "email@sadikturan.com"
password= 'abc123'

girilenEmail = input('email:')
girilenPassword = input('parola: ')

isEmail =(email == girilenEmail.lower.strip())
isPassword= (password == girilenPassword.lower)

print(f'Email bilgisi dogrumu: {isEmail} ve Parola doğrumu : {isPassword}')
