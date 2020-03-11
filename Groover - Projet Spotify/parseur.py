# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:53:22 2020

@author: Charles

recupere les donnes du csv et les place dans tab

chaque element de tab est une liste de deux element contenant :
    en premiere pos :
        l'url de l'artiste
    en deuximee pos:
        band id
"""

#import numpy as np
import csv as csv

fichier = open("GROOVER_SPOTIFY.csv", "r", newline = '', encoding='utf-8')
lecture = csv.reader(fichier)
urls = []
ids = []

for ligne in lecture:
    ligne[0] = ligne[0].split(" ")
    l = []

    for x in ligne:
        if x != '':
            l.append(x)
    urls.append(l[0])
    ids.append(l[1])

ids = ids[1:]
urls = urls[1:]