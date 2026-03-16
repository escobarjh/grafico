import matplotlib.pyplot as plt

plt.style.use("dark_background")

criptos = ["Bitcoin", "Ethereum", "Solana"]

crescimento = [40, 90, 250]

plt.figure(figsize=(8,5))

plt.bar(criptos, crescimento, color=["gold","cyan","purple"])

plt.title("🚀 Crescimento das Criptomoedas (%)")
plt.xlabel("Criptomoedas")
plt.ylabel("Crescimento (%)")

plt.grid(axis="y", alpha=0.3)

plt.show()