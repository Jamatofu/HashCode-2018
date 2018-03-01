#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import argparse

def writeInFile(exitFile, data):
    with open(exitFile, 'w') as f:
        f.write(data)


parser = argparse.ArgumentParser()
parser.add_argument(
    "a",
    type=str,
)

# récupère les arguments dans un objet (appelable comme un struct en C)
args = parser.parse_args()
print(args.a)

writeInFile('output.txt', args.a)