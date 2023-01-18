from dados import *

list_ktg, codigos = [], []
PDT = {}
aqvProd = aqv_prod()

for pd in aqvProd:
    PDT[pd[0]] = Produto(pd[0],pd[1],pd[2],pd[3])
    codigos.append(pd[0])
    if PDT[pd[0]].categoria not in list_ktg: list_ktg.append(PDT[pd[0]].categoria)


def cadastro(comando: str, cod=None):
    window = sg.Window('', [
        [sg.StatusBar(' CADASTRO DE PRODUTOS  ', font=ftBd, justification='c', text_color='red')],
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
            elif comando == 'Atualizar':
                PDT[cod] = Produto(cod, values['_Nm'].strip().title(),
                                   float(conversor(values['_Pc'])), values['_Kt'].upper())
                PDT[cod].atualizar([[PDT[x].codigo, PDT[x].nome, PDT[x].preco, PDT[x].categoria] for x in sorted(codigos)]
)
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

