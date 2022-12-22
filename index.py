from dataset import users, countries
import pprint

pprint.pprint(users)
best_occupation = {}
girls_drivers = []
user_wrong_password = []
max_salary_friends = 0
max_sum_salary_friends = 0
vip_user = ''
avg_flights = 0
del_user = False
count_friends_car = 0
count_travels = 0
print(len(users))

for user in users:
    sum_salary_friends = 0
    if user['password'].isdigit():
        user_wrong_password.append(dict({'name': user['name'], 'mail': user['username']}))
    if user.get('friends'):
        for i in range(len(user['friends'])):
            if user['friends'][i].get('cars'):
                count_friends_car += 1
                if user['friends'][i].get('flights'):
                    count_travels += len(user['friends'][i]['flights'])
                    avg_flights = round(count_friends_car / count_travels, 5)
                    for j in range(len(user['friends'][i]['flights'])):
                        if user['friends'][i]['flights'][j]['country'] in countries:
                            del_user = True
                if user['friends'][i]['sex'] == 'F':
                    girls_drivers.append(user['friends'][i]['name'])
            if int(user['friends'][i]['job']['salary']) > max_salary_friends:
                max_salary_friends = int(user['friends'][i]['job']['salary'])
                best_occupation = user['friends'][i]['job'].copy()
            sum_salary_friends += int(user['friends'][i]['job']['salary'])
        if sum_salary_friends > max_salary_friends:
            max_sum_salary_friends = sum_salary_friends
            vip_user = user['name']
    if del_user:
        key = ['mail', 'name', 'password', 'sex', 'username']
        for k in key:
            del user[k]
print('fr_car = ', count_friends_car)
print('trav = ', count_travels)


print(user_wrong_password)
print(girls_drivers)
print(best_occupation)
print(vip_user)
print(avg_flights)





