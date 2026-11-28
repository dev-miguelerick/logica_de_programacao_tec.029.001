# TODO: Crie um programa que receba do usuário o nome, a massa e a altura, e calcule seu IMC (Indice de Massa Coporal). Após mostrar o IMC, o programa deve informar de acordo com o valor do seu IMC>
# -IMC < 18.5: "Usuário está abaixo do peso"
# -IMC < 25: "Usuário etá acima do peso"
# -IMC < 30: "Usuário está acima do peso"
# -IMC < 35: "Usuário está obeso"
# -IMC < 40: "Usuário está com obesidade nível 2"
# -Se não estiver com nenhim dos casos acima:
# "Usuário está com obesidade morbita"
# NOTE: imc = massa/(altura**2)

# entrada de dados
nome = input("Informe seu nome: ").strip().title()
massa = float(input("Informe seu peso: ").replace(",","."))
altura = float(input("Informe sua altura: ").replace(",","."))

# processamento de dados
imc = massa/(altura**2)
print(f"IMC: {imc}")
if imc <= 18.5:
    print("Usuário está abaixo do peso")
elif imc < 25:
    print("Usuário está acima do peso")
elif imc < 30:
    print("Usuário está acima do peso")
elif imc < 35:
    print("Usuário está obeso")
elif imc < 40:
    print("Usuário está com obesidade nível 2")
else:
    print("Usuário está com obesidade morbita")