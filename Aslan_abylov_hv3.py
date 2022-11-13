class Computer:
    def __init__(self, cpu, memories):
        if isinstance(cpu, int):
            self.__cpu = cpu
        else:
            raise TypeError('cpu should be integer')

        if isinstance(memories, int):
            self.__memories = memories
        else:
            raise TypeError('memories should be integer')

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memories(self):
        return self.__memories

    @memories.setter
    def memories(self, value):
        self.__memories = value

    def make_computations(self):
        return self.__cpu + self.__memories

    def __gt__(self, other):
        return self.__memories > other.memories

    def __lt__(self, other):
        return self.__memories < other.memories

    def __eq__(self, other):
        return self.__memories == other.memories

    def __ne__(self, other):
        return self.__memories != other.memories

    def __le__(self, other):
        return self.memories <= other.memories

    def __ge__(self, other):
        return self.memories >= other.memories

    def __str__(self):
        return f'Cpu: {self.__cpu} memories: {self.__memories}'

class Phone:
    __sim_cards_list = 'belain'

    @classmethod
    def get_sim_cards_list(cls):
        print(cls.__sim_cards_list)

    @classmethod
    def set_sim_card_list(cls):
        return cls.__sim_cards_list

    def call(self, sim_card_number, call_to_number ):
        return f'Идет звонок на номер: {call_to_number} c сим карты {sim_card_number} {self.__sim_cards_list}'

    def __str__(self):
        return f'Sim cards: {self.__sim_cards_list}'

class SmartPhone(Computer, Phone):
    __sim_cards_list = 'O!'
    def __init__(self, cpu, memories):
        Computer.__init__(self, cpu, memories)
        Phone.__init__(self)

    def use_gps(self, location):
        return f'Маршрут с этого место до {location} был построен'

    def __str__(self):
        return f'cpu in phone: {self.cpu}, memory: {self.memories}, sim card: {self.__sim_cards_list}'


my_comp = Computer(200, 300)
my_phone = Phone()
my_smart_phone = SmartPhone(100, 400, )
smart_phone = SmartPhone(250, 150 )
print(my_smart_phone)
print(my_comp)
print(my_comp.make_computations())
print(my_phone)
print(my_phone.call('1', '493094394'))
print(smart_phone)
print(my_smart_phone < my_comp)
print(my_smart_phone > my_comp)
print(my_smart_phone == my_comp)
print(my_smart_phone != my_comp)
print(my_smart_phone >= my_comp)
print(my_smart_phone <= my_comp)