import matplotlib.pyplot as plt

plt.style.use("dark_background")

meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]

bitcoin = [35000,38000,42000,45000,47000,50000]
ethereum = [2000,2100,2300,2600,3000,3400]
solana = [40,60,90,120,150,200]

plt.figure(figsize=(10,6))

plt.plot(meses, bitcoin, label="Bitcoin", linewidth=3, color="gold")
plt.plot(meses, ethereum, label="Ethereum", linewidth=3, color="cyan")
plt.plot(meses, solana, label="Solana", linewidth=3, color="purple")

plt.title("🚀 Evolução das Criptomoedas")
plt.xlabel("Meses")
plt.ylabel("Preço em USD")

plt.legend()
plt.grid(alpha=0.3)

plt.show()