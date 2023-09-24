def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

print(multiplo_de_5(int(input("Digite um número: "))))

numero = int(input("Digite um número inteiro: "))
print(f"True" if numero % 5 == 0 else f"False")