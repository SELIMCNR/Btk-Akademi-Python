arabalar=["Bmw","Mercedes","Opel","Mazda",'Toyota'] # liste oluşturma
listeuzunluk=len(arabalar) # listeuzunluğu
Listeilk=arabalar[0] #liste ilk eleman
Listeson = arabalar[4] # liste son eleman
Listeson2 = arabalar[-1]

listesondeğişim=arabalar[-1] = "Renault" # sondaki elemanı değiştir.

elemanımı = "Mercedes" in arabalar # Mercedes arabalar listesinde var mkı ? 

sondanikinciindeks= arabalar[-2] # sondan ikinci eleman

İlkucelemanılistele=arabalar[0:3] # ilk uc elemanı listele
İlkucelemanılistele2=arabalar[:3] # ilk uc elemanı listele
İlkucelemanılistele3= arabalar[-2:]

yerineata=arabalar[-2:]=["Toyota","Renault"] #son iki eleman yerine toyota ve renault ekle.

eklemeler= arabalar + ["Audi","Nissan"] # iki elemanı ekle

del arabalar[1] # son elemanı siler
 
terstenyazdırma = arabalar[::-1] #terstenyazdırma işlemi
 
studentA = ["Yiğit Bilgi",2010,[70,60,70]]
studentB = ["Sena Turan",1999,[80,80,70]] 
studentC = ["Ahmet Turan",2010,[80,70,90]]

ilkelemana = studentA[0]
ilkelemanb = studentB[0]
ilkelemanc = studentC[0]
notuC= studentC[3][1]
ortalaması=f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması{(studentA[3][0]+studentB[3][1] + studentC[3][2]) / 3}"

