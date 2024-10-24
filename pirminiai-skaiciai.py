#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def arPirminis(skaicius):
    if skaicius == 1:
        return False
    
    for i in range(2, int(skaicius/2)+1):
        if skaicius % i == 0:  # Condition inside loop
            return False
    return True

def ieskotiPirminiu(pradzia, pabaiga):
    for i in range(pradzia, pabaiga+1):
        if(arPirminis(i)):
            print(i)
def paversti_i_skaiciu(ivestis):
    skaicius = None
    try:
        skaicius = int(ivestis)
    except ValueError:
        pass
    return skaicius

def patikrinti_skaiciu(skaicius):
    verte = paversti_i_skaiciu(skaicius)
    if verte == None:
        print("Privaloma ivesti sveikaji skaiciu.")
        sys.exit(0)
    if verte < 1:
        print("Privalome ivesti teigiama skaiciu.")
        sys.exit(0)
    return verte

print("Pirminiu skaiciu paieskos programa.")
print("Programa ras pirminius skaicius nurodytame intervale. ")
skaicius_nuo = input("Iveskite intervalo pradzia: ")
skaicius_nuo = patikrinti_skaiciu(skaicius_nuo)
skaicius_iki = input("Iveskite intervalo pabaiga: ")
skaicius_iki = patikrinti_skaiciu(skaicius_iki)
print("Pirminiu skaiciu ieskoma intervale [" + str(skaicius_nuo) + ", " + str(skaicius_iki) + "]")
if skaicius_nuo > skaicius_iki:
    tmp = skaicius_nuo
    skaicius_nuo = skaicius_iki
    skaicius_iki = tmp
ieskotiPirminiu(skaicius_nuo, skaicius_iki)