taxas_de_cambio = {
    ('USD', 'EUR'): 0.85,
    ('EUR', 'USD'): 1.18,
    ('USD', 'JPY'): 110.24,
    ('JPY', 'USD'): 0.0091,
    ('EUR', 'JPY'): 130.16,
    ('JPY', 'EUR'): 0.0077,
}

def converter_moeda(valor, moeda_origem, moeda_destino, taxa_cambio):
    if (moeda_origem, moeda_destino) in taxas_de_cambio:
        valor_convertido = valor * taxa_cambio
        return valor_convertido
    else:
        print("Taxa de câmbio não encontrada.")
        return None

moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

if (moeda_origem, moeda_destino) in taxas_de_cambio:
    taxa_cambio = taxas_de_cambio[(moeda_origem, moeda_destino)]
    valor = float(input(f"Digite o valor em {moeda_origem}: "))

    resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxa_cambio)
    if resultado is not None:
        print(f"{valor} {moeda_origem} equivalem a {resultado} {moeda_destino}")
else:
    print("As moedas selecionadas não são suportadas.")