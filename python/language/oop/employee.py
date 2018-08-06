import sys

class Employee:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('chandan', "mishra", 36)

print(emp1.email)
print(emp1.fullname())

print(sys.version)
