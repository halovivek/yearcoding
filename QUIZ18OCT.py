person_1 = {'name':'Pratham','age':56}
person_2 ={'name':'Prasantha','age':70}
person_3 ={'name':'Insha','age':12}
person_4 ={'name':'Mike', 'age':30}

mini_database = [
    person_1,
    person_2,
    person_3,
    person_4
]

for person in list(mini_database):
    if 'VIVEK' in person.values():
        print('Mike is here')
    else:
        print("there is no Vivek here")

