import random

def Q1(i, j, points, path):
	if i == len(points)-1 and j == len(points[0])-1:
		return points[i][j], path
	
	pathh = []
	maxp = float('-inf')
	for mi, mj in [(i, j+1), (i+1, j)]:
		if mi < len(points) and mj < len(points[0]):
			newp, npathh = Q1(mi, mj, points, path + [(mi, mj)])
			if newp > maxp:
				pathh = npathh
				maxp = newp
	
	return maxp + points[i][j], pathh
##-----------------------------------------------------------------------
##-----------------------------------------------------------------------

def FindMedian(arr):
	if len(arr) % 2 == 1:
		return helper(arr, (len(arr) + 1) // 2)
	else:
		median1 = helper(arr, len(arr) // 2)
		median2 = helper(arr, len(arr) // 2 + 1)
		return (median1 + median2) / 2

def helper(arr, k): #selection sort
    if not arr:
        return 0

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        if i == k - 1:
            return arr[i]
##-------------------------------------------------------------
##-----------------------------------------------------------------------
## Q3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
  
    def add(self, data):
        nnode = Node(data)
        if self.head is None:
            self.head = nnode
            nnode.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = nnode
            nnode.next = self.head

    def Q3_A(self):
        if self.head is None:
            return None
        curr = self.head
        while curr.next != curr:
            curr.next = curr.next.next
            curr = curr.next
        return curr.data

    def Q3_B(self):
        if self.head is None:
            return None

        if self.head.next == self.head:
            return self.head.data

        f = self.head.next
        s = self.head
        size = 1

        while f.next != self.head:
            f = f.next.next
            s = s.next
            size *= 2

        if f.next == self.head:
            return s.data
        else:
            return self.FindMid(s, size//2)

    def FindMid(self, start, size):
        curr = start
        for _ in range(size):
            curr = curr.next
        if curr.next == self.head:
            return curr.data
        return self.FindMid(curr, size//2)


def testQ1():
    points = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(random.randint(1, 10))
        points.append(row)
    print("2D Map:", points)
    maxp, pathh = Q1(0, 0, points, [(0, 0)])
    print("Points: ",maxp)
    print("Route: ",pathh)
    print("------------------------------\n")



def testQ2():
    ##array = [random.randint(1, 10)]
    rn = random.randint(1, 10)
    array = [random.randint(1, 20) for _ in range(rn)]
    print("Array: ",array)
    print("Median: ",FindMedian(array))
    print("--------------------------------\n")


def testQ3_A():
    rn = random.randint(1, 10)
    Nodes = []
    for i in range(1, rn):
        Nodes.append('P{}'.format(i))
    testList = CircularLinkedList()
    for player in Nodes:
        testList.add(player)
    res = testList.Q3_B()
    print("Nodes (A): ",Nodes, end="  -->  ")
    print("res:" ,res)

def testQ3_B():
    rn = random.randint(1, 10)
    Nodes = []
    for i in range(1, rn):
        Nodes.append('P{}'.format(i))
    testList = CircularLinkedList()
    for player in Nodes:
        testList.add(player)
    res = testList.Q3_A()
    print("Nodes: (B)",Nodes, end="  -->  ")
    print("res:" ,res)


def Test():
    testQ1()
    testQ2()
    testQ3_A()
    testQ3_B()


Test()