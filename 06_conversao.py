# entrada de dados
nome = input("informe o nome: ")
idade = input("informe sua idade: ")
altura = input("Informe sua altura: ").replace(',','.')

# conversão de tipos
idade = int(idade)
altura = float(altura)

# saida de dados
print(f"Nome: {nome}. Tipo: {type(nome)}")
print(f"Idade: {idade}. Tipo: {type(idade)}")
print(f"Altura: {altura} metros. Tipo {type(altura)}")