import cdModul  as mod  #cdModul  eklendi 

result = help(mod)
result = help(mod.func)
result = mod.number
result = mod.numbers
result = mod.person["name"]
result = mod.person["age"]
result = mod.func(10)


p = mod.person()
p.speak()
print(result)
'''
python/lib içerisine modülü atarsan yine çalışır.
yada 
dll olarak yer alanlar built in fonksiyonlardır örnek random
dll'e dönüşüm yapılabilir.
'''