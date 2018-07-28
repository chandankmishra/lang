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
import time

SLEEP = 0.1

# Complex Parts


class TC1:
    def run(self):
        print(u"###### In Test 1 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC2:
    def run(self):
        print(u"###### In Test 2 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC3:
    def run(self):
        print(u"###### In Test 3 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


# Facade
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()
