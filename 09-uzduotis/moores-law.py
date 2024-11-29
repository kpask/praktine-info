import matplotlib.pyplot

f = open("transistor-counts.csv", "r", encoding="utf8")

eiluciu_skaicius = 0
procesoriuPavadinimai = []
tranzistoriuSkaiciai = []
isleidimoMetai = []

# 1. surenkami duomenys
for eilute in f:
    # 1.1 Suskaldome CSV stulpelius, remiantis kableliu
    eilute = eilute.strip().split(",")
    if eiluciu_skaicius > 0:
        procesoriuPavadinimai.append(eilute[0])
        tranzistoriuSkaiciai.append(int(eilute[1]))
        isleidimoMetai.append(int(eilute[2]))
        print(eilute)
    eiluciu_skaicius += 1

# 2. Deklaruojami kintamieji Mūro prognozei atvaizduoti
prognoze = []
metu_intervalas = range(min(isleidimoMetai), max(isleidimoMetai)+1)

# 2.1 Pagal Mūro dėsnį paskaičiuojame kiekvienų metų prognozę
n_0 = min(tranzistoriuSkaiciai)
for y_i in metu_intervalas:
    prognoze.append(n_0 * 2 ** ((y_i - min(isleidimoMetai)) / 2))

# 3. Braižome grafiką
matplotlib.pyplot.scatter(isleidimoMetai, tranzistoriuSkaiciai, label="Sukurti procesoriai")
matplotlib.pyplot.plot(metu_intervalas, prognoze, label="Prognozė", color="gray", linestyle="--")
matplotlib.pyplot.title("Mūro dėsnis")
matplotlib.pyplot.xlabel("Išleidimo metai")
matplotlib.pyplot.ylabel("Tranzistoriu skaičius")
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.legend()

# 4. Išsaugojame grafiką įvairiais formatais
matplotlib.pyplot.savefig("muro_desnis.pdf", format="pdf")
matplotlib.pyplot.savefig("muro_desnis.png", format="png")
matplotlib.pyplot.savefig("muro_desnis.svg", format="svg")

matplotlib.pyplot.show()
