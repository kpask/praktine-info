from collections import Counter

def pasalintiSkyrybosZenklus(eil):
    # Pravalome kablelius, kitus simbolius
    eil = eil.replace(',', ' ')
    eil = eil.replace('-', ' ')
    eil = eil.replace('–', ' ')
    eil = eil.replace('—', ' ')
    eil = eil.replace('„', ' ')
    eil = eil.replace('“', ' ')
    eil = eil.replace('.', ' ')
    eil = eil.replace('!', ' ')
    eil = eil.replace(':', ' ')
    eil = eil.replace('?', ' ')
    eil = eil.replace('(', ' ')
    eil = eil.replace(';', ' ')
    eil = eil.replace(')', ' ')
    return eil

#Atidaromas tekstinis failas, skaitom eilutes, kiekviena eilutes žodį dedame i masyva zodziai
with open("Metai.txt", "r", encoding="utf8") as f:
    zodziai = []
    for eilute in f:
        eilute = pasalintiSkyrybosZenklus(eilute)
        eilute = eilute.strip().split(" ")
        zodziai += eilute

print(zodziai)
