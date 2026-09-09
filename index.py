import pandas as pd

metal_gear_rising = ["Jetstream sam", "Raiden", "mistral", "Armstrong", "Monsoon", "Blade wolf", "Excelsus", "Rose", "Khansim", "Gekko"]

Asuras_wrath = ["Asura", "deus", "Yasha", "Olga", "Augus", "Wyzen", "Sargei", "Gohma Viltra", "Kalrow", "Chakravartin"]

The_witcher3 = ["Geralt", "Triss", "Yennefer", "Ciri", "Vesemir", "Esker", "Lembert", "Filho da puta jr", "Eredin", "Jaskier Dandelion"]

Cyberpunk2077 = ["V", "Jackie", "Paman", "Judy", "Evelyn", "Yorinobu", "Johnny silverhand", "Adam smasher", "Alt Cunningham", "Mama Welles"]

DezPrimeirosAnosGoty =[2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]

df = pd.DataFrame({
    "metal_gear_rising" : metal_gear_rising,
    "Asuras_wrath" :Asuras_wrath,
    "The_witcher3" :The_witcher3,
    "Cyberpunk2077" :Cyberpunk2077,
    "DezPrimeirosAnosGoty" :DezPrimeirosAnosGoty,
    })

# Index alfabetico

OrdemAlfabetica = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
df.index = OrdemAlfabetica

# Filtro

Primeiros2 = df.head(2)

Ultimos4 = df.tail(4)

# Transformar em dict

dicionario_df = df.to_dict()

# Prints

print(f"{"=" * 60} \nDataFrame: \n{df} \n{"=" * 60}")


df["DezPrimeirosAnosGoty"] = df["DezPrimeirosAnosGoty"] + 1
print(f"\nDataFrame + 1: \n{df} \n{"=" * 60}")

print(f"\nDataFrame primeiros 2: \n{Primeiros2} \n{"=" * 60} \nDataFrame últimos 4: \n{Ultimos4} \n{"=" * 60}")

print(f"\nDataFrame em dicionário: \n{dicionario_df} \n{"=" * 60}")

