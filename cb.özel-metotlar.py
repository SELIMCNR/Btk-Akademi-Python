#built-in class python tarafından önceden tanımlanmıştır.
mylist = [1,2,3] 
myString = 'my string'


print(len(mylist))
print(len(myString))

class Movie():
    def __init__(self,title,director,duration=20):
        self.title = title
        self.director=director
        self.duration =duration
        print("Movie objesi oluşturuldu.")

    def __str__(self):   # class içine str fonksiyonu eklendi 
        return f"{self.title} by {self.director}"

    def __len__(self):   # class içine len uzunluk fonksiyonu eklendi
        return self.duration
    
    def __del__(self):   # class içine del silme fonksiyonu eklendi.
        print('movie silindi')
    
m=Movie('Film adı','Yönetmen adı',120)

print(str(mylist))
print(str(m))

print(len(m)) 
print(len(mylist))

del m 
print(m)
#Python specials methot ile googleda arat bulursun.