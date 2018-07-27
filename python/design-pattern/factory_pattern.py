from abc import ABC, abstractmethod

# interface


class ShapeInterface(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Circle(ShapeInterface):
    def draw(self):
        print ("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print ("Square.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()
        assert 0, 'Could not find shape {}!'.format(type)


f = ShapeFactory()
s = f.getShape('square')
s.draw()
s = f.getShape('circle')
s.draw()
# s = f.getShape('triangle')
# s.draw()
