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
#Sukuriam kintamuosius ilgiausiui žodžiui ir filtruotiems žodžiams
ilgiausias = ""
atfiltruotiZodziai = []

#Filtruojame visų žodžių masyvą
for zodis in zodziai:
    zodis = zodis.lower()
    #Jeigu žodis nėra tuščias ir susideda tik iš raidžių, dedame jį į mūsų filtsuotų žodžių masyvą
    if len(zodis) > 0 and zodis.isalpha():
        atfiltruotiZodziai.append(zodis)
        #Tuo pačiu patikriname ar žodis yra ilgesnis už kolkas rastą
        if len(zodis) > len(ilgiausias):
            ilgiausias = zodis

#Žodžių kiekis patampa tuple zodis : kiekis
zodziuKiekis = Counter(atfiltruotiZodziai)
#naudojame most_common, kuris paema 100 dažniausiai pasikartojusių žodžių iš zodžiųKiekis, tuple
zodziaiDazniausi = zodziuKiekis.most_common(100)

print("Ilgiausias žodis: " + ilgiausias)
print("100 dažniausiai pasikartojančių žodžių:")
#Spausdiname dažniausius žodžius, per nutylėjima zodis patampa tuple pirmoji dalis, kiekis patampa antroji dalis - kiekis
for zodis, kiekis in zodziaiDazniausi:
    print(f"{zodis:8}: {kiekis:3}")
