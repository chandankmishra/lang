from abc import ABC, abstractmethod

# Abstract shape classes


class Shape2DInterface(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Shape3DInterface(ABC):
    @abstractmethod
    def build(self):
        raise NotImplementedError

# Concreate shape classes


class Circle(Shape2DInterface):
    def draw(self):
        print ("Circle.draw")


class Squre(Shape2DInterface):
    def draw(self):
        print ("Squre.draw")


class Sphere(Shape3DInterface):
    def build(self):
        print ("Sphere.build")


class Cube(Shape3DInterface):
    def build(self):
        print ("Cube.build")


# Abstract shape factory
class ShapeFactoryInterface(ABC):
    def create(sides):
        raise NotImplementedError

# Concreate shape factories


class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def create(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Squre()
        assert 0, "Bad 2D Shape"


class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def create(sides):
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, "Bad 3D Shape"


f2 = Shape2DFactory()
s2 = f2.create(1)
s2.draw()


f3 = Shape3DFactory()
s3 = f3.create(1)
s3.build()
