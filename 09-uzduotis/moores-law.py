import matplotlib.pyplot

f = open("transistor-counts.csv", "r", encoding="utf8")

eiluciu_skaicius = 0
procesoriuPavadinimai = []
tranzistoriuSkaiciai = []
isleidimoMetai = []

#surenkami duomenys
for eilute in f:
    eilute = eilute.strip().split(",")
    if eiluciu_skaicius > 0:
        procesoriuPavadinimai.append(eilute[0])
        tranzistoriuSkaiciai.append(int(eilute[1]))
        isleidimoMetai.append(int(eilute[2]))
        print(eilute)
    eiluciu_skaicius += 1

#Braizome grafika
matplotlib.pyplot.scatter(isleidimoMetai, tranzistoriuSkaiciai, label = "Tranzistoriu skaičius")
