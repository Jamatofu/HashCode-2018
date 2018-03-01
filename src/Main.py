#!/usr/bin/python
# -*- coding: utf-8 -*-
#


def writeInFile(exitFile, data):
    with open('output/' + exitFile, 'w') as f:
        f.write(data)

def readAndStoreFile(inputFile):
    with open('input/' + inputFile, 'r') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    return content



writeInFile('output.txt', 'a')
courses = []
courses = readAndStoreFile('input.txt')
print(courses)