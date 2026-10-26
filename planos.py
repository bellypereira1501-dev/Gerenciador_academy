from banco import carregar_dados, salvar_dados


def escolher_plano(nome, plano):

    dados = carregar_dados()


    for aluno in dados['alunos']:

        if aluno['nome'] == nome:

            aluno['plano'] = plano


            if plano == 'Plano Básico':
                aluno['valor'] = '99.90'

            elif plano == 'Plano Prime':
                aluno['valor'] = '129.90'

            elif plano == 'Plano Premium':
                aluno['valor'] = '199.90'


    salvar_dados(dados)