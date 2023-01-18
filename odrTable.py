# comanda[num] = {mesa[num]:{'data': 00/00/00,'prod':(qt, cod), (qt, cod), (qt, cod), ...], 'obs':'xxxxxxx'}
from dados import *


layout = [
    [sg.StatusBar('COMANDA', font=ftTT, justification='c', text_color='blue'),
     sg.ButtonMenu('⁝', ['', ['&Limpar::', '&Salvar::', 'E&xcluir::', '...', 'Sai&r::']], k='MENU')],
    [sg.T(hoje), sg.P(), sg.T('Nº', font=ftBd, text_color='black'),
     sg.I('000000', k='NCOMA', s=6, text_color='red', font=ftBd)],
    [sg.T('MESA Nº', font=ftBt), sg.Combo([_ for _ in range(1,15)],k='MESA', s=3, font=ftBt),
     sg.I('Cliente', k='CLNT', expand_x=True)],
    [sg.T('QT', font=ftBt, s=4), sg.T('Descrição', font=ftBt, expand_x=True, justification='C')],
    [sg.I(k='QT'), sg.Combo([produtos[x].nome for x in aqv_prod()])],
    [sg.Table([], ['QT', ' Descrição', 'V. Total'], expand_x=True)],
    [sg.T('OBS.:'), sg.I(k='OBS', expand_x=True, s=(50, 3))],
]
window = sg.Window('', layout, font=ftPd, finalize=True)

window['NCOMA'].update(randint(111111,999999))

while True:
    events, values= window.read()
    if events == sg.WIN_CLOSED or events == 'MENU::' and values['MENU::'] == 'Sair::':
        break
