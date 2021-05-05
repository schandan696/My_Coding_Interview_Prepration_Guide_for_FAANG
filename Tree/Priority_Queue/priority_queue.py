class Pririty_Queue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return len(self.pq) == 0
    
    def getSize(self):
        return len(self.pq)
    
    def getMin(self):
        if self.pq:
            return self.pq[0]
        return None

    def __maxIndex3(self, arr, i, j, k):
        if arr[i] < arr[j] and arr[i] < arr[k]:
            return i
        elif arr[j] < arr[k] and arr[j] < arr[i]:
            return j
        else:
            return k

    def __hippifiDown(self):
        if len(self.pq) <= 1:
            return
        rootindex = 0
        childIndex1 = (2*rootindex)+1
        childIndex2 = (2*rootindex)+2
        while childIndex1 < len(self.pq):
            if childIndex2 > len(self.pq)-1:
                if self.pq[rootindex] > self.pq[childIndex1]:
                    self.pq[rootindex], self.pq[childIndex1] = self.pq[childIndex1], self.pq[rootindex]
                    return
                # return
            minIndex = self.__maxIndex3(self.pq, rootindex, childIndex1, childIndex2)
            if minIndex != rootindex:
                self.pq[rootindex], self.pq[minIndex] = self.pq[minIndex], self.pq[rootindex] 
                rootindex = minIndex
                childIndex1 = (2*rootindex)+1
                childIndex2 = (2*rootindex)+2
            else:
                break

    def insert(self, data):
        self.pq.append(data)
        
        childIndex = len(self.pq) - 1
        parentIndex = (childIndex -1)//2
        while parentIndex >= 0:
            if self.pq[childIndex] < self.pq[parentIndex]:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
            childIndex = parentIndex
            parentIndex = (childIndex -1)//2
    
    def removeMin(self):
        if self.pq:
            if len(self.pq) == 1:
                val = self.pq[0]
                self.pq.pop()
                return val
            val = self.pq[0]
            ele = self.pq[len(self.pq)-1]
            self.pq.pop()
            self.pq[0] = ele
            self.__hippifiDown()
            return val

pq = Pririty_Queue()
pq.insert(10)
pq.insert(12)
pq.insert(1)
pq.insert(18)
pq.insert(4)
pq.insert(0)
pq.insert(3)
pq.insert(27)
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())
print(pq.pq)
print(pq.removeMin())

