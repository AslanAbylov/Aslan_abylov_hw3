
class Figure:
    unit = ' '
    def __init__(self):
        pass

    def info(self):
        pass

    def calculate(self):
       pass



class Circle(Figure):
    unit = 'cm'
    def __init__(self, radius):
        super(Circle, self, ).__init__()
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def calculate(self, const=2):
        return (f'Circle area: {const * self.__radius * self.__radius}')

    def info(self):
        print(f'Circle radius: {self.__radius}{self.unit} {self.calculate()}')



class RightTriangle(Figure):
    unit = 'sm'
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b
        super(RightTriangle, self).__init__()

    def calculate(self):
        return (f'RightTriangle area:{(self.__side_a * self.__side_b) / 2}')

    def info(self):
        print(f'RightTriangle side a: {self.__side_a}, RightTriangle side b: {self.__side_b} {self.unit} {self.calculate()}')



circle_1 = Circle(4)
circle_2 = Circle(7)
RightTriangle_1 = RightTriangle(5, 7)
RightTriangle_2 = RightTriangle(2, 3)
RightTriangle_3 = RightTriangle(4, 6)
figure_list = [circle_1, circle_2, RightTriangle_1, RightTriangle_3, RightTriangle_2]
for figure in figure_list:
    figure.info()




