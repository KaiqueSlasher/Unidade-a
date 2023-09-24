def lista_de_compras():
    lista = []
    fruta = input("Digite o nome da fruta que deseja comprar ou 'sair' para sair: ").lower()
    while fruta != "sair":
        lista.append(fruta)
        print(lista)
        fruta = input("Digite o nome da fruta que deseja comprar ou 'sair' para sair: ").lower()
    print(f"Lista de compras: \n {lista}")
    return lista

lista_de_compras()