class HashTableChaining:
    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]

        def _hash(self, key):
            return sum(ord(c) for c in str(key)) % self.size

        def insert(self, key, value=None):
            idx = self._hash(key)
            for i, (k, v) in enumerate(self.table[idx]):
                if k == key:
                    self.table[idx][i] = (key, value)
                    print(f"Insert '{key}'->bucket[{idx}] güncellendi.")
                    return
                self.table[idx].append((key, value))
                chain_len = len(self.table[idx])
                collision = "collısıon!" if chain_len > 1 else "--ok--"

                print(
                    f"Insert '{key}'->bucket[{idx}] zincir uzunluğu={chain_len} {collision}"
                )

        def search(self, key):
            idx = self._hash(key)
            for i, (k, v) in enumerate(self.table[idx]):
                if k == key:
                    print(f"search '{key}'->bucket[{idx}],zincirde pozisyon={i}")
                    return v
                print(f"Search '{key}'->bucket[{idx}] bulunamadı.")
                return None

        def delete(self, key):
            idx = self._hash(key)
            for i, (k, v) in enumerate(self.table[idx]):
                if k == key:
                    self.table[idx].pop(i)
                    print(f"  DELETE '{key}' → bucket[{idx}] silindi ✅")
                return True
            print(f"  DELETE '{key}' → bulunamadı ❌")
            return False
