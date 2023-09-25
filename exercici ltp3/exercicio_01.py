from datetime import datetime

def calcular_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    else:
        return "Capricórnio"

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

data_atual = datetime.now()

idade = data_atual.year - ano_nascimento

mes_nascimento = int(input("Digite o mês de nascimento (1 a 12): "))
dia_nascimento = int(input("Digite o dia de nascimento: "))

signo = calcular_signo(dia_nascimento, mes_nascimento)

print(f"Sua idade é: {idade} anos")
print(f"Seu signo do zodíaco é: {signo}")