import tkinter as tk

def adicionar_contato():
    # Implemente a lógica para adicionar um contato
    pass

def pesquisar_contato():
    # Implemente a lógica para pesquisar um contato
    pass

def editar_contato():
    # Implemente a lógica para editar um contato
    pass

def excluir_contato():
    # Implemente a lógica para excluir um contato
    pass

# Crie a janela principal
root = tk.Tk()
root.title("Agenda Telefônica")

# Crie botões para as operações
add_button = tk.Button(root, text="Adicionar Contato", command=adicionar_contato)
search_button = tk.Button(root, text="Pesquisar Contato", command=pesquisar_contato)
edit_button = tk.Button(root, text="Editar Contato", command=editar_contato)
delete_button = tk.Button(root, text="Excluir Contato", command=excluir_contato)

# Posicione os botões na janela
add_button.pack()
search_button.pack()
edit_button.pack()
delete_button.pack()

# Inicie a interface gráfica
root.mainloop()

import pickle

# Salvar agenda em um arquivo
def salvar_agenda(agenda, arquivo):
    with open(arquivo, 'wb') as f:
        pickle.dump(agenda, f)

# Carregar agenda de um arquivo
def carregar_agenda(arquivo):
    try:
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Exemplo de uso
agenda = []
arquivo_agenda = 'agenda.pkl'

# Carregar agenda previamente salva
agenda = carregar_agenda(arquivo_agenda)

# Adicionar, editar, excluir contatos e atualizar a agenda

# Salvar a agenda de volta no arquivo
salvar_agenda(agenda, arquivo_agenda)
