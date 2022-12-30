hesapA = {
    'ad' : 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye' : 3000,
    'ekHesap': 2000
}
Sadikhesap = {
    'ad' : 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye' : 3000,
    'ekHesap': 2000
}


AliHesap= {
    'ad' : 'Ali Turan',
    'hesapNo': '15245678',
    'bakiye' : 5000,
    'ekHesap': 2000
}



def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if(hesap['bakiye'] >= miktar):
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap'] 
        
        if (toplam >= miktar):
            ekHesapKullanimi=input("Ek hesap kullanılsın mı (e/h)")
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("paranızı alabilirsiniz. ")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır") 
        else:
            print("Üzgünüz bakiyeniz yetersiz. ")
            bakiyeSorgula(hesap)
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.Ek hesap limitiniz ise {hesap ['ekHesap']} TL bulunmaktadır.")
paraCek(Sadikhesap,5000)    
bakiyeSorgula(Sadikhesap)
print("***********************")
paraCek(Sadikhesap,4000)    
bakiyeSorgula(Sadikhesap)
