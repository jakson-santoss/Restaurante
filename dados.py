from json import load, dump
import sqlite3
import csv
from functions import *
list_Prod, list_Cmd, list_Ped = [], [],[]

class Dados:
    """ Cria e ativa a base de dados abrindo todos os arquivos.
    Abre e faz a conexão com o banco de dados para a criação das tabelas."""
    def __init__(self, tbl):
            if tbl == 'cliente':
                self.conexao = sqlite3.connect('DataBase/clientes.db')
                self.tab_cli()
            elif tbl == 'nota':
                self.conexao = sqlite3.connect('DataBase/invoice.db')
                self.tab_nota()

    def tab_cli(self):
        """Cria a tabela Clientes para inserção de dados."""
        cursor = self.conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
                                 FONE TEXT PRIMARY KEY NOT NULL,
                                 NOME TEXT NOT NULL,
                                 ENDERECO TEXT NOT NULL,
                                 EMAIL TEXT)''')
        self.conexao.commit()
        cursor.close()

    def tab_nota(self):
        """Cria a tabela Clientes para inserção de dados."""
        cursor = self.conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS invoces(
                                 N_ORD INT PRIMARY KEY NOT NULL,
                                 DATA TEXT NOT NULL,
                                 PROD LIST NOT NULL,
                                 OBS TEXT)''')
        self.conexao.commit()
        cursor.close()


def aqv_prod():
    with open("DataBase/produtos.json", "r", encoding='utf-8') as aqv_ctg:
        arquivo = load(aqv_ctg)  # Abre o arquivo para leitura
    return arquivo

def aqv_ped():
    with open("DataBase/pedidos.csv", "r", encoding='utf-8') as ref:
        aqv = csv.reader(ref, delimiter=',')
    return [_ for _ in aqv]

def aqv_cmd():
    with open("DataBase/comandas.csv", "r", encoding='utf-8') as ref:
        aqv = csv.reader(ref, delimiter=',')
    return [_ for _ in aqv]


class Clientes(object):
    """Classe responsável pela manipulação dos dados dos clientes no banco de dados"""

    def __int__(self, fone, nome, ender):
        self.fone = fone
        self.nome = nome
        self.ender = ender
        self.email = '@email'

    @property
    def completo(self):
        return [self.fone, self.nome, self.ender, self.email]

    def write_cli(self):
        """Inclui clientes no banco de dados"""
        banco = Dados('cliente')
        try:
            c = banco.conexao.cursor()
            c.execute('''INSERT into clientes(FONE, NOME, ENDERECO, EMAIL) 
            VALUES(?, ?, ?, ?)''', (self.fone, self.nome, self.ender, self.email))
            banco.conexao.commit()
            c.close()
            return f"{self.nome}\nfoi cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do cliente"

    def updt_cli(self):
        """Atualiza clientes no banco de dados"""
        banco = Dados('cliente')
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE clientes SET NOME = '" + self.nome + "', ENDERECO = '"
                      + self.ender + "', EMAIL = '" + self.email +
                      "' where FONE = '" + self.fone + "'")
            banco.conexao.commit()
            c.close()

            return "Cliente atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do cliente"

    @staticmethod
    def delete_cli(telefone):
        """Exclui clientes no banco de dados"""
        banco = Dados('cliente')
        try:
            c = banco.conexao.cursor()
            c.execute('DELETE FROM clientes WHERE FONE = "' + telefone + '"')
            banco.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do cliente"

    def select_cli(self, fone):
        """Seleciona um cliente no banco de dados"""
        banco = Dados('Cliente')
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM cliente WHERE FONE = '" + fone + "'")

            for linha in c:
                self.fone = linha[0]
                self.nome = linha[1]
                self.ender = linha[2]
                self.email = linha[3]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do cliente"

    def read_task(self):
        banco = Dados('cliente')
        try:
            c = banco.conexao.cursor()
            c.execute('''SELECT * FROM clientes''')
            data = c.fetchall()
            banco.conexao.commit()
            c.close()
            return data
        except:
            return None


class Produto(object):
    aqvProd = aqv_prod()

    def __init__(self, codigo,nome, preco,categoria):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def completo(self):
        return[self.codigo, self.categoria, self.nome, self.preco]

    def excluir(self):
        if self.codigo in aqvProd:
            try:
                self.aqvProd.pop(self.codigo)
                with open("DataBase/produtos.json", "w", encoding='utf-8') as aqv_ctg:
                    dump(self.aqvProd, aqv_ctg)     # Salva o dicionário no arquivo

                return "Produto excluído com sucesso!", True
            except:
                return "Ocorreu um erro na exclusão do produto", False

    def salvar(self):
        try:
            self.aqvProd[self.codigo]=[ self.nome, self.preco, self.categoria]
            with open("DataBase/produtos.json", "w", encoding='utf-8') as aqv_ctg:
                dump(self.aqvProd, aqv_ctg)  # Salva o dicionário no arquivo
            return 'Produto Salvo com sucesso!'
        except:
            return 'Ocorreu algum erro, o produto não foi salvo!'
    def select(self,cod):
        if cod in aqvProd.keys():
            self.codigo = cod
            self.nome = aqvProd[cod][0]
            self.preco = aqvProd[cod][1]
            self.categoria = aqvProd[cod][2]
            return self.completo()
        else:
            return 'Este produto não está cadastrado!'


class Pedidos(object):
    aqvPedidos = Dados('pedido')
    #list_Pedidos= [x[0] for x in aqvPedidos]

    def __int__(self):
        self.nPed = 0
        self.data = ''
        self.fone = ''
        self.pProd = []
        self.obs = ''

    @property
    def completo(self):
        return[self.nPed, self.data, self.fone, self.pProd, self.obs]

    def grava_pdd(self):
        """Inclui ou atualiza produtos na planilha."""
        with open("Arquivos/od_serv.csv", "a+", encoding='utf-8') as arquivo:  # Inclui
            arquivo.write(arquivo,
                f'{self.nPed},{self.data},{self.fone},{self.pProd},{self.obs}\n')

    def slct_pdd(self, p_seq):
        if self.nPed in [self.aqvPedidos[x][0] for x in range(len(self.aqvPedidos))]:  # Atualiza
            for ods in self.aqvPedidos:
                if ods[0] == p_seq:
                    p_seq = Pedidos()
                    p_seq.nPed = ods[0]
                    p_seq.data = ods[1]
                    p_seq.fone = ods[2]
                    p_seq.pProd = ods[3]
                    p_seq.obs = ods[4]
            return p_seq
        else:
            return


class Comandas(object):
    aqvComandas = Dados('comanda')
    #list_Comandas = [x[0] for x in aqvComandas]

    def __int__(self):
        self.nComa = 0
        self.mesa = ''
        self.prodt = []
        self.vTot = 0


class Invoices(object):             # Notas
    def __int__(self):
        self.n_ord = 0
        self.data = ''
        self.prod = []
        self.obs = ''

        banco = Dados('nota')


if __name__ == '__main__':
    #list_Comandas()
    aqvProd = aqv_prod()
    for a in aqvProd:
        print(a,'\t',aqvProd[a])
    print(len(aqvProd))

    pass

