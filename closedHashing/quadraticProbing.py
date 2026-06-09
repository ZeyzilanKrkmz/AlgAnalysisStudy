EMPTY=None
DELETED="__DELETED__"
class QuadraticProbing:
    def __init__(self,m):
        self.m=m
        self.table=[EMPTY]*m
        self.size=0

    def _hash(self,key):
        return hash(key)%self.m
    
    def _probe(self,key,i):
        return (self._hash(key)+i*i)%self.m
    
    def insert(self,key,value):
        if self.size/self.m>=0.5:
            self._rehash()

        i=0
        first_deleted=None

        while i<self.m:
            idx=self._probe(key,i)

            if self.table[idx] is EMPTY:
                slot=first_deleted if first_deleted is not None else idx
                self.table[slot]=(key,value)
                self.size+=1
                return
            
            if self.table[idx]==DELETED:
                if first_deleted is None:
                    first_deleted=idx
                elif self.table[idx][0]==key:
                    self.table[idx]=(key,value)
                    return
                i+=1

            if first_deleted is not None:
                self.table[first_deleted]=(key,value)
                self.size+=1
            else:
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
                if self.table[idx] is EMPTY:
                    return False
                if self.table[idx]!=DELETED and self.table[idx][0]==key:
                    self.table[idx]=DELETED
                    self.size-=1
                    return True
                i+=1
            return False
        

        def _rehash(self):
            old=self.table
            new_m=self.m*2+1
            while not self._is_prime(new_m):
                new_m+=2
            self.m=new_m
            self.table=[EMPTY]*self.m
            self.size=0
            for slot in old:
                if slot is not EMPTY and slot !=DELETED:
                    self.insert(slot[0],slot[1])

        def _is_prime(self,n):
            if n<2: return False
            return all(n%i !=0 for i in range(2,int(n**0.5)+1))