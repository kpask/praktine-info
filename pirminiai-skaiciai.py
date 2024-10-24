#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

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
if skaicius_nuo > skaicius_iki:
    tmp = skaicius_nuo
    skaicius_nuo = skaicius_iki
    skaicius_iki = tmp
print("Pirminiu skaiciu ieskoma intervale [" + str(skaicius_nuo) + ", " + str(skaicius_iki) + "]")

