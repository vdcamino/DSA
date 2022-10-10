class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, val):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, val)
                found = True
                break

        if not found:
            self.bucket.append((key, val))

    def delete(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]
                break


class MyHashMap:
    def __init__(self):
        self.max = 2069
        self.table = [Bucket() for i in range(self.max)]

    def update(self, key, val):
        hashKey = key % self.max
        self.table[hashKey].update(key, val)

    def get(self, key):
        hashKey = key % self.max
        return self.table[hashKey].get(key)

    def delete(self, key):
        hashKey = key % self.max
        self.table[hashKey].delete(key)
