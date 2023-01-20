from functions import *
import produtos
from dados import randint, dt

hoje = f'{dt.now():%d/%m/%Y}'

Itens_Prod = {'X_Burger': 10, 'X_Salada': 15, 'X_Bacon': 15, 'X_Egg': 12, 'X_Calabresa': 12,
              'X_Chicken': 12, 'Fritas': 7, 'Refrigerante': 5}

categorias = {
    'prato do dia': {'Virado à Paulista': 25, 'Dobradinha': 30, 'Bife à Role': 25, 'Feijoada Pq': 60, 'Feijoada Md': 70,
                     'Feijoada Gd': 80, 'Macarrão c/ Frango': 25, 'Filéde Peixe': 25},
    'refeição': {'Prato Executivo': 18, 'Comercial': 20, 'Frango Parmeggiana': 30, 'Contra Parmeggiana': 35},
    'lanches': {'X_Burger': 10, 'X_Salada': 15, 'X_Bacon': 15, 'X_Egg': 12, 'X_Calabresa': 12, 'X_Chicken': 12,
                'Bauru': 6, 'Misto Quente': 7, 'Fritas': 7},
    'porções': {'Batata Frita': 20, 'Mandioca Frita': 20, 'Polenta': 20, 'Calabresa': 25, 'Churrasco': 30},
    'bebidas': {'Refrigerante Ks': 4, 'Refrigerante lata': 5, 'Refrigerante 600ml': 7, 'Suco': 7},
    'cervejas': {'Atarctica 600ml': 10, 'Amstel 600ml': 12, 'Skol 600ml': 10, 'Original 600ml': 12, 'Heineken': 14,
                 'Skol Lata': 5, 'Heineken Lata': 7}}

Itens_Prod.clear()
Itens_Prod.update(categorias['refeição'])
Itens_Prod.update(categorias['lanches'])
total_prod = categorias

Nome_Prod = list(Itens_Prod.keys())
Preco_Prod = list(Itens_Prod.values())
tam_list = len(Itens_Prod)
qtdade = total = [p for p in range(tam_list)]


def show_Price():
    """— > mostra a lista de produtos e preços."""
    listaPreco = [[sg.StatusBar(' LISTA DE PRODUTOS  ', font=['_', 16, 'bold'], justification='c', text_color='red')],
                  [sg.Table(
                      [[prod, f'R$ {prec:2.2f}'] for cat in categorias for prod, prec in categorias[cat].items()],
                      ['      PRODUTO     ', ' PREÇO '], font=['_', 14], justification='l')],
                  [sg.HSep()], [sg.Push(), sg.OK(s=10)]]
    escolha, _ = sg.Window('', listaPreco, disable_close=True).read(close=True)


def Invoices():
    def Fechamento():
        for pos, prod in enumerate(Itens_Prod):
            values['-QTDADE' + prod + '-'] = int(values['-QTDADE' + prod + '-']) if values[
                '-QTDADE' + prod + '-'] else 0
            total[pos] = values['-QTDADE' + prod + '-'] * Itens_Prod[prod]
        print(total)

        Sub_Total = sum(total)
        Imposto = (Sub_Total * .22)
        Valor_total = Sub_Total + Imposto

        for pos, prod in enumerate(Nome_Prod):
            if total[pos]:
                window['-TOT-' + prod + '-'].update(f'R$ {total[pos]:3.2f}')

        window['-SUBTOTAL-'].update(f'R$ {Sub_Total:3.2f}', background_color='yellow')
        window['-TAXA-'].update(f'R$ {Imposto:3.2f}', background_color='yellow')
        window['-TOTAL-'].update(f'R$ {Valor_total:3.2f}', background_color='yellow')

    def Limpa():
        window['-RAND-'].update('')
        for pos, prod in enumerate(Itens_Prod):
            window['-QTDADE' + prod + '-'].update('')
            window['-TOT-' + prod + '-'].update('')
            total[pos] = 0

        Sub_Total = 0
        Imposto = 0
        Valor_total = 0

    #sg.theme('DarkBlack')
    rand = randint(10908, 500876)

    menu_def = [['&Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sai&r']],
                ['&Editar', ['Colar', ['Special', 'Normal', ], 'Desfazer', '&Preços'], ],
                ['&Categorias', ['Refeições', 'Bebidas', 'Poções', 'Cervejas', '&Tabela'], ],
                ['Ajuda', 'Sobre...']]

    topo = [[sg.Menu(menu_def, tearoff=False)],
            [sg.Text(" Software de Gerenciamento de Restaurante ", font=ftTT, expand_x=True,
                     text_color='lime', justification='center', relief=sg.RELIEF_GROOVE, p=(5, 10))],
            [sg.P(), sg.T("Pedido Nº", font=ftBt, relief='ridge'),
             sg.In(k='-RAND-', default_text=rand, font=ftBt, s=6), sg.P(),
             sg.Text(hoje, font=ftPd, text_color='white', relief='sunken', p=(5, 10))]]

    coluna_E = [[sg.In(k='-QTDADE' + prod + '-', size=3, justification='l'),
                 sg.Text(prod, size=15, font=ftPd, justification='l')]
                for prod in Nome_Prod]

    coluna_D = [[sg.T(f'R$ {Preco_Prod[pos]:2.2f}', text_color='black', s=(9, 1), font=ftPd),
                 sg.T(k='-TOT-' + prod + '-', background_color='white', size=(9, 1), text_color='black', font=ftBd)]
                for pos, prod in enumerate(Nome_Prod)]

    rodape = [[sg.Frame('',
                        [[sg.T("Sub Total", font=ftBt, s=10, text_color='black'), sg.P(),
                          sg.T("Imposto", font=ftBt, s=10, text_color='black'), sg.P(),
                          sg.T("Custo Total", font=ftBt, s=10, text_color='black')],
                         [sg.Text(k='-SUBTOTAL-', font=ftBt, s=10, text_color='red', justification='r'), sg.P(),
                          sg.Text(k='-TAXA-', font=ftBt, s=10, text_color='red', justification='r'), sg.P(),
                          sg.Text(k='-TOTAL-', font=ftBt, s=10, text_color='red', justification='r')]], expand_x=True)],
              [sg.Button('Total', font=ftBt), sg.Button('Preços', font=ftBt),
               sg.Button('Limpa', font=ftBt), sg.Push(), sg.Button('Sair', font=ftBt)]]

    layout = [topo, [sg.Col(coluna_E), sg.P(), sg.Col(coluna_D, p=(0, 0))], rodape]
    window = sg.Window('', layout, finalize=True)

    window['-QTDADE' + Nome_Prod[0] + '-'].set_focus()


    # Inicio do programa...
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Sair'):
            break
        if event in 'Refeições':
            Itens_Prod.clear()
            Itens_Prod.update(categorias['refeição'])

        if event in 'Bebidas':
            Itens_Prod.clear()
            Itens_Prod.update(categorias['bebidas'])

        if event in 'Poções':
            Itens_Prod.clear()
            Itens_Prod.update(categorias['porções'])

        if event in 'Cervejas':
            Itens_Prod.clear()
            Itens_Prod.update(categorias['cervejas'])

        if event == 'Total':
            Fechamento()
        if event == 'Preços':
            show_Price()
        if event == 'Tabela':
            produtos.Show_Price()
        if event == 'Limpa':
            Limpa()

    window.close()


if __name__ == '__main__':
    Invoices()