from ap2.lib.interface import *
import json


class Banco_de_dados:
    dados_clientes = {}
    dados_produtos = {}
    dados_vendas = {}
    def __init__(self):
        pass

    def update_data(self):
        buffer_client = []
        for k,v in Banco_de_dados.dados_clientes.items():
            buffer_client.append({k : v.__dict__})
        load_reload.save("CLIENTES.JSON","w+", *buffer_client)

        buffer_prod= []
        for k,v in Banco_de_dados.dados_produtos.items():
            buffer_prod.append({k : v.__dict__})
        load_reload.save("PRODUTOS.JSON","w+", *buffer_prod)

        buffer_vendas = []
        for k, v in Banco_de_dados.dados_vendas.items():
            buffer_vendas.append({k: v.dicionario()})
        load_reload.save("VENDAS.JSON", "w+", *buffer_vendas)


    def retrieve_data(self):
        cl = arquivo.reload_data("CLIENTES.json")
        firstkey =[list(i.values()) for i in cl]
        secondkey = [list(i[0].values()) for i in firstkey]
        for valores in secondkey:
            Cliente(*valores)

        cl = arquivo.reload_data("PRODUTOS.json")
        firstkey = [list(i.values()) for i in cl]
        secondkey = [list(i[0].values()) for i in firstkey]
        for valores in secondkey:
            Motocicleta(*valores)

        cl = arquivo.reload_data("VENDAS.json")
        firstkey = [list(i.values()) for i in cl]
        secondkey = [list(i[0].values()) for i in firstkey]
        for valores in secondkey:
            Venda(*valores)


class Cliente(Banco_de_dados):
    reg = 0
    reg_3 = Banco_de_dados.dados_clientes.keys()


    def __init__(self, nome="Vazio", cont="Vazio", cpf="Vazio", reg=None):
        self.nome = nome.title().strip()
        self.contato = cont.strip()
        self.cpf = cpf.strip()

        self.reg = reg
        while self.reg == None or self.reg in Cliente.reg_3:
            Cliente.reg += 1
            self.reg = str(Cliente.reg)
        # Cliente.reg_2.update({self.reg: self})
        super().dados_clientes.update({self.reg: self})

    def __repr__(self):
        return f"# Reg: {self.reg} | Nome: {self.nome} | CPF: {self.cpf} | " \
               f"Cont.: {self.contato} |"

    def editar_valores(self):
        c = 0
        editaveis = {"Nome" : self.nome, "Contato" : self.contato, "CPF" : self.cpf}
        print('Selecione o dado a ser alterado')
        for k,v in editaveis.items():
            c+=1
            print(formatar(f"{c} » ", cor = "azul"), formatar(f"{k}: {v}", cor = "azul", bold = True))

        editando = str(selecionar_dict(Nome = "nome", Contato = "contato", CPF = "cpf"))
        if editando == True:
            novo_valor = str(input(formatar("Novo Valor: ", "verde", bold=True)))
            novo_valor.strip().title()
            setattr(self, editando, novo_valor)
        else:
            return

def novo_cliente():
    while True:
        try:
            nome = str(input(formatar("Nome Completo: ", bold = True)))
            cpf = str(input(formatar("RG ou CPF: ", bold = True)))
            cont = str(input(formatar("Contato: ", bold = True)))
        except:
            print(formatar("Valor inválido! \n Tente Novamente", cor="vermelho"))
        else:
            return Cliente(nome, cpf, cont)


class Motocicleta(Banco_de_dados):
    reg = 0
    reg_3 = Banco_de_dados.dados_produtos.keys()

    def __init__(self, modelo="Desconhecido", ano="Desconhecido", valor="00", estoque="00", reg=None):
        self.modelo = modelo.title().strip()
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
        self.reg = reg
        while self.reg == None or self.reg in Motocicleta.reg_3:
            Motocicleta.reg += 1
            self.reg = str(Motocicleta.reg)
        super().dados_produtos.update({self.reg: self})

    def __repr__(self):
        try:
            return f"# Reg: {self.reg} |  {int(self.estoque)} un | Modelo/ano: {self.modelo} / {int(self.ano)} | Valor: R$ {float(self.valor):,.2f}"
        except:
            return formatar(f"#Reg: {self.reg} |  Registro interrompido pela alimentação de valor inválido","vermelho")

    def editar_valor(self):
        c = 0
        editaveis = {"Modelo" : self.modelo,
        "Ano": self.ano,
        "Valor": self.valor,
        "Estoque": self.estoque}
        print('Selecione o dado a ser alterado')
        for k,v in editaveis.items():
            c+=1
            print(formatar(f"{c} » ", cor = "azul"), formatar(f"{k}: {v}", cor = "azul", bold = True))

        editando = str(selecionar_dict(Modelo = "modelo", Ano = "ano", Valor = "valor", Estoque = "estoque"))
        if editando == True:
            novo_valor = str(input(formatar("Novo Valor: ", "verde", bold = True)))
            novo_valor.strip().title()
            setattr(self, editando,novo_valor )
        else:
            return

