# This script is to find distance between cities
import csv
import math
from math import pi, log, tan


#loop through csv list
def find (city):

    csv_file = csv.reader(open('cc.csv', "rt"), delimiter=",")
    for row in csv_file:
     if city == row[1]:
        finding = row
        #print(finding)
        return finding

def distance (list1, list2):
    x1 = list1[0]
    x2 = list2[0]
    #sq = ((x1 - x2)**2)
    sq = ((list1[0] - list2[0])**2 + (list1[1] - list2[1])**2)
    #print(sq)
    range = math.sqrt(sq)
    return range

def conversion (cityrow):
    mapWidth = 30030.000000
    mapHeight = 30015.000000

    latitude = float(cityrow[2])
    longitude = float(cityrow[3])

    x = (longitude + 180) * (mapWidth / 360)
    #print("x", x)

    latRad = latitude * pi / 180

    mercN = log(tan((pi / 4) + (latRad / 2)))

    y = (mapHeight / 2) - (mapWidth * mercN / (2 * pi))

    #print ("y", y)
    list = [x, y]
    return list

def main():
    city = input('Enter first city\n')
    city2 = input('Enter second city\n')
    city3 = input('Enter third city\n')

    Imp_SI = int(input("Would you like output in miles Input (1) or kilometers Input (2)"))
    while Imp_SI != 1 and Imp_SI != 2:
       Imp_SI = int(input("Please enter correct choice in miles Input (1) or kilometers Input (2)"))

    cityrow = find(city)
    cityrow2 = find(city2)
    cityrow3 = find(city3)
    #print(cityrow3)

    listcity1 = conversion(cityrow)
    # print(listcity1)
    listcity2 = conversion(cityrow2)
    # print(listcity2)
    listcity3 = conversion(cityrow3)
    #print(listcity3)

    range = distance(listcity1, listcity2)
    if Imp_SI == 2:
        print("This is distance between", city, "and", city2, "in kilometers:", ("%.2f" % range))
    else:
        print("This is distance between", city, "and", city2, "in miles:", ("%.2f" % (range/1.609)))

    range = distance(listcity2, listcity3)

    if Imp_SI == 2:
      print("This is distance between", city2, "and", city3, "in kilometers:", ("%.2f" % range))
    elif Imp_SI == 1:
      print("This is distance between cities", "in miles:", ("%.2f" % (range/1.609)))

if __name__ == "__main__":
    main()