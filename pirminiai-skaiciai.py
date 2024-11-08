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
    pirminiai = 0
    for i in range(pradzia, pabaiga + 1):
        if arPirminis(i):
            pirminiai += 1
            print(f"{pirminiai:2}.{' ' * (6 - len(str(i)))}{i}")


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
        print("Klaida 1. Privaloma ivesti sveikaji skaiciu.")
        sys.exit(0)
    if verte < 1:
        print("Klaida 2. Privalome ivesti teigiama skaiciu.")
        sys.exit(0)
    if verte > 1000000:
        print("Klaida 3. Skaiciaus rezis negali buti didesnis uz 1000000")
        sys.exit(0)
    return verte

def tikrinti_intervala(pradzia, pabaiga):
    if pabaiga - pradzia > 100:
        print("Klaida 4. Per didelis intervalas, turi buti maziau ar lygu 100.")
        return -1
    return 1

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


if tikrinti_intervala(skaicius_nuo, skaicius_iki) == 1:
    print("Pirminiu skaiciu ieskoma intervale [" + str(skaicius_nuo) + ", " + str(skaicius_iki) + "]")
    ieskotiPirminiu(skaicius_nuo, skaicius_iki)

    


