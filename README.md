# Atv2PythonDataframe
 
## Fazendo essa atividade junto da outra que abordava sobre series, eu fiz exemplos de ambos e percebi que a principal diferença é:

### Serie:
Series se tratam de **colunas isoladas**, **sozinhas**. Possui uma dimensão apenas e é usado para quando você quer "um pedaço" de uma tabela inteira, uma lista de dados apenas
> uma analogia boa é que a Serie é uma "gaveta" de um armário (Dataframe)
```
Índice | Valor
-------|--------
0      | valor1
1      | valor2
2      | valor3
3      | valor4
```
### Dataframe:
Enquanto a Serie é uma coluna, o Dataframe é a **tabela inteira**, todas as colunas do Excel, por exemplo, estão aqui, junto de seus valores. Ele é usado quando você tem várias listas relacionadas
> Igualmente dito antes, enquanto a serie é uma "gaveta", o Dataframe é o armário todo
```
Índice | Nome     | Idade | Cidade     | Profissão
-------|----------|-------|------------|------------
A      | João     | 25    | São Paulo  | Engenheiro
B      | Maria    | 30    | Rio de Janeiro | Médica
C      | Pedro    | 22    | Belo Horizonte | Estudante
```

## Exemplo prático:

### Series (Atividade 1):
```
SleepToken = ["Telomeres", "Caramel", "The summoning", "Emergence", "Take me back to eden", "Democles", "Rain", "Granite", "Gethsemane", "Alkaline"]
NumeroViewEmMilhao = [15, 191, 323, 172, 202, 35, 110, 200, 12, 95]

serie = pd.Series(SleepToken)
serie2 = pd.Series(NumeroViewEmMilhao)
```

### Dataframe (Atividade 2):
```
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
```
