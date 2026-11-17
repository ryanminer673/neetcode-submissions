class LRUCache:

    def __init__(self, capacity: int):
        #initiate a data strct to store used values that is size capacity
        # use a dict for O(1) lookup
        # if we add data and its at capacity we removed least
        # recently used data
        # i need a queue 
        # 

        self.capacity = capacity
        self.data = {}
        

    def get(self, key: int) -> int:
        # look up in the lru cash for the key 
        # 

        if key in self.data:

            #update teh order of the key in the data 
            val = self.data.pop(key)
            self.data[key] = val

            return self.data[key]
        else:
            return -1


# 2 1 4
    def put(self, key: int, value: int) -> None:

        if key in self.data:
            self.data.pop(key)
            self.data[key] = value
        else:
            self.data[key] = value

        if len(self.data) > self.capacity:
            #delete the leats recently used data (first value from my dict)
            first_key = next(iter(self.data))
            first_value = self.data.pop(first_key)
        
