## Hacı Hasan Savan 1901042704
##-----------------------Q1-----------------------####

#A)

visited = []


def IsItVisited(node):
    for i in visited:
        if node in visited:
            return True
    return False


def GetParents(child,graph):
    parents = []
    for key, value in graph.items():
        if child in value:
            parents.append(key)
    return parents

def DoYouHaveNonVisitedParent(node,graph):
    parents = GetParents(node,graph)
    for i in parents:
        if IsItVisited(i) == False:
            return i
    return None

def GetChild(parent,graph):
    children = []
    for key, value in graph.items():
        res = parent in key 
        if res == True:
            valList = list(value)
            return valList[0]
    return None

def FindStartPoint(graph):
    startPoints = []
    for key, value in graph.items():
        if GetParents(key,graph) == []:
            startPoints.append(key)
    return startPoints


## just give a node
def Fun(node,graph):
    res = DoYouHaveNonVisitedParent(node,graph) 
    if res != None:
        Fun(res,graph)
    else:
        visited.append(node)
        if GetChild(node,graph) == None:
            return
        child = GetChild(node,graph) 
        if  child != None:
            Fun(child,graph)
        else:
            return 

def DFSTopologicalSorting(start,graph):
    startPoints = FindStartPoint(graph)
    Fun(startPoints[0],graph)   



##------------------------------------------------####

#B)
def TopologicalSorting(graph):
    inDegreeCounts = {node: 0 for node in graph}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            inDegreeCounts[neighbor] += 1

    queue = [node for node, count in inDegreeCounts.items() if count == 0]

    sortedNodes = []

    while queue:
        node = queue.pop(0)

        sortedNodes.append(node)

        for neighbor in graph[node]:
            inDegreeCounts[neighbor] -= 1

            if inDegreeCounts[neighbor] == 0:
                queue.append(neighbor)

    if len(sortedNodes) < len(graph):
        return None
    else:
        return sortedNodes



##-----------------------Q2-----------------------####
def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        x = pow(a, n / 2)
        return x * x
    else:
        x = pow(a, (n - 1) / 2)
        return a * x * x



##-----------------------Q3-----------------------####
def SolveSudoku(grid):
    def CanPlace(row, col, num):
        for i in range(9):
            if grid[row][i] == num:
                return False

        for i in range(9):
            if grid[i][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if grid[i][j] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if CanPlace(row, col, num):
                            grid[row][col] = num
                            if solve():
                                return True
                            grid[row][col] = 0
                    return False
        return True

    if solve():
        return grid
    else:
        return None

def printGrid(grid):
    for i in grid:
        for j in i:
            print(j,end=" ")
        print()

def test(grid,solution):
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if grid[i][j] != solution[i][j]:
                print("Solutions are not equal")
                return
    print("\nSolutions are equal") 


##----------------------------------------------####


### DRIVER FUNCTION:

def Driver():
    print()


    ##graph = {"CSE102": {"CSE241"},"CSE240":{"CSE241"},"CSE241": {"CSE222","CSE422"}, "CSE222": {"CSE321"}, "CSE211":{"CSE321"},"CSE321":{"CSE422"}}
    graph2 = {"CSE102": {"CSE241"},"CSE241": {"CSE222"}, "CSE222": {"CSE321"}, "CSE211":{"CSE321"}, "CSE321":{"CSE422"}}
    # Q1 (A) - Test
    print("Q1(A) Test:")
    DFSTopologicalSorting("CSE241",graph2)
    print()
    print(visited)
    print("---------------------")
    # Q1 (B) - Test
    graph3 = {'CSE102': ['CSE241'],'CSE241': ['CSE222',],'CSE222': ['CSE321'],'CSE211': ['CSE321'],'CSE321': ['CSE422'],'CSE422': [] }
    print("Q1(B) Test:")
    sortedNodes = TopologicalSorting(graph3)
    print(sortedNodes)
    print("---------------------")
    ##-----------------------Q2 - DRIVER -----------------------####
    print("Q2 Test:")
    print("2^10:",pow(2, 10))
    print()
    print("---------------------")

    ##-----------------------Q3 - DRIVER -----------------------####

    grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    print("Q3 Test:\n")

    solutionGrid = SolveSudoku(grid)
    printGrid(solutionGrid)
    test(solutionGrid,solution)
    print()

Driver()