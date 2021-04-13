class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self):
        self.size = 0
        self.numBucket = 5
        self.bucket = [None] * self.numBucket
    
    def size(self):
        return self.size

    def getBucketIndex(self, key):
        hashcode = 0
        currentCofficient = 1
        for i in range(len(key)-1, -1, -1):
            hashcode += ord(key[i])*currentCofficient
            hashcode %= self.numBucket
            currentCofficient *= 37
            currentCofficient %= self.numBucket

        return hashcode % self.numBucket

    def getValue(self, key):
        bucketIndex = self.getBucketIndex(key)
        head = self.bucket[bucketIndex]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def rehash(self):
        temp = self.bucket
        newBucketsize = 2 * self.numBucket
        self.bucket = [None] * newBucketsize
        self.numBucket = newBucketsize
        self.size = 0
        for eachObj in temp:
            head = eachObj
            while head:
                key = head.key
                value = head.value
                self.insert(key, value)
                head = head.next
    

    def insert(self, key, value):
        bucketIndex = self.getBucketIndex(key)
        head = self.bucket[bucketIndex]
        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.bucket[bucketIndex]
        newNode = MapNode(key, value)
        newNode.next = head
        self.bucket[bucketIndex] = newNode
        self.size += 1
        loadFactor = self.size/self.numBucket
        if loadFactor > 0.7:
            self.rehash()

    def remove(self, key):
        bucketIndex = self.getBucketIndex(key)
        head = self.bucket[bucketIndex]
        prev = None
        while head:
            if head.key == key:
                if prev is None:
                    self.bucket[bucketIndex] = head.next
                else:
                    prev = head.next
                self.size -= 1           
                return head.value
            prev = head
            head = head.next
        return -1
        


ob = HashMap()
for i in range(29):
    ob.insert(str(i), "abc")

for i in range(32):
    print(ob.getValue(str(i)))

