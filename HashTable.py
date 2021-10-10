

class HashTable:
    def __init__(self, hash_size, elems=[]):
        self._hash_size = hash_size
        self._A = 0.6180339887
        self._array = [[] for _ in range(hash_size)]

        for elem in elems:
            self.insert(elem)

    def __str__(self):
        return str(self._array)

    def _hash(self, key):
        return int(self._hash_size * ((hash(key) * self._A) % 1))

    def insert(self, key):
        index = self._hash(key)
        self._array[index].append(key)

    def search(self, key):
        index = self._hash(key)
        if self._array[index] is not None:
            for j in range(len(self._array[index])):
                if key == self._array[index][j]:
                    return j
            else:
                return None

    def get(self, key):
        if self.search(key) is not None:
            return key
        else:
            return None

    def delete(self, key):
        index = self._hash(key)
        if self.search(key) is not None:
            self._array[index].remove(key)


