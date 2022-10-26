from ap2.lib.interface import *

DATA = Banco_de_dados()
DATA.retrieve_data()

CLIENTES = list(DATA.dados_clientes.values()) #[Cliente("Fevereiro","100009", "97777-7789"),Cliente("claudio", "12998", "369-4496")] # temp
MOTOCICLETAS = list(DATA.dados_produtos.values()) #[Motocicleta("Arrumba",1992,2900000,15),Motocicleta("Hyunday",2015,2900,10)] #  temp
VENDAS = list(DATA.dados_vendas.values()) #[Venda(1,1,2900000,39)] # temp


REGISTRO_CLIENTES = {"Procurar": ("procura_dict",{"Editar": "Funcaoeditar","Excluir": "Exclusao"}),
                     "Editar": "Funcaoeditar",
                     "Excluir": "Exclusao"}
OPCOES_CLIENTES = {"Novo Cliente": "Vazio",
                   "Registro de Clientes": REGISTRO_CLIENTES}



REGISTRO_MOTO = {"Procurar": ("procura_dict",{"Editar": "Funcaoeditar","Excluir": "Exclusao"}),
                     "Editar": "Funcaoeditar",
                     "Excluir": "Exclusao"}
OPCOES_MOTO = {"Novo Produto": "Vazio",
               "Registro de Motocicletas": REGISTRO_MOTO}



REGISTRO_VENDAS = {"Procurar": ("procura_dict",{"Editar": "Funcaoeditar"}),
                     "Editar": "Funcaoeditar"}
OPCOES_VENDA = {"Nova Venda": "Vazio",
                "Registro de Vendas": REGISTRO_VENDAS }



OPCOES_BASE = {"Clientes": OPCOES_CLIENTES,
          "Motocicletas": OPCOES_MOTO,
          "Vendas": OPCOES_VENDA}

TITULO_BASE = "Sistema Básico de Registros"

opcoes = {}
alter = ()
opcoes = OPCOES_BASE
Escolha = bool

