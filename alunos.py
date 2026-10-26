from banco import carregar_dados, salvar_dados


def cadastrar_aluno(nome, idade, telefone):

    dados = carregar_dados()

    aluno = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone,
        'plano': '',
        'valor': ''
    }

    dados['alunos'].append(aluno)

    salvar_dados(dados)


def listar_alunos():

    dados = carregar_dados()

    lista = ''

    for aluno in dados['alunos']:

        lista += (
            f"Nome: {aluno['nome']}\n"
            f"Idade: {aluno['idade']}\n"
            f"Telefone: {aluno['telefone']}\n"
            f"Plano: {aluno['plano']}\n"
            f"Valor: {aluno['valor']}\n"
            '-------------------\n'
        )

    return lista