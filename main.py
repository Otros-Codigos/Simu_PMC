
# Graficos y simulación
# ______________________

import simulation as sim
import matplotlib.pyplot as plt
import statistics as st

# Parametros
# ___________

NUM_VIAJEROS = 50
NUM_USUARIOS = NUM_VIAJEROS*3

NUM_SIMULATIONS = 0
REPORT = True

X = []
Y = []

# Main
# _____

for _ in range(NUM_SIMULATIONS+1):
    try:
        coverture, trips = sim.mip_simulation(REPORT, NUM_VIAJEROS, NUM_USUARIOS, _, NUM_SIMULATIONS)
        X.append(trips)
        Y.append(coverture)
    except:
        _ -= 1

print("\n--------------")
print("    Packa ")
print("--------------\n")
print(f"Número de viajeros promedio: {st.mean(X)}")
print(f"Cobertura promedio: {st.mean(Y)}")
print("----------------------------------------------\n")

fig, ax = plt.subplots()
ax.scatter(X, Y)
plt.xlabel("Número de Viajeros)", size = 16,)
plt.ylabel("% Cubrimiento", size = 16)
plt.title("Packa", fontdict={'family': 'serif', 'color' : 'darkblue', 'weight': 'bold', 'size': 18})
plt.show()

