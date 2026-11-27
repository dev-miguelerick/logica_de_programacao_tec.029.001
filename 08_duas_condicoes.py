# entrada de dados
massa = float(input("Informe seu peso: ").replace(",","."))
altura = float(input("Informe sua altura: ").replace(",","."))

# estrutura de decisão
if massa <=140 and altura >=1.15:
    print(f"Entrada do usuário permitida. ")
else:
    print(f"Entrada do usuário negada. ")