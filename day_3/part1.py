currX = 0
currY = 0
visited = {}
bestDistance = 9999999999

def applyStep(step, numWire):
    global currX
    global currY
    direction = step[0]
    distance = int(step[1:])
    for i in range(distance):
        if direction == "U":
            currY += 1
        elif direction == "L":
            currX -= 1
        elif direction == "R":
            currX += 1
        elif direction == "D":
            currY -= 1

        checkInterseption(numWire)



def checkInterseption(numWire):
    global visited
    global bestDistance

    if not currX in visited:
        visited.update({currX : {}})

    if currY in visited[currX] and visited[currX][currY] != numWire:
        bestDistance = min(bestDistance, abs(currX) + abs(currY))

    visited[currX].update({currY : numWire})


def calcNearestInterseption(wire1, wire2):
    global currX
    global currY

    for step in wire1:
        applyStep(step, 1)

    currX = 0
    currY = 0

    for step in wire2:
        applyStep(step, 2)



file = open("input.txt", "r")
wireString1 = file.readline()
wire1 = [x.strip() for x in wireString1.split(',')]
wireString2 = file.readline()
wire2 = [x.strip() for x in wireString2.split(',')]

calcNearestInterseption(wire1, wire2)

print(bestDistance)