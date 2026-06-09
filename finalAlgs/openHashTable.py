class OpenHashTable:
    def __init__(self,m):
        self.m=m
        self.table=[[] for _ in range(m)]

    def _hash(self,key):
        return hash(key)%self.m
    
    def insert(self,key,value):
        idx=self._hash(key)
        for i,(k,v) in enumerate(self.table[idx]):
            if k==key:
                self.table[idx][i]=(key,value)
                return
            
        self.table[idx].append((key,value))

    def search(self,key):
        idx=self._hash(key)
        for k, v in self.table[idx]:
            if k==key:
                return v
        return None
    
    def delete(self,key):
        idx=self._hash(key)
        self.table[idx]=[(k,v) for k,v in self.table[idx] if k !=key]