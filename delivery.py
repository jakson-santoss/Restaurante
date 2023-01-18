# pedido[num]={cliente[fone]:{'data':'00/00/00','prod':[(qt, cod),(qt, cod),(qt, cod),...],'obs':'xxxxx'}
from dados import *
import functions
import CadCliente
import produtos

fPgto = ['Dinheiro', 'Pix', 'Cartão', 'Cheque']


def __select_cli():
    title = 'Digite ou escolha\no telefone do cliente'
    fone = functions.fone_test(functions.PopupLista(title, [fone[0] for fone in Clientes().read_task()]))
    if not fone or fone not in (x[0] for x in Clientes().read_task()):
        if sg.PopupOKCancel('Deseja cadastrar o cliente?') == 'OK':
            sg.PopupQuickMessage(f'Redirecionando para cadastro!')
            CadCliente.Cliente()
        else:
            return
    else:
        window['NOME'].update(CadCliente.cliente[fone].nome)
        window['FONE'].update(CadCliente.cliente[fone].fone)
        window['ENDER'].update(CadCliente.cliente[fone].ender)
    return


layout = [[
    [sg.ButtonMenu('⁝', ['', ['Limpar::', 'Salvar::', 'Excluir::', '...', 'Sair::']], k='MENU::'),
     sg.StatusBar(' DELIVERY ', justification='c', text_color='lime', font=ftTT)],
    [sg.T(' PEDIDO Nº ', font=ftBd), sg.In('000000', k='NUM_ODR', font=ftBd, s=6, text_color='blue'),
     sg.P(), sg.T(f'{hoje}', k='DATA', text_color='white')],
    # Informações
    [sg.Frame('', [
        [sg.I('Nome', k='NOME',expand_x=True), sg.I('Telefone', k='FONE', s=12)],
        [sg.I('Endereço', k='ENDER', s=60, )]])],
    [sg.T('Obs', pad=(0, 0)), sg.I(key='OBS', expand_x=True)],
    [sg.Button('Produtos', k='PROD'), sg.P(), sg.T('F. Pagamento'),
     sg.Combo(fPgto, k='PAGTO', default_value=fPgto[0])],
    # Corpo
    [sg.T(' QT ', font=ftBd, text_color='black'), sg.P(),
     sg.T('Descrição', font=ftBd, text_color='black'), sg.P(),
     sg.T('Valor   ', font=ftBd, text_color='black')],
    [sg.Output(size=(60, 8), expand_x=True, expand_y=True)]],
    # Rodapé
    [sg.Col([[sg.B('...', disabled=True)],
             [sg.B('...', disabled=True)],
             [sg.B('IMPRIMIR')]]), sg.P(),
     sg.Col([[sg.T('VALOR', font=ftBt, text_color='red')],
             [sg.T('ENTREGA', font=ftBt, text_color='red')],
             [sg.T('TOTAL', font=ftBt, text_color='red')]]),
     sg.Frame('', [[sg.T(k='VALOR', font=ftBd, text_color='black')],
                   [sg.T(k='DEDUCAO', font=ftBd, text_color='black')],
                   [sg.T(k='TOTAL', font=ftBd, text_color='black')]], s=(100, 90))]]

window = sg.Window('', layout, font=ftPd, finalize=True)

#__select_cli()
window['OBS'].set_focus()

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED or events == 'MENU::' and values['MENU::'] == 'Sair::':
        exit()
    elif events == 'PROD':  # and values['NOME']: ['NUM_ODR']:
        pdt = produtos.show_Price()