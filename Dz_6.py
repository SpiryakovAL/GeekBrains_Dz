#Урок №6
print ("Задача №1")

with open ('nginx_logs.txt', 'r', encoding ="utf-8") as f:
    requests_list = []
    for l in f:
        remote_addr = l[:l.find (' ')]
        request_type = l[l.find('"')+1: l.find('"')+4]
        requested_resource = l[l.find('\d'): l.find('HTTP')-1]
        tuple_requstests=(remote_addr,request_type,requested_resource)
        requests_list.append(tuple_requstests)
print(requests_list)

print ('\n Задача №2\n')

with open ('nginx_logs.txt', 'r', encoding ="utf-8") as f:
    requests_lst = []
    for l in f:
        remote_addr = l[:l.find(' ')]
        requests_lst.append(remote_addr)
    a = max(set(requests_lst), key=requests_lst.count)
print (a, 'количество отправленных запросов', requests_lst.count(a))

print ('\nЗаздача№3\n')

from itertools import zip_longest
import json

with open ('user.csv', 'r', encoding ="utf-8") as user,\
    open ('hobby.csv', 'r', encoding='utf-8') as hobby:

    users=user.read().splitlines()
    hobbys=hobby.read().splitlines()

if len(users) < len(hobbys):
    print (1)
else:
    users_hobby = dict(zip_longest(users,hobbys, fillvalue=None))
    with open ('users_hobby_dict.txt', 'w') as f:
        json.dump(users_hobby, f)
    with open ('users_hobby_dict.txt', 'r') as f:
        rez=json.load(f)
        print (rez)
