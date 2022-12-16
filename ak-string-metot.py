message = " hello There . My name is Sadık Turan"

message = message.upper() # metotlarda () parantez aç kapa  tüm karakterler büyük harf oldu 
message2 = message.lower() # hepsini küçük harfe çevirir.
message3 = message.title() # her kelimenin baş harfi büyük harf olur 
message4 = message.capitalize() # sadece ilk harf büyük harf olur.
message5 = message.strip()  #başdaki ve sondaki boşlukları siler
message6 = message.split()  # cümleyi dize haline çevirir.
message7 = message.split('.') # noktalar arası ayırır 
message8 = "".join(message6) # boşluklar şeklinde birleştirir.
message9 = "--".join(message6)

arananindex=message.find('Sadık') # aran kelime varsa + bir indeks değeri gelir yoksa -1 değeri gelir.

neilebaşlıyor= message.startswith("h") # h harfi ile başlıyorsa true başlamıyorsa false
neilebitiyor = message.endswith("n") # n harfi ile bitiyorsa true yoksa false değeri alır.

kelimedeğiştirme= message.replace("Sadık","Çınar") # sadık kelimesini Çınar yapar.
kelimedeğiştirme2= message.replace("","*")
kelimedeğiştirme3= message.replace("ç","c").replace("ö","o").replace("","-")
ortala= message.center(50) # 50 karakterlik boşluklar ile ortalar

print(message)
print(message6[2]) #split ile dizi olan değişkenden 2.indisi getir
print(message7)
print(message7)
print(message8)
print(message9)
print(arananindex)
print(neilebaşlıyor)
print(neilebitiyor)
print(kelimedeğiştirme)
print(kelimedeğiştirme2)
print(kelimedeğiştirme3)
print(ortala)


