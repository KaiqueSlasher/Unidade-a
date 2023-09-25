import os

# Função para exibir a lista de tarefas
def mostrar_tarefas(tarefas):
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
    print()

# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, nova_tarefa):
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida(tarefas, numero_tarefa):
    if numero_tarefa >= 1 and numero_tarefa <= len(tarefas):
        tarefa = tarefas[numero_tarefa - 1]
        print(f"Tarefa '{tarefa}' marcada como concluída!")
        tarefas.pop(numero_tarefa - 1)
    else:
        print("Número de tarefa inválido!")

# Função para remover uma tarefa
def remover_tarefa(tarefas, numero_tarefa):
    if numero_tarefa >= 1 and numero_tarefa <= len(tarefas):
        tarefa = tarefas[numero_tarefa - 1]
        print(f"Tarefa '{tarefa}' removida com sucesso!")
        tarefas.pop(numero_tarefa - 1)
    else:
        print("Número de tarefa inválido!")

# Função para salvar a lista de tarefas em um arquivo
def salvar_tarefas_em_arquivo(tarefas, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa}\n")

# Função para carregar a lista de tarefas de um arquivo
def carregar_tarefas_de_arquivo(nome_arquivo):
    tarefas = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                tarefa = linha.strip()
                tarefas.append(tarefa)
    return tarefas

# Nome do arquivo para salvar as tarefas
nome_arquivo = 'tarefas.txt'

# Carregar a lista de tarefas do arquivo (se existir)
tarefas = carregar_tarefas_de_arquivo(nome_arquivo)

while True:
    mostrar_tarefas(tarefas)
    print("Opções:")
    print("1. Adicionar Tarefa")
    print("2. Marcar Tarefa como Concluída")
    print("3. Remover Tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nova_tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefa(tarefas, nova_tarefa)
        salvar_tarefas_em_arquivo(tarefas, nome_arquivo)
    elif opcao == '2':
        numero_tarefa = int(input("Digite o número da tarefa concluída: "))
        marcar_tarefa_concluida(tarefas, numero_tarefa)
        salvar_tarefas_em_arquivo(tarefas, nome_arquivo)
    elif opcao == '3':
        numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
        remover_tarefa(tarefas, numero_tarefa)
        salvar_tarefas_em_arquivo(tarefas, nome_arquivo)
    elif opcao == '4':
        print("Saindo do aplicativo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
