import customtkinter as ctk

from alunos import cadastrar_aluno, listar_alunos
from planos import escolher_plano
from pagamentos import registrar_pagamento, mostrar_pagamentos
from banco import carregar_dados

ctk.set_appearance_mode('light')

app = ctk.CTk()
app.title('AUREA GYM')
app.geometry('1000x600')

rosa = '#D81B60'
roxo = '#6A1B9A'
lilas = '#AB47BC'
fundo = '#FAF7F2'

principal = ctk.CTkFrame(
    app,
    fg_color=fundo
)

principal.pack(
    expand=True,
    fill='both'
)

lado_esquerdo = ctk.CTkFrame(
    principal,
    width=250,
    fg_color=fundo
)

lado_esquerdo.pack(
    side='left',
    fill='y'
)

titulo = ctk.CTkLabel(
    lado_esquerdo,
    text='AUREA\nGYM',
    font=('Arial', 55, 'bold'),
    text_color=roxo
)

titulo.pack(
    pady=120
)

titulo.pack(
    pady=80
)

linha = ctk.CTkFrame(
    principal,
    width=2,
    fg_color='black'
)

linha.pack(
    side='left',
    fill='y'
)

area = ctk.CTkFrame(
    principal,
    fg_color=fundo
)

area.pack(
    side='left',
    expand=True,
    fill='both'
)

categorias = ctk.CTkFrame(
    area,
    fg_color=fundo
)

categorias.pack(
    expand=True
)

def tela_inicio():

    limpar_tela()

    botoes = [
        ('Alunos', tela_alunos),
        ('Planos', tela_planos),
        ('Pagamentos', tela_pagamentos),
        ('Lista de alunos', tela_lista)
    ]

    espaco = ctk.CTkLabel(
        area,
        text=''
    )

    espaco.pack(
        pady=80
    )

    for texto, comando in botoes:

        botao = ctk.CTkButton(
            area,
            text=texto,
            width=350,
            height=65,
            corner_radius=20,
            fg_color=rosa,
            hover_color=lilas,
            font=('Arial',20),
            command=comando
        )

        botao.pack(
            pady=12
        )

def limpar_tela():
    for item in area.winfo_children():
        item.destroy()

def botao_voltar():
    voltar = ctk.CTkButton(
        area,
        text='← Voltar',
        width=120,
        fg_color=roxo,
        hover_color=lilas,
        command=tela_inicio
    )

    voltar.pack(
        pady=20
    )

def tela_alunos():

    limpar_tela()

    botao_voltar()

    titulo = ctk.CTkLabel(
        area,
        text='Cadastro de aluno',
        font=('Arial',25,'bold'),
        text_color=roxo
    )

    titulo.pack(pady=20)

    nome = ctk.CTkEntry(
        area,
        placeholder_text='Nome do aluno',
        width=300
    )

    nome.pack(pady=10)


    idade = ctk.CTkEntry(
        area,
        placeholder_text='Idade',
        width=300
    )

    idade.pack(pady=10)

    telefone = ctk.CTkEntry(
        area,
        placeholder_text='Telefone',
        width=300
    )

    telefone.pack(pady=10)

    def salvar():

        cadastrar_aluno(
            nome.get(),
            idade.get(),
            telefone.get()
        )

        tela_planos()


    botao = ctk.CTkButton(
        area,
        text='Cadastrar aluno',
        fg_color=rosa,
        hover_color=lilas,
        command=salvar
    )

    botao.pack(
        pady=20
    )

    def salvar():
        cadastrar_aluno(
            nome.get(),
            idade.get(),
            telefone.get()
        )

def botao_voltar():
    voltar = ctk.CTkButton(
        area,
        text='← Voltar',
        width=120,
        fg_color=roxo,
        hover_color=lilas,
        command=tela_inicio
    )

    voltar.pack(
        pady=20
    )

