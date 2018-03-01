#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import argparse

def writeInFile(exitFile, data):
    with open('output/' + exitFile, 'w') as f:
        f.write(data)

def readAndStoreFile(inputFile):
    with open('input/' + inputFile, 'r') as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    print("content " + str(content[0]))

    return content

class Vehicle:
    def __init__(self):
        self.courses = []
        self.x = 0
        self.y = 0

    def moveTo(self,x,y):
        self.x = x
        self.y = y

    def addCourse(self, course):
        self.courses.append(course)
        self.moveTo(course.to_x, course.to_y)

    def printCourse(self):
        content = str(len(self.courses))
        for c in self.courses:
            content += ' '
            content += str(c.id)
        return content

class Ride :
    def __init__(self, idR, from_x, from_y, to_x, to_y, start, finish):
        self.id = idR
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y
        self.start = start
        self.finish = finish

    def getDistance(self):
        return abs(int(self.from_y) - int(self.to_y)) + abs(int(from_x) - int(self.to_x))

    def isBonus(self, distance):
        return self.start < distance and distance < self.finish


class Map :
    def __init__(self, row, cols, nbVehicles, nbRides, bonus, nbSteps, name):
        self.bonus = bonus
        self.nbRides = nbRides
        self.cols = cols
        self.row = row
        self.vehiclesList = []
        print("nb vec => " + nbVehicles)
        for i in range(0, int(nbVehicles)):
            self.vehiclesList.append(Vehicle())
        self.nbSteps = nbSteps
        self.rideList = []
        self.name = name

    def compute_distance(self, x1, y1, x2, y2):
        return abs(int(y1) - int(y2)) + abs(int(x1) - int(x2))

    def findClosestVehicle(self, x, y):
        vehicle = None
        for v in self.vehiclesList:
            if vehicle is None:
                vehicle = v
            else:
                if (abs(int(v.y) - int(y)) + abs(int(v.x) - int(x))) < (abs(int(vehicle.y) - int(y)) + abs(int(vehicle.x) - int(x))):
                    vehicle = v
        return vehicle

    def findVehicleSimple(self, idRide):
        vehicle = self.vehiclesList[idRide%len(self.vehiclesList)]
        return vehicle

    def findVehicleSmart(self,ride):
        distance = 99999
        vehicle_sel = self.vehiclesList[0]
        for vehicle in self.vehiclesList:
            if self.compute_distance(vehicle.x, vehicle.y, ride.x, ride.y) < distance:
                vehicle_sel = vehicle


    def solveCourse(self):
        for course in self.rideList:
            #self.findClosestVehicle(course.from_x, course.from_y).addCourse(course)

            self.findVehicleSimple(course.id).addCourse(course)

    def add_ride(self, ride):
        self.rideList.append(ride)

    def getBonus(self):
        idCurrentCar = 0
        copyCouse = self.rideList

        for ride in self.rideList:
            distance = ride.getDistance()
            for copy in copyCouse:
                if copy.isBonus():
                    self.vehiclesList[idCurrentCar].addCourse(copy)
                    copyCouse.remove(copy)
                    continue





    def printResult(self):
        content = ""
        for car in self.vehiclesList:
            content += car.printCourse() + '\n'

        content = content[:-1]
        writeInFile(self.name, content)





def startSimulation(file):
    content = readAndStoreFile(file)
    line = content[0].split(' ')
    map = Map(line[0], line[1], line[2], line[3], line[4], line[5], file)
    for i in range(1, len(content)):
        line = content[i].split(' ')
        map.add_ride(Ride(i-1, line[0], line[1], line[2], line[3], line[4], line[5]))
    map.solveCourse()
    map.printResult()

if __name__ == '__main__':
    startSimulation('a_example.in')
    startSimulation('b_should_be_easy.in')
    startSimulation('c_no_hurry.in')
    startSimulation('d_metropolis.in')
    startSimulation('e_high_bonus.in')


