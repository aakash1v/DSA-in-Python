class MyHash:
    def __init__(self,b):
        self.Bucket = b
        self.table = [[] for i in range(b)]

    def insert(self,x):
        i = x % self.Bucket
        self.table[i].append(x)
    
    def remove(self,x):
        i = x%self.Bucket
        if x in self.table[i] :
            return self.table[i].remove(x)
    def search(self,x):
        i = x%self.Bucket
        return x in self.table[i]
    
    def __str__(self) -> str:
        return str(self.table)

#Driver code.
h = MyHash(7)
h.insert(23)
h.insert(41)
h.insert(4)
print(h.search(4))
print(h)
print('The End')

