#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import argparse

def writeInFile(exitFile, data):
    with open(exitFile, 'w') as f:
        f.write(data)


parser = argparse.ArgumentParser()
parser.add_argument(
    "--showUi",
    type=str,
    default="true",
    help="Valeur booléenne spécifiant si la partie graphique devrait être affichée ou non. \nValeur par défaut : faux."
)

# récupère les arguments dans un objet (appelable comme un struct en C)
args = parser.parse_args()

if args.showUi:

    # create an object that inputs data randomly
    if args.showUi == "true":
        print("Starting project with UI!")
        exit(0)

    else:
        print("Starting project with no UI!")
        exit(0)