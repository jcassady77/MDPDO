
time t = 0
obstacles = [ [ [ ]]]
graph = [[[]]]
start = []
goal = []




def distance(pos1, pos2):
    return sqrt((pos1[0]-pos2[0]) + (pos1[1]-pos2[1]))

def cost(pos, time):
    obs = obstacles[time]
    sum = 0
    for agent in obs:
        sum += 1/sqrt((pos[0]-agent[0])+(pos[1]-agent[1]))
    return sum

def Astar(pos, time):
    #Of the nodes within range r, which one has lowest heuristic + travel cost
    range = 10
    possibleMoves = []
    for node in graph[time]:
        dist = distance(pos, node)
        if dist < range && dist != 0:
            possibleMoves.append(node)
    if len(possibleMoves) == 0:
        print("No moves within range")

    lowestCost = 9999
    lowestCostNode = []
    for node in possibleMoves:
        #problem with this is that large distances outweigh cost of being close to obstacles
        cost = (distance(node, goal)+distance(pos, node)+cost(pos, time))
        if cost < lowestCost:
            lowestCost = cost
            lowestCostNode = node

    

searching = True

while(searching):

