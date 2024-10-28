from pprint import pprint 
import copy

initial = [
    [6,7,3],
    [8,"",5],
    [4,2,1],
]

precision = 10

def printS(state):
    for row in state:
        print(row)

def printSP(path):
    for state in path:
        print("...")
        for row in state:
            print(row)
    
visited = []
nextToVisit = [[0,initial]]

def switch(state, xb, yb, x, y):
    state = copy.deepcopy(state)
    try:
        state[xb][yb] = state[x][y]
    except:
        return None
    state[x][y] = ""
    return state

def findBlankPos(state):
    # print(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == "":
                return (i, j)

def findPos(state, ele):
    # print(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == ele:
                return (i, j)
            
def getNextMoves(path):
    # print(path)
    path = copy.deepcopy(path)
    state = path[-1]

    x,y = findBlankPos(state)

    nextStates = []
    xb, yb = findBlankPos(state)
    # print("curr", printS(state), "xb:", xb, "yb:", yb)
    nextStates.append(switch(state, xb, yb, x+1, y))
    if (x != 0):
        nextStates.append(switch(state, xb, yb, x-1, y))
    nextStates.append(switch(state, xb, yb, x, y+1))
    if (y != 0):
        nextStates.append(switch(state, xb, yb, x, y-1))
    # print("next", nextStates)


    nextStates = [i for i in nextStates if i != None]
    # print("next moves:")
    # printSP(nextStates)
    # print("\n\n")


    # to avoid making a step back, returing to the previous state
    try:
        prevState = path[-2]
        nextStates.remove(prevState)
    except:
        pass
    
    return (nextStates)


getNextMoves(nextToVisit[0])

def heusticFunction(state):
    # print("state", state)
    vals = [1,2,3,4,5,6,7,8,""]
    h = 0
    counter = 0
    for i in state:
        for j in i:
            if j != vals[counter]:
                h +=1        
            counter+=1

    return h

# print(heusticFunction(goal))
solution = None
while (1):

    nextPath = None

    for path in nextToVisit:
        # print(path)
        
        if nextPath == None:
            nextPath = copy.deepcopy(path)
            continue
        elif (heusticFunction(path[-1]) + (path[0] / precision)) < (heusticFunction(nextPath[-1]) + (nextPath[0] / precision)):
            nextPath =  copy.deepcopy(path)

    # printS(nextPath[-1])
    # print("-------")

    if heusticFunction(nextPath[-1]) == 0:
        solution = (nextPath)
        break

    nextToVisit.remove(nextPath)
    visited.append(nextPath[-1])
    # print(nextPath)
    posibleMoves = getNextMoves(nextPath[1:])
    nextPath[0] +=1

    # print("sss")
    # print(posibleMoves)
    for move in posibleMoves:

        if (move not in visited):
            npath = copy.deepcopy(nextPath)
            npath.append(move)
            nextToVisit.append(npath)




def translateToSteps(solution):
    for state in range(len(solution)):
        xb, yb = findBlankPos(solution[state])
        elementInBPostion = solution[state+1][xb][yb]
        elementPrevPostionX, elementPrevPostionY = findPos(solution[state], elementInBPostion)
        
        if (elementPrevPostionX == xb and elementPrevPostionY == yb-1):
            print(elementInBPostion, "Right")
        elif (elementPrevPostionX == xb and elementPrevPostionY == yb+1):
            print(elementInBPostion, "Left")
        elif (elementPrevPostionX == xb+1 and elementPrevPostionY == yb):
            print(elementInBPostion, "Up")
        elif (elementPrevPostionX == xb-1 and elementPrevPostionY == yb):
            print(elementInBPostion, "Down")
        # printS(solution[state])
        if (state == len(solution) -2):
            printS(solution[-1])
            break
        


print(len(solution))

translateToSteps(solution[1:])