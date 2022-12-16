sehirler = ['kocaeli','istanbul']
plakalar=[41,34]

plakalar=plakalar[sehirler.index('kocaeli')] #plakayı getirdi

#dictionary oluşturma 
plakalar = {'kocaeli': 41,'İstanul':34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

#dictionary değer atama
plakalar['ankara'] = 6 
plakalar['koceli'] = 'new value'

users = {
    'sadikturan':{
        'age':36,
        'roles':['admin','user'],
        'email': 'sadik@gmail.com',
        'address':'Kocaeli',
        'phone':'15616516'
    },
    'cinarturan':{
        'age':36,
        'roles':['user'],
        'email': 'sadik@gmail.com',
        'address':'Kocaeli',
        'phone':'15616516'
    }
}
print(users['cinarturan']['age'])
print(users['cinarturan']['email'])
print(users['cinarturan']['address'])

print(users['cinarturan']['roles'][0])



