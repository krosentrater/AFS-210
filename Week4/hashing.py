class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return (key % self.size)

    def rehash(self, key):
        return (key // self.size)
    
    # Could not get this to work. My thoughts behind this were to iterate through self.data, find the indexes where data is None, return that index as a "hash value". 
    # Then set the self.slots[rerehashvalue] = key and self.slots[rerehashvalue] = data. When I tried to implement this I failed and couldn't figure it out. 
    # Not necessary to go over this but if you have the time it bugs me that I couldn't get it and I was wondering what I was doing incorrectly. 
    def rerehash(self, key):
        for item in enumerate(self.data, start = 0):
            if (item[1] is None) :
                return item[0]

    def put(self, key, data):
        
        for item in enumerate(self.data, start = 0):
            hv = self.hashfunction(key)
            rhv = self.rehash(key)
            if (item[1] is None) and (item[0] == hv):
                self.slots[hv] = key
                self.data[hv] = data
            elif (item[0] == hv) and (item[1] is not None) and (hv != rhv):
                self.slots[rhv] = key
                self.data[rhv] = data
            elif (item[0] == rhv) and (item[1] is not None):
                return

    def get(self, key):
        for item in enumerate(self.data, start = 0):
            hv = self.hashfunction(key)
            rhv = self.rehash(key)
            if (item[0] == rhv) or (item[0] == hv):
                return item[1]

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)
        

H = HashTable()
# Store remaining input data
H[69] = 'A' # 9  
H[66] = 'B' # 6
H[80] = 'C' # 0
H[35] = 'D' # 5
H[18] = 'E' # 8
H[52] = 'F' # 2
H[89] = 'G' # 9  REHASH 8
H[70] = 'H' # 0  REHASH 7 
H[12] = 'I' # 2  REHASH 1

# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H[52])