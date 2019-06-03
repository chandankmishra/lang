from transaction_db import TransactionDb


class MemDb:
    def __init__(self):
        self._db_store = TransactionDb()

    # Basic API's
    def set(self, key, value):
        self._db_store.set(key, value)

    def get(self, key):
        if self._db_store.key_exist(key):
            return self._db_store.get(key)
        return 'NULL'

    def delete(self, key):
        self._db_store.delete(key)

    def count(self, value):
        return self._db_store.count(value)

    # Transactions related API's
    def begin(self):
        pass

    def rollback(self):
        pass

    def commit(self):
        pass


def testcases1():
    memDb = MemDb()
    memDb.set('a', 10)
    memDb.set('a', 20)
    print ("GET", memDb.get('a'))
    memDb.delete('a')
    print ("GET", memDb.get('a'))


def testcases2():
    memDb = MemDb()
    memDb.set('a', 10)
    memDb.set('b', 10)
    print (memDb.count(10))
    print (memDb.count(20))
    memDb.delete('a')
    print (memDb.count(10))
    memDb.set('b', 30)
    print (memDb.count(10))


def main():
    # testcases1()

    testcases2()


main()
