"""
What is this pattern about?
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This kind of abstraction is seen in many real life situations. For
example, we can turn on a computer by just pressing a button, but in
fact there are many procedures and operations done when that happens
(e.g., loading programs from disk to memory). In this case, the button
serves as an unified interface to all the underlying procedures to
turn on a computer.
"""

# Complex Parts


class Engine:
    def __init__(self):
        self.spin = 0

    def start(self, spin):
        self.spin = min(spin, 3000)


class StarterMotor:
    def __init__(self):
        self.spin = 0

    def start(self, charge):
        if charge > 50:
            self.spin = 2500


class Battery:
    def __init__(self):
        self.charge = 0


# Facade
class Car:
    def __init__(self):
        self.battery = Battery()
        self.starter = StarterMotor()
        self.engine = Engine()

    def turn_key(self):
        self.starter.start(self.battery.charge)
        self.engine.start(self.starter.spin)
        if self.engine.spin > 0:
            print ("Engine Started :)")
        else:
            print ("Engine not Started :(")

    def jump(self):
        self.battery.charge = 100
        print ('Car Jump Started !')



# Client
if __name__ == '__main__':
    car = Car()
    car.turn_key()
    car.jump()
    car.turn_key()
"""
Output
Engine not Started :(
Car Jump Started !
Engine Started :)
"""
