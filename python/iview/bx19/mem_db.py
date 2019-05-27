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
        self._db_store.begin()

    def rollback(self):
        if self._db_store.transaction_not_exist():
            return 'NO TRANSACTION'
        else:
            self._db_store.rollback_commands()

    def commit(self):
        self._db_store.commit()
