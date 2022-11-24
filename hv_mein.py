import random
from hv_construction import Compareresult

class Casino:
    def __init__(self):
        self.arrey = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        self.bid_u = int(input('поставьте ставку : '))
        self.comp = print([random.choice(self.arrey)])
        self.player = int(input('выбери число от 1 до 30: '))



    def game(self):
        while True:
            compare_1 = Compareresult(player_list=self.player, comp_list=self.comp, bid=self.bid_u, )
            if compare_1.compare_results():
                break
games_1 = Casino()
games_1.game()