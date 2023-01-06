# Object Oriented Programming (OOP)
#Class  Classlar özellik tutuar ve yeni objeler oluşturmaya yarar.
#ınstanve (object) : Class özelliklerinden oluşur.
#objeye bağlı metot objeye bağlı değil metot.
'''
# List kütüphane içinde oluşturulan bir yapı
lst  = [1,2,3]
lst1 = [1,2,3,4]

result = type(lst)
result = type(lst1)

print= result


# Kendi classımızı oluşturuyoruz.
# class => Person(name,surnmae,age,birthday,calculateAge())
class Person1:
    #pass # yer tutucu görev üstlenir.
    # class attributes özellikler
    addres = "No information "
    #constructor (yapıcı metot)
    def __init__(self,name,year): #init metodu her bir objede çalışır
      
        #object attributes         #self,this de olabilir. oluşturulacak objeleri temsil eder.
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
    # metotlar
    def intro(self):
        print("Hello there" + self.name)
    def calculateAge(self):
        return 2019 - self.year

#object => instance
p1 = Person1(name='selim',year=2000)  # Person classından p1 objesi oluştu.
p2 = Person1('ali',1995)
p1.intro()
p2.intro()
print(f"adım: {p1.name} ve yaşım : {p1.calculateAge}")
print(f"adım: {p2.name} ve yaşım: {p2.calculateAge()}")



#)

#updating
p1.name = 'Ahmet'
p1.addres = 'Kocaeli'




print(f"p1: name {p1.name} year: {p1.year} address: {p1.addres}")
print(f"p2: name {p2.name} year: {p2.year} address: {p2.addres}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))

print(p1 == p2)
'''
#Metot
class Circle : 
    #Class object attribute
    pi = 3.14
    
    def __init__(self,yaricap=1):
        self.yaricap= yaricap
        
    #Methods
    def cevre_hesapla(self):
        return 2* self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    

c1=Circle()  #yaricap = 1
c2=Circle(5) #yaricap = 5

print(f'c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c1 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')

# Inheritance (Kalıtım) : Miras alma 


# Person  => name ,lastname, age, eat() , run(), drink()

#Student(Person), Teacher(Person)

#Animal => Dog(Animal) , Cat(Animal)

class Person ():
    def __init__(self,fname,lname):
        self.firstname = fname   #kalıtım yoluyla özellik eklendi
        self.lastname = lname
        print("Person Created")


    def who_am_i(self):
        print('I am a person')

    
    def eat(self):
        print("I am eating")
        
    

class Student(Person):   #Student klası persondan miras aldı.
    def __init__(self,fname,lname,number):  #Student clası init edildi başlatıldı
        Person.__init__(self,fname,lname)  #Person clası init edildi başlatıldı
        self.studentNumber = number
        print("Student Created")

    # override diğer clasdaki metodu kalıtım yoluyla alsada kullanmadı 
    #Aynı isimdeki kendi metodunu kullandı.
    def who_am_i(self):
        print("I am a student")
    
    def sayHello(self):
        print("Hello I am a student")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname,lname) #  Person.__init__(self,fname,lname) bunun yerine kullanılır.
        self.branch = branch    

    def who_am_i(self):
        print (f'I am a {self.branch} teacher')

p1=Person('Ali','Yılmaz')
s2=Student('Çınar','Turan',1256) #kalıtım yoluyla person öğesinin özelliklerini aldı.
t1 = Teacher('Serkan','Yılmaz','Math')

print(p1.firstname + ' ' +p1.lastname)
print(s2.firstname + ' ' +s2.lastname + ' '+ str(s2.studentNumber)) #kalıtım yoluyla özellikler çalıştırıldı.


p1.who_am_i()
s2.who_am_i() # kalıtım yoluyla student clası person clasında metotu override etti yani ezdi.

p1.eat()
s2.eat()
s2.sayHello()

t1.who_am_i()



 



        
        
     
        



