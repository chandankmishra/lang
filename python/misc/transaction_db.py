class TransactionDb:
    def __init__(self):
        self._value_count = {}
        self._cache = {}

    def _update_value_count(self, value, count):
        self._value_count[value] = self._value_count.get(value, 0) + count

    # Basic API's
    def key_exist(self, key):
        if key in self._cache:
            return True
        return False

    def set(self, key, new_value):
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

    def delete(self, key):
        if self.key_exist(key):
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
    def begin(self):
        pass

    def rollback(self):
        pass

    def commit(self):
        pass
