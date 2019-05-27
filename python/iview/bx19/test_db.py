from mem_db import MemDb


def testcases1():
    print("============= TESTCASE 1 =============")
    memDb = MemDb()
    memDb.set('a', 10)
    # memDb.set('a', 20)
    print ("GET", memDb.get('a'))
    memDb.delete('a')
    print ("GET", memDb.get('a'))


def testcases2():
    print("============= TESTCASE 2 =============")
    memDb = MemDb()
    memDb.set('a', 10)
    memDb.set('b', 10)
    print (memDb.count(10))
    print (memDb.count(20))
    memDb.delete('a')
    print (memDb.count(10))
    memDb.set('b', 30)
    print (memDb.count(10))


def testcases30():
    print("============= TESTCASE 30 =============")
    memDb = MemDb()
    memDb.begin()
    memDb.set('a', 10)
    print ("GET", memDb.get('a'))
    memDb.rollback()
    print ("GET", memDb.get('a'))


def testcases3():
    print("============= TESTCASE 3 =============")
    memDb = MemDb()
    memDb.begin()
    memDb.set('a', 10)
    print ("GET", memDb.get('a'))
    memDb.begin()
    memDb.set('a', 20)
    print ("GET", memDb.get('a'))
    memDb.rollback()
    print ("GET", memDb.get('a'))
    memDb.rollback()
    print ("GET", memDb.get('a'))


def testcases4():
    print("============= TESTCASE 4 =============")
    memDb = MemDb()
    memDb.begin()
    memDb.set('a', 30)
    # print ("GET", memDb.get('a'))
    memDb.begin()
    memDb.set('a', 40)
    memDb.commit()
    print ("GET", memDb.get('a'))
    print(memDb.rollback())


def main():

    # testcases1()

    # testcases2()

    # testcases3()

    testcases4()

    # testcases30()


main()
