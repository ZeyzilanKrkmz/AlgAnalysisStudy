EMPTY=None
DELETED="__DELETED__"

class LinearProbing:
    def __init__(self,m=11):
        self.m=m
        self.table=[EMPTY]*m
        self.size=0



    def _hash(self,key):
        return hash(key)%self.m
    
    def _probe(self,key,i):
        return (self._hash(key)+i)%self.m
    
    def insert(self,key,value):
        if self.size/self.m>=0.7:
            self._rehash()


        i=0
        while i<self.m:
            idx=self._probe(key,i)

            if self.table[idx] is EMPTY or self.table[idx]==DELETED:
                self.table[idx]=(key,value)
                self.size+=1
                return
            
            if self.table[idx][0]==key:
                self.table[idx]=(key,value)
                return
            i+=1
        raise Exception("hash table is full")
    

    def search(self,key):
        i=0
        while i<self.m:
            idx=self._probe(key,i)

            if self.table[idx] is EMPTY:
                return None
            if self.table[idx]!=DELETED and self.table[idx][0]==key:
                return self.table[idx][1]
            
            i+=1
        return None
    
    def delete(self,key):
        i=0
        while i<self.m:
            idx=self._probe(key,i)

            if self.table[idx]is EMPTY:
                return False
            
            if self.table[idx]!=DELETED and self.table[idx][0] == key:
                self.table[idx]=DELETED
                self.size-=1
                return True
            i+=1
        return False
    
    def _rehash(self):
        old=self.table
        self.m=self.m*2+1
        self.table=[EMPTY]*self.m
        self.size=0
        for slot in old:

            if slot is not EMPTY and slot !=DELETED:
                self.insert(slot[0],slot[1])