from dados import *

ftTT = ("Arial", "20", "bold", "italic")
ftPd = ("Arial", "12")
ftBd = ("Arial", "14", "bold")
ftBt = ("Calibri", "16", "bold")
btn_menu = sg.ButtonMenu('⁝', ['', ['Limpar::', 'Salvar::', 'Excluir::', '...', 'Sair::']], k='Menu',font=('_',10))
list_ktg, codigos = [], []
PDT = {}
aqvProd = aqv_prod()

for prod in aqvProd:
    PDT[prod] = Produto(prod,aqvProd[prod][0],aqvProd[prod][1],aqvProd[prod][2])
    codigos.append(prod)
    if PDT[prod].categoria not in list_ktg: list_ktg.append(PDT[prod].categoria)


def cadastro(comando: str, cod=None):
    window = sg.Window('', [
        [sg.StatusBar(' CADASTRO DE PRODUTOS  ', font=['_', 14, 'bold'], justification='c', text_color='red')],
        [sg.T('Categoria', size=12), sg.T('Descrição', justification='c', size=30), sg.T('Preço')],
        [sg.Combo(list_ktg, k='_Kt', size=10),
         sg.I(size=30, k='_Nm'), sg.I(size=8, k='_Pc')],
        [sg.P(), sg.B('Ok'), sg.Exit('Cancelar')]], font=ftPd, finalize=True)

    if cod:
        window['_Nm'].update(PDT[cod].nome)
        window['_Pc'].update(float(PDT[cod].preco))
        window['_Kt'].update(PDT[cod].categoria)

    while True:
        buttons, values = window.read()
        if buttons in ('Exit', sg.WIN_CLOSED):
            break
        elif buttons == 'Ok':
            if comando == 'Novo':
                cod = str(randint(99, 999))
            PDT[cod] = Produto(cod, values['_Nm'].strip().title(),
                               float(conversor(values['_Pc'])), values['_Kt'].upper())
            PDT[cod].salvar()
        else:
            sg.PopupQuickMessage('encerrando sem salvar')
        window.close()


def show_Price():
    """— > mostra a lista de produtos e preços."""
    def up_dt():
        if values['-CATEG-'] != 'TODOS':
            #values['-CATEG-'] = list_ktg
            lsta = [[PDT[cdg].codigo, PDT[cdg].nome, f'R$ {PDT[cdg].preco:2.2f}', PDT[cdg].categoria]
                     for cdg in sorted(codigos) if PDT[cdg].categoria in values['-CATEG-']]
        else:
            lsta = [[PDT[x].codigo, PDT[x].nome, f'R$ {PDT[x].preco:2.2f}', PDT[x].categoria] for x in sorted(codigos)]
        window['-LISTA-'].update(lsta)
        window['-QTD-'].update(f'{len(lsta)} PRODUTOS')
        return lsta

    cabecalho = [' COD ', ' PRODUTO ', ' PREÇO ', ' CATEGORIA ']
    menu_f = [['☰', ['&Novo', 'Atuali&zar', '&Outros', ['E&xcluir', '...'], 'Rela&tórios', 'Sai&r', ], ], ]
    lista = [[PDT[x].codigo, PDT[x].nome, f'R$ {PDT[x].preco:2.2f}', PDT[x].categoria] for x in sorted(codigos)]

    window = sg.Window('', [
        [sg.Menu(menu_f)],
        [sg.T(' LISTA DE PRODUTOS  ', font=ftTT, expand_x=True,
                 text_color='lime', justification='c', relief=sg.RELIEF_GROOVE)],
        [sg.Table(lista,cabecalho, key='-LISTA-', justification='l', expand_x=True)],
        [sg.HSep()],
        [sg.Combo(list_ktg + ['TODOS'], default_value='TODOS', key='-CATEG-', enable_events=True),
         sg.OK(),
         sg.StatusBar(f'{len(lista)} PRODUTOS', k='-QTD-', justification='c',expand_x=True),
         sg.B('Sair')]], font=ftPd, disable_close=False)

    while True:
        event, values = window.read()
        if event in ('Sair', sg.WIN_CLOSED):
            #return False
            break
        if event in 'OK' and values['-LISTA-']:
            print(values['-LISTA-'][0])#[0])
            print(len(lista))#[values['-LISTA-'][0]][0])
            print(lista[values['-LISTA-'][0]])#[0])

        elif event == 'Novo':
            cadastro(comando=event)

        elif event == 'Atualizar':
            if values['-LISTA-']:
                cadastro(event, lista[values['-LISTA-'][0]][0])
            else:
                sg.PopupQuickMessage('Escolha um produto para atualizar!', background_color='red', font=ftBt)

        elif event == 'Excluir' and values['-LISTA-']:
            msg, xx = PDT[lista[values['-LISTA-'][0]][0]].excluir()
            if xx:
                lista.remove(lista[values['-LISTA-'][0]])
            sg.PopupQuickMessage(msg, no_titlebar=False)
        lista = up_dt()
    window.close()


if __name__ == '__main__':
    show_Price()

    #a= 15.6
    #print(repr(a).zfill(8))
    pass