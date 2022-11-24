import random

Fortuna = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
comp = print(random.choice(Fortuna))
# user_cash = [1000]
user = int(input('выберите число от 1 до 30: '))
stavka = list(int(input('поставьте ставку: ')))


def game(user_cash=1000):
    if comp == user:


