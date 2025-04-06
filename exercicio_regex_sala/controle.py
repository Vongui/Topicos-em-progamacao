import re
from conexao import Conexao
from collections import defaultdict


class Controle:

    def __init__(self):
        self.lista_conexoes = []
        self.abrir_arquivo()

    def abrir_arquivo(self):
        with open("log", "r") as arq:
            dados = arq.read().splitlines()
        conexoes = {}
        for linha in dados:
            match = re.search(r'\[(\d+)\]', linha)
            if match:
                id_conexao = match.group(1)
                if id_conexao not in conexoes:
                    conexoes[id_conexao] = {}

                if "received" in linha:
                    conexoes[id_conexao]["received"] = linha
                if "authorized" in linha:
                    conexoes[id_conexao]["authorized"] = linha

        self.lista_conexoes = [
            conexao for conexao in conexoes.values() if "received" in conexao or "authorized" in conexao
        ]

    def separar_logs(self):
        lista = []

        for x in self.lista_conexoes:
            id_conexao = None
            hora = None
            host = None
            porta = None
            usuario = None
            database = None

            cnx = Conexao()  # Criando a instância

            if "received" in x:
                linha_received = x["received"]

                if result := re.search(r'\[(\d+)\]', linha_received):
                    id_conexao = result.group(1)

                if result := re.search(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3}', linha_received):
                    hora = result.group()

                if result := re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', linha_received):
                    host = result[0]

                if result := re.search(r'port=(\d+)', linha_received):
                    porta = result.group(1)

            if "authorized" in x:
                linha_authorized = x["authorized"]

                if result := re.search(r'user=(\S+)', linha_authorized):
                    usuario = result.group(1)

                if result := re.search(r'database=(\S+)', linha_authorized):
                    database = result.group(1)

            # Define os valores no objeto Conexao
            if id_conexao:
                cnx.set_id(id_conexao)
            if hora:
                cnx.set_hora(hora)
            if host:
                cnx.set_host(host)
            if porta:
                cnx.set_porta(porta)
            if usuario:
                cnx.set_usuario(usuario)
            if database:
                cnx.set_database(database)

            if id_conexao or hora or host or porta or usuario or database:
                lista.append(cnx)

        return lista

    def listar(self):
        for x in self.separar_logs():
            print(x)

    def filtrar(self, user):
        for x in self.separar_logs():
            if x.usuario == user:
                print(x)

    def resumo(self):
        resumo_dict = defaultdict(lambda: {"qtd_acesso": 0, "usuarios": set()})

        for cnx in self.separar_logs():
            if cnx.host and cnx.usuario:
                resumo_dict[cnx.host]["qtd_acesso"] += 1
                resumo_dict[cnx.host]["usuarios"].add(cnx.usuario)

        # Convertendo os sets para listas para facilitar a exibição
        return {host: {"qtd_acesso": dados["qtd_acesso"], "usuarios": list(dados["usuarios"])}
                for host, dados in resumo_dict.items()}
