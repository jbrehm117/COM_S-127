# Joseph Brehm       10.18.23
# Lab Week 9         Exercise 2

import math


def calculateDistance(x_list: list, y_list: list, x: float, y: float):
    return [math.sqrt((x - cur_x) ** 2 + (y - cur_y) ** 2) for (cur_x, cur_y) in zip(x_list, y_list)]


def main():
    listName = []
    listX = []
    listY = []
    cityInput = None
    while cityInput != '*':
        cityInput = input("Input a name of a city (* to quit): ")
        if cityInput != '*':
            listName.append(cityInput)
            x = float(input("Input Coordinate for (x): "))
            y = float(input("Input Coordinate for (y): "))
            listX.append(x)
            listY.append(y)
        else:
            myx = float(input("Input your coordinate for (x): "))
            myy = float(input("Input your coordinate for (y): "))
    listDistances = calculateDistance(listX, listY, myx, myy)
    minDistance = math.inf
    closestCity = ''
    for (city, distance) in zip(listName, listDistances):
        if distance < minDistance:
            minDistance = distance
            closestCity = city
    print(listName)
    print(listDistances)
    print("The closest city to you ({0}, {1}) is {2}. The distance is {3}".format(
        myx, myy, closestCity, minDistance))


main()
