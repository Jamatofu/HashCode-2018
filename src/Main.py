#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import argparse

def writeInFile(exitFile, data):
    with open('/output/' + exitFile, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "a",
        type=str,
    )



    # récupère les arguments dans un objet (appelable comme un struct en C)
    args = parser.parse_args()
    print(args.a)

    writeInFile('output.txt', args.a)