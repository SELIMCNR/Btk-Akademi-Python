x= 5 
hak=5
devam='e'
result= 5<x<10

#Mantiksal opetörler
#and ve
result = x>5 and x<10   #false
result = (hak>0) and (devam == 'e') #true

#or veya
result (x>0) or (x & 2 ==0) #true

#not değil 
result =  not(x>0)

#x, 5-10 arasında bir çift sayı mı 
result = ((x>5) and (x<10)) and (x%2==0)
print(result)
 