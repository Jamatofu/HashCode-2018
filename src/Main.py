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


def startSimulation(file):
    readAndStoreFile('input/' + file)



if __name__ == '__main__':
    startSimulation('a_example.in')
    startSimulation('b_sould_be_easy.in')
    startSimulation('c_no_hurry.in')
    startSimulation('d_metropolis.in')
    startSimulation('e_high_bonus.in')



writeInFile('output.txt', 'a')
courses = []
courses = readAndStoreFile('input.txt')
print(courses)