Test = "Hello World!"
Categoria = ""

print("Teste: ", Test)

Altura_string = input("insira sua altura (EM METROS): ")  # Em metros
Peso_string = input ("insira seu peso (EM KILOGRAMAS): ") # Em Quilogramas


# Tente converter para float, caso erro, fechar programa
# Trocar ',' por '.'
try:
    Altura = float(Altura_string.replace(",", "."))
    Peso = float(Peso_string.replace(",", "."))
except:
    print("Erro: Só valores numéricos são aceitos!")
    quit()

# Verificação de valores inimaginaveis para campos peso e altura
if Altura <= 0 or Altura >= 5:
    print("Erro: Os valores de altura devem estar entre 0 e 4.99")
    quit()
elif Peso <= 0  or Peso >= 500:
    printf("Erro: Os valores de peso devem estar entre 0 e 499.99")
    quit()


# Calculo do IMC
IMC = (Peso / Altura ** 2)

# Categoria
if IMC > 35:
    categoria = "Maior que 35 → Obesidade Extrema"
elif IMC >= 30:
    categoria = "Maior ou igual que 30 → Obesidade"
elif IMC >= 25:
    categoria = "Entre 25 e 29,99 → Excesso de Peso"
elif IMC >= 18.5:
    categoria = "Entre 18,5 e 24,99 → Peso Normal"
else:
    categoria = "Menor que 18,5 → Baixo Peso"

# teste = ("Categorias de IMC: Menor que 18,5 → Baixo Peso 18,5 – 24,9 → Peso Normal 25 – 29,9 → Excesso de Peso Maior que 30 → Obesidade Maior que 35 → Obesidade Extrema")

# Resultado. Float configurado para mostrar 2 casas decimais.
print("=-"*10)
print(f"IMC: {IMC:.2f}\nCategorias de IMC: {categoria}")
print("=-"*10)