def novo_produto():
    while True:
        try:
            modelo = str(input(formatar("Modelo: ",bold = True)))
            ano = str(input(formatar("Ano: ", bold = True)))
            valor = int(input(formatar("Valor: ", cor="amarelo", bold = True)))
            estoque = int(input(formatar("Quant em Estoque: ", cor = "cinza", bold = True)))
        except:
            print(formatar("Valor inválido! \n Tente Novamente", cor = "vermelho"))
        else:
            return Motocicleta(modelo, ano, valor, estoque)


class Venda(Banco_de_dados):
    reg = 0
    reg_3 = Banco_de_dados.dados_produtos.keys()
    total_em_vendas = 0

    def __init__(self, client_reg, prod_reg, valor, parcelas, nome=None , modelo=None):
        self.reg = Venda.reg + 1
        self.cliente_reg = int(client_reg)
        if nome == None:
            self.cliente = super().dados_clientes[str(client_reg)].nome
        else:
            self.cliente = nome

        self.produto_reg = int(prod_reg)
        if modelo == None:
            self.produto = super().dados_produtos[str(prod_reg)].modelo
        else:
            self.produto = modelo
        try:
            self.valor = float(self.produto.valor)
        except:
            self.valor = valor
        Venda.total_em_vendas += self.valor
        self.prestacoes = int(parcelas)
        self.valor_parcelas = self.valor / parcelas * 1.1
        super().dados_vendas.update({self.reg: self})

    def __repr__(self):
        return  f"# Reg: {self.reg} | Cliente: {self.cliente} | Produto: {self.produto} | Financiamento: {self.prestacoes} x de R$ {self.valor_parcelas:,.2f}"

    def dicionario(self):
        a = {"client_reg" : self.cliente_reg,
             "prod_reg" : self.produto_reg,
             "valor" : self.valor,
             "parcelas" : self.prestacoes,
             "nome" : self.cliente,
             "modelo": self.produto}
        return a

    def editar_venda(self):
        c = 0
        editaveis = {"Cliente": self.cliente, "Produto": self.produto, "Parcelas": self.prestacoes}
        print('Selecione o dado a ser alterado')
        for k, v in editaveis.items():
            c += 1
            print(formatar(f"{c} » ", cor="azul"), formatar(f"{k}: {v}", cor="azul", bold=True))

        editando = str(selecionar_dict(Cliente="cliente_reg", Produto="produto_reg", Parcelas="prestacoes"))
        if editando == True:
            novo_valor = str(input(formatar("Novo Valor: ", "verde", bold = True)))
            novo_valor.strip().title()
            setattr(self, editando,novo_valor )
        else:
            return

        self.cliente = super().dados_clientes[str(self.cliente_reg)]
        self.produto = super().dados_produtos[str(self.produto_reg)]
        self.valor = self.produto.valor
        self.valor_parcelas = float(self.valor) / float(self.prestacoes) * 1.1


def nova_venda(lista_cliente, lista_produto):
    while True:
       # try:
        cabecalho("Nova Venda")
        reg_client = selecionar_lista(conteudo("Lista de Clientes", *lista_cliente), True, registro=True)
        if reg_client == True: # True significa que a opcao sair foi escolhida entao a funcao retorna None cancelando a criacao
            return None
        print(reg_client)
        print("**"*20)
        reg_prod = selecionar_lista(conteudo("Lista de Produtos", *lista_produto), registro=True)
        if reg_prod == True: # True significa que a opcao sair foi escolhida entao a funcao retorna None cancelando a criacao
            return None
        valor = Banco_de_dados.dados_produtos[reg_prod].valor
        print(f"\33[1mCliente:\33[m {Banco_de_dados.dados_clientes[reg_client].nome} \n")
        print(f"\33[1mProduto:\33[m {Banco_de_dados.dados_produtos[reg_prod].modelo} | {Banco_de_dados.dados_produtos[reg_prod].ano} \n")
        print(f"\33[1mValor:\33[m {valor:.2f} \n")
        prestacoes = int(input(formatar("Quant de Parcelas: ", cor="cinza", bold=True)))
        return Venda(reg_client, reg_prod, valor, prestacoes)
       # except:
       #     print(formatar("Ocorreu Um Erro!", cor = "vermelho"))
    # while True:
        # try:
            # reg_client = str(input(formatar("Cliente: ",bold = True)))
            # reg_prod = str(input(formatar("Produto: ", bold = True)))
            # valor = int(input(formatar("Valor: ", cor="amarelo", bold = True)))
            # prestacoes = int(input(formatar("Quant em Estoque: ", cor = "cinza", bold = True)))
        # except:
        #     print(formatar("Valor inválido! \n Tente Novamente", cor = "vermelho"))
        # else:
        #     return Venda(reg_client, reg_prod, valor, prestacoes)



if __name__ == '__main__':
    a = Cliente("Augusto","155997799", "98879-7789")
    b = Cliente("Juvenisclaudio", "12", "996")
    c = Motocicleta("Arrumba",1992,2900000,15)

    lista_c = [a,b,Cliente("Fevereiro","100009", "97777-7789"), Cliente("claudio", "12998", "369-4496")]
    lista_m = [c,Motocicleta("Modelagem", "1999", 1500, 9), Motocicleta("Hyunday", "2010", 1200, 5)]
    lista_v = []

    Banco_de_dados.update_data(Banco_de_dados)

    Banco_de_dados.retrieve_data(Banco_de_dados)










