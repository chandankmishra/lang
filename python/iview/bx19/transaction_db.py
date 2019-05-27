class DBStack:
    def __init__(self):
        self.operations = []

    def log_command(self, command, *args):
        self.operations.append((command, args))

    def rollback(self):
        for op in reversed(self.operations):
            func, args = op[0], op[1]
            func(*args)


class TransactionDb:
    def __init__(self):
        self._blocks = []
        self._value_count = {}
        self._cache = {}

    def _update_value_count(self, value, count):
        self._value_count[value] = self._value_count.get(value, 0) + count

    # Basic API's
    def key_exist(self, key):
        if key in self._cache:
            return True
        return False

    def update_transaction(self, key, new_value, logAction):
        key_exist = self.key_exist(key)
        if len(self._blocks) > 0 and logAction:
            block = self._blocks[-1]
            if key_exist:
                block.log_command(self.set, key, self.get(key), False)
            else:
                block.log_command(self.delete, key, False)

    def set(self, key, new_value, logAction=True):
        self.update_transaction(key, new_value, logAction)

        key_exist = self.key_exist(key)
        if key_exist:
            old_value = self.get(key)
            if old_value != new_value:
                self._update_value_count(old_value, -1)
                self._update_value_count(new_value, 1)
        else:
            self._update_value_count(new_value, 1)

        self._cache[key] = new_value
        # print ("set", key, new_value, self._value_count, self._cache)

    def get(self, key):
        # print (key, self._cache)
        return self._cache[key]

    def delete(self, key, logAction=True):
        if self.key_exist(key):
            if len(self._blocks) > 0 and logAction:
                self._blocks[-1].log_command(self.set, key, self.get(key), False)

            value = self.get(key)
            self._update_value_count(value, -1)
            del self._cache[key]

    def count(self, value):
        if value not in self._value_count:
            self._value_count[value] = 0
            return 0
        # print ("count", value, self._value_count)
        return self._value_count[value]

    # Transactions related API's
    def transaction_not_exist(self):
        return len(self._blocks) == 0

    def begin(self):
        """Start a new transaction."""
        self._blocks.append(DBStack())

    def rollback_commands(self):
        """ Rollback commands """
        self._blocks.pop().rollback()

    def commit(self):
        """ Reset the transaction stack """
        self._blocks = []