def tela_planos():
    limpar_tela()

    titulo = ctk.CTkLabel(
        area,
        text='Planos AUREA GYM',
        font=('Arial', 28, 'bold'),
        text_color=roxo
    )

    titulo.pack(pady=20)

    container = ctk.CTkFrame(
        area,
        fg_color='#F3E5F5'
    )

    container.pack(pady=20)

    planos = [
        {
            'nome': 'Plano Básico',
            'valor': 'R$ 99,90/mês',
            'beneficios': '• Musculação\n• Aeróbico\n• Sem matrícula'
        },

        {
            'nome': 'Plano Prime',
            'valor': 'R$ 129,90/mês',
            'beneficios': '• Musculação\n• Treino personalizado\n• Aulas coletivas'
        },

        {
            'nome': 'Plano Premium',
            'valor': 'R$ 199,90/mês',
            'beneficios': '• Todas unidades\n• Acompanhamento mensal\n• Desconto produtos'
        }
    ]

    nome_aluno = ctk.CTkEntry(
        area,
        placeholder_text='Nome do aluno',
        width=300
    )

    nome_aluno.pack(pady=10)

    for plano in planos:

        card = ctk.CTkFrame(
            container,
            width=220,
            height=250,
            corner_radius=15,
            fg_color='white'
        )

        card.pack(
            side='left',
            padx=15,
            pady=10
        )


        nome = ctk.CTkLabel(
            card,
            text=plano['nome'],
            font=('Arial',20,'bold'),
            text_color=roxo
        )

        nome.pack(pady=15)


        valor = ctk.CTkLabel(
            card,
            text=plano['valor'],
            font=('Arial',18),
            text_color=rosa
        )

        valor.pack()


        beneficios = ctk.CTkLabel(
            card,
            text=plano['beneficios'],
            font=('Arial',14),
            text_color=roxo
        )

        beneficios.pack(pady=20)


        def escolher(p=plano['nome']):

            escolher_plano(
                nome_aluno.get(),
                p
            )

            tela_pagamentos()


        botao = ctk.CTkButton(
            card,
            text='Escolher plano',
            fg_color=rosa,
            hover_color=lilas,
            command=escolher
        )

        botao.pack(pady=10)

def tela_pagamentos():

    limpar_tela()

    titulo = ctk.CTkLabel(
        area,
        text='Registrar pagamento',
        font=('Arial', 25),
        text_color=roxo
    )

    titulo.pack(pady=20)

    nome = ctk.CTkEntry(
        area,
        placeholder_text='Nome do aluno'
    )

    nome.pack(pady=10)

    plano = ctk.CTkEntry(
        area,
        placeholder_text='Plano escolhido'
    )

    plano.pack(pady=10)

    valor = ctk.CTkEntry(
        area,
        placeholder_text='Valor do plano'
    )

    valor.pack(pady=10)

    forma = ctk.CTkComboBox(
        area,
        values=[
            'Pix',
            'Cartão',
            'Dinheiro'
        ]
    )

    forma.pack(pady=10)

    def buscar_aluno(event):

        dados = carregar_dados()

        for aluno in dados['alunos']:

            if aluno['nome'].lower() == nome.get().lower():

                plano.delete(0, 'end')
                plano.insert(0, aluno['plano'])

                valor.delete(0, 'end')
                valor.insert(0, aluno['valor'])

                break


    nome.bind(
        '<Return>',
        buscar_aluno
    )


    def salvar_pagamento():

        registrar_pagamento(
            nome.get(),
            plano.get(),
            valor.get(),
            forma.get()
        )

        tela_lista()


    botao = ctk.CTkButton(
        area,
        text='Registrar pagamento',
        fg_color=rosa,
        hover_color=lilas,
        command=salvar_pagamento
    )

    botao.pack(
        pady=20
    )

def tela_lista():

    limpar_tela()

    titulo = ctk.CTkLabel(
        area,
        text='Alunos cadastrados',
        font=('Arial',25,'bold'),
        text_color=roxo
    )

    titulo.pack(pady=20)

    lista = listar_alunos()

    texto = ctk.CTkLabel(
        area,
        text=lista,
        font=('Arial',16),
        text_color=roxo
    )

    texto.pack(pady=20)

    botao_voltar()

tela_inicio()

app.mainloop()