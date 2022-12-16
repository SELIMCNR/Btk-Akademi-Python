ogrenciler= {
    '120': {
        'ad': input("isim gir"),
        'soyad':input('soyad'),
        'telefon':input('telefon')
    },
     '125': {
        'ad': input("isim gir"),
        'soyad':input('soyad'),
        'telefon':input('telefon')
    },
      '128': {
        'ad': input("isim gir"),
        'soyad':input('soyad'),
        'telefon':input('telefon')
    }
}
print(ogrenciler['120'])


ogrenciler= {
    input("numara"): {
        'ad': 'ali',
        'soyad':'yılmaz',
        'telefon':'532 000 00 01'
    },
    input("numara"): {
        'ad': 'Can',
        'soyad':'Korkmaz',
        'telefon':'532 000 00 01'
    },
      input("numara"): {
       'ad': 'Volkan',
        'soyad':'Yükselen',
        'telefon':'532 000 00 01'
    }
}



number = input("öğrenci no: ")
name = input("öğrenci adı : ")
surname = input("Öğrenci soyadı")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})
print("*"*50)
ogrNo = input("öğrenci no: ")
ogrenci = ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
