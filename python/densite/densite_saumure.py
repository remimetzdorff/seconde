import matplotlib.pyplot as plt

Cm  = [0, 31, 62, 96, 130, 166, 204, 243, 283, 311]
rho = [1.000,1.020,1.041,1.063,1.086,1.109,1.132,1.156,1.180,1.197]

plt.plot(Cm, rho, color="yellow")

plt.xlabel("Concentration massique en sel")
plt.ylabel("Masse volumique (kg/L)")
plt.title("Le titre")

plt.grid()
plt.show()