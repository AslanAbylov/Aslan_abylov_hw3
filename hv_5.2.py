import aslan_abylov_hv5
from random import randint
comp = print(randint(1, 30))
user_cash = 1000
user = int(input('выбери число из 1 - 30: '))
stavka = int(input('введите ставку: '))

user_cash -= stavka
if user == comp:
    stavka *= 2
    user_cash += stavka
    print(f'вы выиграли! ваш баланс : {user_cash}')

elif user != comp:
    user_cash -= stavka
    print(f'вы проииграли ваш баланс {user_cash}')

else:
    print('что то пошло не так')
