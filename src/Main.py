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
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    return content

class Vehicle:
    def __init__(self):
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

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


class Map :
    def __init__(self, row, cols, nbVehicles, nbRides, bonus, nbSteps, name):
        self.bonus = bonus
        self.nbRides = nbRides
        self.cols = cols
        self.row = row
        self.vehiclesList = []
        for i in nbVehicles:
            self.vehiclesList.append(Vehicle())
        self.nbSteps = nbSteps
        self.rideList = []
        self.name = name

    def solveCourse(self):
        for course in self.rideList:
            self.vehiclesList[0].addCourse(course)

    def add_ride(self, ride):
        self.rideList.append(ride)

    def printResult(self):
        content = ""
        for car in self.vehiclesList:
            content += car.printCourse() + '\n'
        content = content[:-1]
        writeInFile(self.name, content)



def startSimulation(file):
    content = readAndStoreFile(file)
    map = Map(content[0][0], content[0][1], content[0][2], content[0][3], content[0][4], content[0][5], file)
    for i in range(1, len(content)):
        map.add_ride(Ride(i-1, content[i][0], content[i][1], content[i][2], content[i][3], content[i][4], content[i][5]))
    map.solveCourse()
    map.printResult()

if __name__ == '__main__':
    startSimulation('a_example.in')
    startSimulation('b_should_be_easy.in')
    startSimulation('c_no_hurry.in')
    startSimulation('d_metropolis.in')
    startSimulation('e_high_bonus.in')


