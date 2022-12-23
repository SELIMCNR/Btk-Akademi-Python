#Identity Operator: is 

x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(x==z)
print(x is y)   #referanslara adreslere bakar
print(x is z)


x=[1,2,3]
y=[2,4]

del x[2]
y[1] = 1
y.reverse()  # tersten yazar.

print(x==y)
print(x is y)
print(x is not y) # adresler aynı değil mi 

#Membership Operator : in 
x=["apple","banana"]
print("banana" in x)


name = "Çınar"
print("banana" in x) # x içinde banana var mı 
print("Çınar"in name)
print("Çınar"not in name)






