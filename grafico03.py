import matplotlib.pyplot as plt

plt.style.use("dark_background")

criptos = ["Bitcoin", "Ethereum", "Solana"]

investimento = [400, 350, 250]

cores = ["gold","cyan","purple"]

plt.figure(figsize=(6,6))

plt.pie(investimento,
        labels=criptos,
        colors=cores,
        autopct="%1.1f%%")

plt.title("💰 Distribuição do Portfólio Cripto")

plt.show()