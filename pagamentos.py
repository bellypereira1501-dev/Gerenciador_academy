from dados import Pagamentos

def registrar_pagamento(nome, plano, valor, forma):
    pagamento = {
        'Nome': nome,
        'Plano': plano,
        'Valor': valor,
        'Forma': forma
    }

    Pagamentos.append(pagamento)

def mostrar_pagamentos():
    lista = ''

    for pagamento in Pagamentos:
        lista += f'''
Aluno: {pagamento['Nome']}
Plano: {pagamento['Plano']}
Valor: R$ {pagamento['Valor']}
Forma de pagamento: {pagamento['Forma']}
-------------------------
'''

    return lista