while True:
    DATA.update_data()
    CLIENTES = list(DATA.dados_clientes.values())
    MOTOCICLETAS = list(DATA.dados_produtos.values())
    VENDAS = list(DATA.dados_vendas.values())

    if not Escolha:
        break

    titulo = TITULO_BASE
    alter = ()
    buffer = []
    Escolha = menu(titulo, *alter, **opcoes)

    if Escolha == opcoes["Clientes"]: # Menu » Cliente
        titulo = "Clientes"
        buffer = CLIENTES
        Escolha = menu(titulo,**Escolha)


        if Escolha == OPCOES_CLIENTES ["Novo Cliente"]: # Menu » Cliente » Novo Cliente
            CLIENTES.append(novo_cliente())
            continue


        elif Escolha == OPCOES_CLIENTES ["Registro de Clientes"]: # Menu » Cliente » Registro de Clientes
            Escolha = menu(titulo,True,f"{len(CLIENTES)} Clientes Registrado(s)",CLIENTES,**Escolha)

            if Escolha == REGISTRO_CLIENTES["Procurar"]: # Menu » Cliente » Registro de Clientes » Procurar
                cabecalho(titulo)
                buffer = conteudo("Clientes", *procura_em_inst(CLIENTES, formatar("Registro, CPF ou Nome: ", "verde")))
                Escolha = comando(**Escolha[1])

                if Escolha == REGISTRO_CLIENTES["Editar"]: # Menu » Cliente » Registro de Clientes » Procurar » Editar
                    buffer = selecionar_lista(list(buffer), True)
                    try:
                        buffer.editar_valores()
                    except:
                        continue

                elif Escolha == REGISTRO_CLIENTES["Excluir"]:  # Menu » Cliente » Registro de Clientes » Excluir
                    buffer = selecionar_lista(list(buffer), True, registro=True)
                    del Banco_de_dados.dados_clientes[buffer]
                    continue

                else:
                    continue

            elif Escolha == REGISTRO_CLIENTES["Editar"]: # Menu » Cliente » Registro de Clientes » Editar
                buffer = selecionar_lista(list(buffer), True)
                try:
                    buffer.editar_valores()
                except:
                    continue

            elif Escolha == REGISTRO_CLIENTES["Excluir"]:  # Menu » Cliente » Registro de Clientes » Excluir
                buffer = selecionar_lista(list(buffer), True, registro = True)
                del Banco_de_dados.dados_clientes[buffer]
                continue

            else:
                continue


    elif Escolha == opcoes["Motocicletas"]: # Menu » Motocicletas
        titulo = "Motocicletas"
        buffer = MOTOCICLETAS
        Escolha = menu(titulo,**Escolha)

        if Escolha == OPCOES_MOTO["Novo Produto"]: # Menu » Motocicletas » Novo Produto
            MOTOCICLETAS.append(novo_produto())
            continue

        elif Escolha == OPCOES_MOTO["Registro de Motocicletas"]: # Menu » Motocicletas » Registro de Motocicletas
            Escolha = menu(titulo,True,f"{len(MOTOCICLETAS)} Motocicletas Cadastrada(s)",MOTOCICLETAS, **Escolha)


            if Escolha == REGISTRO_MOTO["Procurar"]: # Menu » Motocicletas » Registro de Motocicletas » Procurar
                cabecalho(titulo)
                buffer = conteudo("Motocicletas", *procura_em_inst(MOTOCICLETAS, formatar("Registro, Modelo ou Ano: ", "verde")))
                Escolha = comando(**Escolha[1])

                if Escolha == REGISTRO_MOTO["Editar"]: # Menu » Motocicletas » Registro de Motocicletas » Procurar » Editar
                    buffer = selecionar_lista(list(buffer), True)
                    try:
                        buffer.editar_valor()
                    except:
                        continue

                elif Escolha == REGISTRO_MOTO["Excluir"]:  # Menu » Motocicletas » Registro de Motocicletas » Excluir
                    buffer = selecionar_lista(list(buffer), True, registro=True)
                    del Banco_de_dados.dados_produtos[buffer]
                    continue

                else:
                    continue

            elif Escolha == REGISTRO_MOTO["Editar"]:  # Menu » Motocicletas » Registro de Motocicletas » Editar
                buffer = selecionar_lista(buffer, True)
                try:
                    buffer.editar_valor()
                except:
                    continue

            elif Escolha == REGISTRO_MOTO["Excluir"]:  # Menu » Motocicletas » Registro de Motocicletas » Excluir
                buffer = selecionar_lista(list(buffer), True, registro=True)
                del Banco_de_dados.dados_produtos[buffer]
                continue

            else:
                continue


        else:
            continue


    elif Escolha == opcoes["Vendas"]: # Menu » Vendas
        titulo = "Vendas"
        buffer = VENDAS
        Escolha = menu(titulo,**Escolha)

        if Escolha == OPCOES_VENDA["Nova Venda"]: # Menu » Vendas » Nova Venda
            VENDAS.append(nova_venda(CLIENTES, MOTOCICLETAS))
            pass


        elif Escolha == OPCOES_VENDA["Registro de Vendas"]: # Menu » Vendas » Registro de Venda
            Escolha = menu(titulo,True,F"{len(VENDAS)} x Vendas Registradas",VENDAS, **Escolha)

            if Escolha == REGISTRO_VENDAS["Procurar"]:  # Menu » Vendas » Registro de Vendas » Procurar
                cabecalho(titulo)
                buffer = conteudo("Vendas",*procura_em_inst(VENDAS, formatar("Registro de Venda, Cliente ou Motocicleta: ", "verde")))
                Escolha = comando(**Escolha[1])

                if Escolha == REGISTRO_VENDAS["Editar"]:  # Menu » Vendas » Registro de Vendas » Procurar » Editar
                    buffer = selecionar_lista(list(buffer), True)
                    try:
                        buffer.editar_venda()
                    except:
                        continue
                else:
                    continue


            elif Escolha == REGISTRO_VENDAS["Editar"]:  # Menu » Vendas » Registro de Vendas » Editar
                buffer = selecionar_lista(buffer, True)
                try:
                    buffer.editar_venda()
                except:
                    continue
            else:
                continue



print("Encerrando")
