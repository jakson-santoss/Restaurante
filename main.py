from invoice import Invoices               # Notas
from order import Orders                   # Pedidos
from delivery import Delivery              # Entregas
from table import Tables                   # Mesas
from produtos import Show_Price            # Cadastro de produtos
from customer import Customers             # Cadastro de Clientes
from functions import *                    # Importação de Bibliotecas e fuções extras
from dados import *                        # Tratamento de dados, abertura e fechamento de arquivos


def main_window():
    menu_mw = [['☰', ['&Cadastros', ['Clientes::', 'Produtos::', ' ...'], '&Relatórios::', 'O&utros::',
                     ['...', '...'], 'Sai&r::', ], ], ]
    layout = [[sg.Menu(menu_mw, tearoff=False)],
              [sg.T('Feijão Food Services', justification='c', expand_x=True, font=ftTT, text_color='lime')],
              [sg.Button('Pedidos', font=ftBt), sg.P(),
               sg.Button(' Mesas ', font=ftBt), sg.P(),
               sg.Button('Entregas', font=ftBt), sg.P(),
               sg.Button(' Notas ', font=ftBt)],
              [sg.Image('Logo.png')], ]
    return sg.Window('GERENCIAMENTO DE RESTAURANTE', layout=layout, font=ftPd, finalize=True)


def Inicio():
    window = main_window()
    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:                     # 'X' da jaanela (apenas fecha a janela principal)
                break
            case 'Sair::':                          # Menu Sair (Encerra o programa por completo)
                values = exit()
            case 'Clientes::':                      # Menu\ Cadastros\ Clientes
                Customers()
            case 'Produtos::':                      # Menu\ Cadastro\ Produtos
                Show_Price()
                continue
            case 'Relatórios::':                    # Menu Relatórios
                pass
                continue
            case 'Outros::':                        # Menu Outos
                pass
                continue
            case 'Pedidos':                         # Botão Pedidos
                Orders()
                continue
            case ' Mesas ':                          # Botão Mesas
                Tables()
                continue
            case 'Entregas':                         # Botão Entregas
                Delivery()
                continue
            case ' Notas ':                          # Botão Notas
                print('aqui')
                Invoices()
                continue
            case _:
                pass


# Pressione o botão verde na sarjeta para executar o script.
if __name__ == '__main__':
    # Criar as janelas iniciais
    # Funcoes.login()
    Invoices()
    Inicio()
    print('Encerrando programa!')
    # print(*forma_pagto, sep='\n')   # Desempacota a lista

