import json
import os
import pathlib
# people = ['piotr', 'anna', 'jolanta', 'grzechu']
# people_tuple = ('piotr', 'anna', 'jolanta', 'grzechu')

# print(type(people))
# new_people = list(people_tuple)
# #print('append: ', new_people.append('kazik'))

# # lista.append(el) - dodaje na koniec
# # lista.insert(index,el) - dodaje na index
# # lista.remove(lista[index]) - usuwa
# females = 0
# for person in people:
#     if person[-1] == 'a':
#         # females=females+1
#         females += 1

# if 'kazik' in new_people:
#     print('czesc kazik')
people = ['jan', 'piotr', 'jan', 'anna', 'jolanta', 'anna', 'grzechu']
names = list(set(people))
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# print(a.union())


def count_paint(eff_per_m2, *rooms, **roomies):
    # return eff_per_m2*sum(rooms)
    paint_per_person = {}
    for area, (room_no, name) in zip(rooms, roomies.items()):
        paint_per_person[name] = area*eff_per_m2
    return paint_per_person


# print(count_paint(2, 4, 8, 15, room1='maciej', room2='sebastian', room3='piotr'))
credentials = {'email': 'piotr@wp.pl',
               'password': 'piotr123', 'login': 'piotrus'}

people = {
    1: ['Piotr', 'Peplinski', credentials, {'remote': True}],
    2: ['Jan', 'Kowalski', {
        'login': 'jano',
        'password': 'jan123'
    }, {'remote': False}]
}

base_dir = pathlib.Path(__file__).resolve().parent
path = os.path.join(base_dir, 'data','people.json')

# r,w,a
# r+,w+,a+
with open(path, 'w', encoding='utf-8') as file:
    json.dump(people, file)
    #zamkniecie

# def save_credentials(login, email, password):
#     print(login)
#     print(email)
#     print(password)


# save_credentials(credentials['login'],
#                  credentials['email'], credentials['password'])
# save_credentials(**credentials)
# save_credentials('hello_world',password='hello123',email='hello@wp.pl')
