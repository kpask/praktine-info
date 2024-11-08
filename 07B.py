#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def arSveikasis(skaicius):
    if skaicius%1 != 0:
        print("Klaida 1. Ivestas skaicius nera sveikas.")
        sys.exit(0)
    return 1

print("N-tojo laipsnio šaknies traukimo iš skaičiaus programa.")

daugiklis = input("Iveskite daugikli pries sakni (1 jei nera):")
daugiklis = float(daugiklis)
arSveikasis(daugiklis)

laipsnis = input("Iveskite saknies laipsni: ")
laipsnis = float(laipsnis)
arSveikasis(laipsnis)

if(laipsnis < 2):
    print("Klaida 2. Saknies laipsnis negali buti mazesnis uz 2")
    sys.exit(0)

posaknis = input("Iveskite posakni: ")
posaknis = float(posaknis)
arSveikasis(posaknis)

if(posaknis < 0 and laipsnis%2 == 0):
    print("Klaida 3.Posaknis negali buti mazesnis uz 0, jeigu laipsnis lyginis")
    sys.exit(0)
