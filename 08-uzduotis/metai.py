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

ilgiausias = ""
atfiltruotiZodziai = []
for zodis in zodziai:
    zodis = zodis.lower()
    if len(zodis) > 0 and zodis.isalpha():
        atfiltruotiZodziai.append(zodis)
        if len(zodis) > len(ilgiausias):
            ilgiausias = zodis

print("ilgiausias žodis: " + ilgiausias)
print(atfiltruotiZodziai)
