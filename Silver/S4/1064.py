import math

def findSlope(firstCoordinate : list[2], secondCoordinate : list[2]) -> float:
    if secondCoordinate[0] == firstCoordinate[0]:
        return float('inf')
    return (secondCoordinate[1]-firstCoordinate[1])/(secondCoordinate[0]-firstCoordinate[0])

def findDistance(firstCoordinate : list[2], secondCoordinate : list[2]) -> float:
    return math.sqrt((secondCoordinate[0]-firstCoordinate[0])**2 + (secondCoordinate[1]-firstCoordinate[1])**2)

def main():
    coordinate = list(map(int, input().split())) # 좌표 저장 (Xa, Ya, Xb, Yb, Xc, Yc)
    coordinates = []
    distances = []

    for i in range(3):
        coordinates.append(coordinate[2*i:2*i+2])

    if findSlope(coordinates[0], coordinates[1]) == findSlope(coordinates[1], coordinates[2]):
        print(-1.0)
        return 0

    for j in range(3):
        distances.append(findDistance(coordinates[j],coordinates[(j+1)%3]))
    distances.sort()
    print(2*((distances[1]+distances[2])-(distances[0]+distances[1])))
    return 0

if __name__ == '__main__':
    main()