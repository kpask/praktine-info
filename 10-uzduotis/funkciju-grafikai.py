import matplotlib.pyplot as plt
import numpy as np

# 1. Reikalingi kintamieji, paprastos X reiksmes, x reiksmes sin(x^2), funkciju y reiksmes
X = np.linspace(-5, 5, 50001)
SX = np.linspace(-6, 6, 50001)
F1  = 1/(np.cbrt(X))
F2 = 1/X
F3 = 1/(X*X)
S1 = np.sin(X*X)

# 2. Piesiam grafikus 1/sqrt(x), 1/x, 1/x^2, issaugojam pdf formatu
plt.plot(X, F1, linestyle="-", label=r"$f_1(x)=\frac{1}{\sqrt[3]{x}}$")
plt.plot(X, F2, linestyle="--", color="orange", label=r"$f_2(x)=\frac{1}{x}$")
plt.plot(X, F3, linestyle=":", color="green", label=r"$f_3(x)=\frac{1}{x^2}$")
plt.ylim(-15, 15)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Hiperboles")
plt.legend()
plt.savefig("funk.pdf")
plt.show()
plt.close()

# 3. Atskirai piesiam grafika sin(x^2) ir ji veliau issaugojam pdf formatu
plt.plot(SX, S1, linestyle=":", color="blue", label=r"$f(x)=\sin(x^2)$")
plt.ylim(-1, 1)
plt.xlim(-6, 6)
plt.ylabel("y")
plt.xlabel("x")
plt.title(r"$f(x)=\sin(x^2)$")
plt.savefig("sin.pdf")
plt.show()
plt.close()