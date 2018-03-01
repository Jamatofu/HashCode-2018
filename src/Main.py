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

class Ride :
    def __init__(self, si, fi, es, lf):
        self.start_inter = si
        self.finish_inter = fi
        self.earliest_start = es
        self.latest_finish = lf


class Map :
    def __init__(self, row, cols, nbVehicles, nbRides, bonus, nbSteps):
        self.bonus = bonus
        self.nbRides = nbRides
        self.cols = cols
        self.row = row
        self.nbVehicles = nbVehicles
        self.nbSteps = nbSteps
        self.rideList = []

    def add_ride(self, ride):
        self.rideList.append(ride)


def startSimulation(file):
    content = readAndStoreFile(file)
    #print(content)
    map = Map(content[0][0], content[0][1], content[0][2], content[0][3], content[0][4], content[0][5])
    for i in range(1,len(content)):
        map.add_ride(Ride(content[i][0], content[i][1], content[i][2], content[i][3]))
    print(map)

if __name__ == '__main__':
    startSimulation('a_example.in')
    #startSimulation('b_should_be_easy.in')
    #startSimulation('c_no_hurry.in')
    #startSimulation('d_metropolis.in')
    #startSimulation('e_high_bonus.in')


