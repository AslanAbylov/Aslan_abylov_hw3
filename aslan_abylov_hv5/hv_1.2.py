import random

arrey = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
comp = print(random.choice(arrey))
player = int(input('Выберите число: '))
stavka = int(input('поствьте ставку: '))
cash = 1000

def game():
    if player == comp:
        stavka * 2
        stavka + cash
        print(f'вы выиграли на вашем счету {cash}')

    elif player != comp:
        cash - stavka
        print(f'вы проиграли ваш баланс {cash}')
game()




