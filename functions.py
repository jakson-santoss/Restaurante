import PySimpleGUI as sg
import requests
from datetime import datetime as dt
from random import randint

'''☰ ≡ ⁝ ▲ ▼ ▶△▽▷
relief must be flat, groove, raised, ridge, solid, or sunken
sg.popup(format_input_information(values))'''


btn_menu = sg.ButtonMenu('⁝', ['', ['&Limpar::', '&Salvar::', 'E&xcluir::', '...', 'Sai&r::']], k='MENU')

hoje = f'{dt.now():%d/%m/%Y %H:%M}'
ftTT = ("_", "18", "bold", "italic")
ftPd = ("_", "10")
ftBt = ("_", "12", "bold")
ftBd = ("_", "14", "bold")



def conversor(numero):
    if numero.isalpha():
        sg.Popup('Valor inválido, digite novamente.')
        return
    if ',' in numero:
        numero = numero.replace(',', '.')
        numero = float(numero)
    else:
        numero = float(numero)
    return numero


def adress():
    """Função que abre uma tela simples para busca de endereço e CEP.
            :return retorna um dicionário com o endereço do cliente."""
    endereco = {}
    wndCep = sg.Window('Busca de Endereço', [
        [sg.T('CEP:', size=12), sg.Input(key='-CEP-', size=8),
         sg.T('Número:', text_color='red'), sg.I(key='-NMR-', size=8)],
        [sg.T('Logradouro', size=12), sg.Input(key='-PLACE-', size=40)],
        [sg.T('Cidade', size=12), sg.Input(key='-CITY-', size=20),
         sg.I('SP', key='-UF-', size=4)],
        [sg.Button('OK', bind_return_key=True), sg.Cancel()]
    ], font=ftPd, finalize=True)

    while True:  # Event Loop
        event, values = wndCep.read()
        if event == sg.WIN_CLOSED or event in 'Cancel':
            return
        elif event == 'OK':
            if not values['-NMR-']:
                sg.PopupQuickMessage('Não se esqueça de fornecer o número!', text_color='red', font=(None, 16))
                continue
            elif values['-CEP-']:
                if len(values['-CEP-']) < 8 or len(values['-CEP-']) > 9 or values['-CEP-'].isalpha():
                    sg.PopupQuickMessage('CEP inválido, digite novamente.', no_titlebar=False, font=ftBt)
                    continue
                elif '-' in values['-CEP-']:
                    values['-CEP-'] = values['-CEP-'].replace('-', '')
                link = f"https://viacep.com.br/ws/{values['-CEP-']}/json/"
                pedido = requests.get(link)  # Recebe o pedido do link
                dic_pedido = pedido.json()  # Transforma o conteúdo recebido em um dicionário
                endereco = dic_pedido
            elif not values['-CEP-'] and values['-PLACE-'] and values['-CITY-']:
                place = values['-PLACE-'].title()
                city = values['-CITY-'].title()
                uf = values['-UF-'].upper()
                link = f'https://viacep.com.br/ws/{uf}/{city}/{place}/json/'
                pedido = requests.get(link)  # Recebe o pedido do link
                dic_pedido = pedido.json()  # Transforma o conteúdo recebido em um dicionário
                endereco = dic_pedido[0]
                if len(dic_pedido) > 1:
                    sg.PopupQuickMessage(f'Atenção\nExistem {len(dic_pedido)} logradouros com {place}.'
                                         f'\nBusque pelo nome completo ou pelo CEP.'
                                         , no_titlebar=False, font=ftBt)
                    continue
            else:
                busca = sg.PopupOKCancel('Preciso de um CEP ou "logradouro e cidade" para pesquisar.',
                                         title='Busca')
                if busca == 'Cancel':
                    return
                continue
            break
    endereco_cliente = f"{endereco.get('logradouro')}, {values['-NMR-']}\n" \
                       f"{endereco.get('bairro')} - {endereco.get('cep')}\n" \
                       f"{endereco.get('localidade')} - {endereco.get('uf')}"
    sg.PopupQuickMessage(endereco_cliente, no_titlebar=False, font=ftBt)
    endereco_cliente = endereco_cliente.replace('\n', ' - ')
    wndCep.close()
    return endereco_cliente


def PopupLista(title: str, lista: list):
    botao, valor = sg.Window('', [
        [sg.T(title, expand_x=True, font=ftBt, text_color='blue')],
        [sg.InputCombo(lista)],
        [sg.Ok(), sg.Cancel()]],
                             text_justification='c', finalize=True).read(close=True)
    if botao == 'Cancel':
        return
    elif botao == 'Ok' and valor:
        return valor[0]


def fone_test(fone_n):
    msg_err = 'Número inválido!\nForneça um número válido por favor!'
    if fone_n:
        fone_n = fone_n.strip()
        # testa se os quatro primeiros números e os 4 últimos são número
        if fone_n[:4].isnumeric() and fone_n[-4:].isnumeric():
            if '-' not in fone_n:
                fone_n = fone_n[:-4] + '-' + fone_n[-4:]
            return fone_n
    else:
        sg.PopupQuickMessage(f'{fone_n}\n{msg_err}' if fone_n else 'Não há telefone',
                             font='_,16', background_color='red')
        return


def funcao_teste():
    """Função criada para teste."""
    lista = []
    codigos = {}

    for prod in aqvProd:
        # codigos[prod] = Produto(prod, aqvProd[prod][0], aqvProd[prod][1], aqvProd[prod][2])
        # print (codigos[prod].codigo, codigos[prod].nome, codigos[prod].preco)
        print(prod, type(prod), aqvProd[prod])
    # print(produtos)
    # print(sorted(codigos))
    print()

    '''
    with open("produtos.json", "w", encoding='utf-8') as aqv_ctg:
        dump(_produtos, aqv_ctg)     # Salva o dicionário no arquivo
    '''


if __name__ == '__main__':
    # teste_teste()
    fone_test()
