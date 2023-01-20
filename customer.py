from dados import *

list_fone, cliente = [], {}

for clt in Clientes().read_task():
    cliente[clt[0]] = Clientes()
    cliente[clt[0]].fone = clt[0]
    cliente[clt[0]].nome = clt[1]
    cliente[clt[0]].ender = clt[2]
    cliente[clt[0]].email = clt[3]
    list_fone.append(clt[0])


def Customers():
    menu = sg.ButtonMenu('⁝', ['', ['Limpar::', 'Salvar::', '...', ['Excluir::'],  'Sair::']], k='MENU::')
    kbc = ['TELEFONE', 'NOME', 'ENDEREÇO',  'EMAIL']

    def __atu(inf=None):
        if inf:
            window['FONE::'].update(cliente[inf].fone)
            window['NOME::'].update(cliente[inf].nome)
            window['ENDER::'].update(cliente[inf].ender)
            window['EMAIL::'].update(cliente[inf].email)
        else:
            window['FONE::'].update('')
            window['NOME::'].update('')
            window['ENDER::'].update('')
            window['EMAIL::'].update('')
            window['_Box'].update([cliente[x].completo for x in list_fone])

    window = sg.Window('Cadastro de Clientes', [
        [sg.Frame('', [
            [sg.T('Telefone:', font=ftBt), sg.I(s=15, k='FONE::', font=ftBt),
             sg.B('Buscar'), sg.P(), menu],
             [sg.T('Nome:', s=9), sg.I(k='NOME::', expand_x=True)],
            [sg.B('BUSCA', k='Adress_Btn', bind_return_key=True), sg.I(k='ENDER::', s=60)],
            [sg.P(), sg.T('Email:', s=6), sg.I(size=30, k='EMAIL::')]])],
        [sg.Table([], kbc, key='_Box', justification='l', enable_events=True, expand_x=True)],
        [sg.B('Salvar', bind_return_key=True), sg.P(), sg.B('Sair', bind_return_key=True)]],
                       font=ftPd, finalize=True)
    __atu()
    while True:
        event, values = window.read()
        # botão sair ou menu sair
        if event in ('Sair', sg.WIN_CLOSED) or event == 'MENU::' and values['MENU::'] == 'Sair::':
            break
        # Botão Buscar, busca o cliente no arquivo.
        elif event == 'Buscar':
            if values['FONE::'] in [x[0] for x in Clientes().read_task()]:
                for x in Clientes().read_task():
                    if values['FONE::'] in x:
                        __atu(values['FONE::'])
        # Botão Busca (Endereço) entra na busca de enrereço por CEP ou logradouro
        elif event == 'Adress_Btn':
            if values['FONE::']:
                window['ENDER::'].update(adress())
                window['EMAIL::'].set_focus()
            else:
                sg.PopupQuickMessage('Não há cliente válido,\n por favor insira um cliente!',
                                     title='ATENÇÃO', no_titlebar=False, font=ftBt)
        # Escolha direto na lista, passa as informações para a as caixas de incerssão
        elif event == '_Box' and values['_Box']:
            __atu(list_fone[values['_Box'][0]])
        # Menu, ..., Excluir, excui o cliente do banco de dados.
        elif event == 'MENU::' and values['MENU::'] == 'Excluir::' and values['_Box']:
            if sg.PopupOKCancel(f'Deseja realmente excluir {values["NOME::"]}?') == 'OK':
                sg.PopupQuickMessage(Clientes().delete_cli(values['FONE::']), no_titlebar=False, font=ftBt)
                list_fone.remove(values['FONE::'])
                __atu()
            else:
                continue
        # Botão Salvar ou [Menu, Salvar]. Salva as informações do cliente no banco de dados
        elif event == 'Salvar' or event == 'MENU::' and values['MENU::'] == 'Salvar::':
            fone = fone_test(values['FONE::'])
            if not fone:
                window['FONE::'].set_focus()
                continue
            cliente[fone] = Clientes()
            cliente[fone].fone = fone
            cliente[fone].nome = values['NOME::'].title()
            cliente[fone].ender = values['ENDER::']
            cliente[fone].email = values['EMAIL::'].lower()
            list_fone.append(fone)

            if fone in [x[0] for x in Clientes().read_task()]:
                sg.PopupQuickMessage(cliente[fone].updt_cli(), no_titlebar=False, font=ftBt)
            else:
                sg.PopupQuickMessage(cliente[fone].write_cli(), no_titlebar=False, font=ftBt)
            __atu()
            window['FONE::'].set_focus()
    window.close()


if __name__ == '__main__':
    Customers()
