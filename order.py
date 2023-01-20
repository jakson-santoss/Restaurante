# pedido[N_ORD]{'data':00/00, [(QT, COD), (QT, COD), (QT, COD), ...], 'obs':'xxxxxxxxxxxxxxxxx'}
from functions import *
from produtos import PDT, codigos

pedidos, tabela = {}, []
lista_P = [[PDT[cd].codigo, PDT[cd].nome, PDT[cd].preco] for cd in codigos]


def Orders():
    layout = [
        [sg.Text(" PEDIDO ", font=ftTT, expand_x=True, text_color='lime',
                 justification='center', relief='groove'),
         btn_menu(['&Limpar::', '&Salvar::', 'E&xcluir::']), ],
        [sg.T(hoje, relief='ridge'), sg.P(),
         sg.T('Nº', font=ftTT, text_color='red'), sg.I(k='-N_ORD-', s=6, font=ftTT, text_color='red')],
        [sg.HSep(color='gray', p=(0, 0))],
        [sg.T('QT', font=ftBt), sg.T('PRODUTO', font=ftBt, expand_x=True, justification='c')],
        [sg.Spin([_ for _ in range(15)], k='-QT-', initial_value=1, s=3),
         sg.Combo(lista_P, default_value=lista_P[0], k='-COD-', expand_x=True, enable_events=True, readonly=True)], #bind_return_key=True)],
        [sg.Table(tabela, ['QT', ' Descrição', 'V. Total'], k='-TBL-', expand_x=True)],
        [sg.T('OBS.:'), sg.I(k='OBS', expand_x=True, s=(50, 3))],
        [sg.StatusBar('', k='STTS')],
        [sg.Sizegrip()]
    ]

    window = sg.Window('', layout, font=ftPd, finalize=True)

    # if pedidos[1]['data'] != hoje[:10]:
    #     del pedidos
    # N_ORD = max(pedidos.keys())+1

    window['-QT-'].set_focus()
    while True:
        events, values = window.read()
        if events == sg.WIN_CLOSED or events == 'MENU::' and values['MENU::'] == 'Sair::':
            break
        if events == '-COD-':
            pc_tot = values["-COD-"][2] * values["-QT-"]
            tabela.append([values['-QT-'], values['-COD-'][1], f'R$ {pc_tot:.2f}'])
            print([values['-QT-'], values['-COD-'][1], f'R$ {pc_tot:.2f}'])
            window['-TBL-'].update(tabela)
            window['-QT-'].set_focus()

        N_ORD = values['-N_ORD-']
        DATA = hoje[:10]
        # pedidos[N_ORD]={'data':hoje, [(QT, COD), (QT, COD), (QT, COD)], 'obs':'xxxxxxxxxxxxxxxxx'}

    window.close()


if __name__ == '__main__':
    Orders()

    pass