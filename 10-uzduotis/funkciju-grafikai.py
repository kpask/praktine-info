import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-5, 5, 50001)
F1  = 1/(np.cbrt(X))
F2 = 1/X
F3 = 1/(X*X)

plt.plot(X, F1, linestyle="-", label=r"$f_1(x)=\frac{1}{\sqrt[3]{x}}$")
plt.plot(X, F2, linestyle="--", color="orange", label=r"$f_2(x)=\frac{1}{x}$")
plt.plot(X, F3, linestyle=":", color="green", label=r"$f_3(x)=\frac{1}{x^2}$")
plt.ylim(-15, 15)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Hiperboles")
plt.legend()
plt.show()
plt.close()