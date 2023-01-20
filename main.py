#!/usr/bin/python3
import invoice
from invoice import Invoices  # Notas
from order import Orders  # Pedidos
from delivery import Delivery  # Entregas
from table import Tables  # Mesas
from produtos import Show_Price  # Cadastro de produtos
from customer import Customers  # Cadastro de Clientes
from functions import *  # Importação de Bibliotecas e fuções extras
from dados import *  # Tratamento de dados, abertura e fechamento de arquivos

dica = {'Pedidos': 'Anotação dos pedidos para enviar à cozinha', 'Mesas': 'Controla as comandas das mesas',
        'Entregas': 'Emite as comandas de entrega', 'Notas': 'Emite as Notas para os clientes',
        'Clientes': 'Abre o Cadastro de clientes', 'Produtos': 'Abre o Cadastro de Produtos',
        'Relatórios': 'Emite os relatórios', 'Outros': 'Outras deduções', 'Sair': 'Encerra o programa'}


def Inicio():
    #sg.theme('dark')
    layout = [[sg.T('Feijão Food Services', font=ftTT, expand_x=True, text_color='lime',
                    justification='center', relief='groove', p=(5, 10))],
              [[sg.Col([
                  [sg.Button('Pedidos', font=ftBt, border_width=0, s=12, tooltip=dica['Pedidos'])],
                  [sg.Button('Mesas', font=ftBt, border_width=0, s=12, tooltip=dica['Mesas'])],
                  [sg.Button('Entregas', font=ftBt, border_width=0, s=12, tooltip=dica['Entregas'])],
                  [sg.Button('Notas', font=ftBt, border_width=0, s=12, tooltip=dica['Notas'])],
                  [sg.Button('Clientes', font=ftBt, border_width=0, s=12, tooltip=dica['Clientes'])],
                  [sg.Button('Produtos', font=ftBt, border_width=0, s=12, tooltip=dica['Produtos'])],
                  [sg.Button('Relatórios', font=ftBt, border_width=0, s=12, tooltip=dica['Relatórios'])],
                  [sg.Button('Outros', font=ftBt, border_width=0, s=12, tooltip=dica['Outros'])],
                  [sg.VPush()],
                  [sg.Button('Sair', font=ftBt, border_width=0, s=12, tooltip=dica['Sair'])]],
                  expand_y=True),
                  sg.Col([[sg.Image('Logo.png')]])], ],
              [sg.StatusBar('',k='DICA'), sg.Sizegrip()]]
    window = sg.Window('GERENCIAMENTO DE RESTAURANTE', layout=layout, font=ftPd,
                       button_color=sg.theme_background_color(), finalize=True)
    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:         # 'X' da jaanela (apenas fecha a janela principal)
                break
            case 'Sair':                # Botão Sair (Encerra o programa por completo)
                values = exit()
            case 'Pedidos':  # Botão Pedidos
                Orders()
                continue
            case ' Mesas ':  # Botão Mesas
                Tables()
                continue
            case 'Entregas':  # Botão Entregas
                Delivery()
                continue
            case 'Notas':     # Botão Notas
                invoice.Invoices()
                continue
            case 'Clientes':            # Botão Clientes
                Customers()
            case 'Produtos':  # Menu\ Cadastro\ Produtos
                Show_Price()
                continue
            case 'Relatórios':  # Menu Relatórios
                pass
                continue
            case 'Outros':  # Menu Outos
                pass
                continue
            case _:
                pass

if __name__ == '__main__':
    # Criar as janelas iniciais
    # Funcoes.login()
    Inicio()

    # print('Encerrando programa!')
    pass
    # print(*forma_pagto, sep='\n')   # Desempacota a lista
# Pressione o botão verde na sarjeta para executar o script.

