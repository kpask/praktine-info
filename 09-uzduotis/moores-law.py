import matplotlib.pyplot

f = open("transistor-counts.csv", "r", encoding="utf8")

eiluciu_skaicius = 0
procesoriuPavadinimai = []
tranzistoriuSkaiciai = []
isleidimoMetai = []

# 1. surenkami duomenys
for eilute in f:
    # 1.1 Suskaldome stulpelius pagal kableli
    eilute = eilute.strip().split(",")
    if eiluciu_skaicius > 0:
        procesoriuPavadinimai.append(eilute[0])
        tranzistoriuSkaiciai.append(int(eilute[1]))
        isleidimoMetai.append(int(eilute[2]))
        print(eilute)
    eiluciu_skaicius += 1

prognoze = []
metu_intervalas = range(min(isleidimoMetai), max(isleidimoMetai)+1)

n_0 = min(tranzistoriuSkaiciai)
for y_i in range(min(isleidimoMetai), max(isleidimoMetai)+1):
    prognoze.append(n_0 * 2 ** ((y_i - min(isleidimoMetai))/2))
# 2. Įtraukiame prognozes kiekvieniems metams

print(len(isleidimoMetai))
print(len(prognoze))

# 3. Braizome grafika
matplotlib.pyplot.scatter(isleidimoMetai, tranzistoriuSkaiciai, label = "Tranzistoriu skaičius")
matplotlib.pyplot.plot(metu_intervalas, prognoze, label="Prognozė (Mūro dėsnis)", color="gray", linestyle="--")
matplotlib.pyplot.title("Mūro dėsnis")
matplotlib.pyplot.xlabel("Išleidimo metai")
matplotlib.pyplot.ylabel("Tranzistoriu skaičius")
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.show()