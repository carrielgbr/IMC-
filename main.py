Test = "Hello World!"

print("Teste: ", Test)

Altura = float (input ("insira sua altura (EM METROS COM . PONTO)"))# Em metros
Peso = float (input ("insira seu pelo"))       # Em Quilogramas

# Calculo do IMC
IMC = (Peso / Altura ** 2)

teste = ("Categorias de IMC: Menor que 18,5 → Baixo Peso 18,5 – 24,9 → Peso Normal 25 – 29,9 → Excesso de Peso Maior que 30 → Obesidade Maior que 35 → Obesidade Extrema")

# Resultado. Float configurado para mostrar 2 casas decimais.

print(f"IMC: {IMC:.2f}\n"  + teste)
