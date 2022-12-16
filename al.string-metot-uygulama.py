website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama (40 saat)"

hello = " Hello World ".strip() # baş ve sondaki karakterleri sil
hello2 = " Hello World ".lstrip() # soldaki boşlukları sil 
hello3 = " Hello World ".rsplit() # sağdaki boşlukları sil

silme = "www.sadikturan.com".strip("w.moc")


kucukharf = course.lower # tüm karakterleri küçük harf yap
buyukharf= course.upper  # tüm karakterleri büyük harf yap 
Başharf = course.title  # her kelimenin baş harfi büyük 

kactane = website.count("a") # kaç tane a var
kactane1 = website.count("www")
kactane2 = website.count("www",0,10)

başlıyormu = website.startswith("www")
bitiyormu  = website.endswith("com")

bul = website.find("com") # com ifadesi var mı ? 
bul2 = website.find ("com",0,10)
bul3 = website.find("Python")
bul4 = website.rfind("Python")

index = website.index("com") # com ifadesi indexi kaçta ? 
index1 = website.rindex("com")
index2 = website.rindex("comm")

alfabetikmi = course.isalpha() # karakterler alfabetikmi 
alfabetikmi = "Hello".isalpha()
sayısalmı = course.isdigit() # karakterler sayısalmı 
sayısalmı2 = "123".isdigit()

ortala = "Contents".center(50,"") # 50 karakter boşluklu ayır
ortala2 = "Contents".center(50,"*")
ortala3 = "Contents".ljust(50,"*")
ortala4 = "Contents".rjust(50,"*")

degistir = course.replace(" ","-") # boşluklara - karakter koy
degistir2 = course.replace(" ","-",2)
degistir3 = course.replace(" ","")
degistir4 = "Hello World".replace("World","There")

böl = course.split(" ") # listelere ayırır
böl = böl[2]

print(böl)

