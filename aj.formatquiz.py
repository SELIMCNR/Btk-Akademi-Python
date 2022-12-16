website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama (40 saat)"

coursekaraktersayısı = len(course)  # toplam karakter sayısı

websitewww = website[7:10] ## www olan kısım 
websitecom = website[22:25] # com olan kısım
courseilk15= website[0:15] # ilk onbeş karakter
courseson15= website[9:25] # son onbeş karakter
coursetersten = website[::-1] # terstenyazdırma

name,surname,age,job = "Bora","Yılmaz",32,"Mühendis" # çoklu değişken tanımı
hello="hello world"
hello[6] = "W"          # değişken içerisindeki tek karakteri değiştirme.
hello= hello[0:6] + "W" + hello[-4:]
ifade = "abc" * 3       # abc ' yi 3 defa yazdır.

print(coursekaraktersayısı)
print(websitewww)
print(websitecom)
print(courseilk15)
print(courseson15)
print(coursetersten)
print("Benim adım "+name + " "+surname + ", Yaşım"+ str(age)+ "ve mesleğim"+ job)
print("Benim adım {0} {1} , Yaşım {2} ve mesleğim {3} . ".format(name,surname,age,job))
print(f"Benim adım {name} {surname} ,yaşım {age} ve mesleğim {job}")
print(hello)
print(ifade)


 