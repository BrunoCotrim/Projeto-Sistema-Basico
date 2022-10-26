
# Fortmata textos mudando cor e adicionando sublinhado ou bold
def formatar(texto, cor="branco", **kwargs):
    style = 0
    cores = {"branco":" ",
             "preto": 30,
             "vermelho": 31,
             "verde": 32,
             "amarelo": 33,
             "azul": 34,
             "roxo": 35,
             "ciano": 36,
             "cinza": 37}
    if kwargs.get("bold"):
        style = 1
    if kwargs.get("sub"):
        style = 4

    return f"\33[{style};{cores[cor]}m{texto}\33[m"

#Procura uma string inputada entre os valores de instancias em uma lista
def procura_em_inst(lista, request = "Procurar por: "):
    search = str(input(request)).lower()
    focus = []

    for item in lista:
        for valor in item.__dict__.values():
            try:
                if item not in focus:
                    if search in valor.lower():
                        focus.append(item)
                else:
                    continue
            except:
                continue

    return focus

# Retorna o valor de uma chave de um dicionario
def selecionar_dict(**kwargs):
    run = True
    COMANDO = 0
    indice = 0

    kwargs.update({"Sair": False})
    for k,v in kwargs.items():
        indice += 1
        if v == False:
            print(formatar(f" « {indice} - Sair »", cor ='roxo'))
        else:
            print(formatar(f" « {indice} - {k} » |", cor='ciano'), end="")
    valores = tuple(kwargs.values())
    valores = list(valores)

    while True:
        try:
            COMANDO = int(input("Selecione: "))
            return valores[COMANDO - 1]
        except TypeError:
            print(formatar("Apenas numeros inteiros!", cor = "vermelho"))
        except ValueError:
            print(formatar("Por favor digite um número!", cor = "vermelho"))
        except IndexError:
            print(formatar("Por favor digite um número válido!", cor = "vermelho"))
        else:
            if COMANDO < 1 or COMANDO > len(kwargs.values()):
                print(formatar("Opção inválida!", cor = "vermelho"))

# Retorna um item de uma lista ou o seu indice
def selecionar_lista(lista, moto_cliente = False,**kwargs):
    COMANDO = 0
    indice = 0
    for opcao in lista:
        indice += 1
        if moto_cliente:
            print(formatar(f"« {indice} » | « Reg {opcao.reg} » |", cor='azul'))
        else:
            print(formatar(f"« {indice} » | {opcao} |", cor='azul'))

    indice += 1
    print(formatar(f"« {indice} » Sair", cor='roxo'))

    while True:
        try:
            COMANDO = int(input("Selecione: "))
            if COMANDO < 1 or COMANDO > len(lista)+1:
                print(formatar("Opção inválida!", cor="vermelho"))
                raise IndexError
            if COMANDO == indice:
                return True # A ultima opção é sair e se escolhida a funcao termina retornando True
            else:
                if kwargs.get("registro"):
                    return str(COMANDO)

                if kwargs.get("indice"):
                    return COMANDO - 1
                else:
                    return lista[COMANDO - 1]
        except TypeError:
            print(formatar("Apenas numeros inteiros!", cor="vermelho"))
        except ValueError:
            print(formatar("Por favor digite um número!", cor="vermelho"))
        except IndexError:
            print(formatar("Por favor digite um número válido!", cor="vermelho"))


# Exibe uma lista de valores na tela e a retorna
def conteudo(texto="Registro Padrão",*args):
    print(formatar("-" * 56))
    print(formatar(f"{texto}".center(44) , bold=True))
    print(formatar("-" * 56))
    if len(args) == 0:
        return
    for i in args:
        print(i)
    print(formatar("-" * 56))
    return args

#Cabecalho com espaco para a funcao conteudo (tabela)
def cabecalho(titulo, tabela=False,titulo_tabela = "Tabela sem nome",info="Lista Vazia"):
    texto = "SISTEMA DE VENDAS"
    print("")
    print(formatar("="*35,bold=True))
    print(formatar(f"{texto:^42}",bold=True,cor="azul"))
    print(formatar(f"----{titulo:^34}----",bold=True))

    if tabela:
        conteudo(titulo_tabela,*info)

    print(formatar("="*35,bold=True))

# Exibe opções, inputa a escolha e devolve o valor da chave
def comando(**kwargs):
    run = True
    COMANDO = 0
    indice = 0

    kwargs.update({"Voltar": True, "Sair": False})
    for opcao in kwargs.keys():
        indice += 1
        if opcao == "Sair":
            print(formatar(f"« {indice} | {opcao} »", cor='vermelho', bold=True))
        else:
            print(formatar(f"« {indice} | {opcao} »", cor='azul', bold=True))
    valores = tuple(kwargs.values())
    valores = list(valores)

    while True:
        try:
            COMANDO = int(input("Selecione: "))
            if COMANDO < 1 or COMANDO > len(kwargs.values()):
                print(formatar("Opção inválida!", cor = "vermelho"))
                raise IndexError
            return valores[COMANDO - 1]
        except TypeError:
            print("Apenas numeros inteiros!")
        except ValueError:
            print("Por favor digite um número!")
        except IndexError:
            print("Por favor digite um número válido!")
        else:
            if COMANDO < 1 or COMANDO > len(kwargs.values()):
                print("Opção inválida!")

# Cabecalho, conteudo e comando unidas
def menu(titulo, tabela=False, tit_tabela="Nome Tabela" , info="Vazio", **kwargs):
    cabecalho(titulo, tabela, tit_tabela, info)
    return comando(**kwargs)

from ap2.lib.interface import load_reload as arquivo
from ap2.lib.interface.class_and_object import *
import json

if __name__ == '__main__':
    opcoes = {"Opção teste 1": "Resposta", "Opção Teste 2": True, "Opção teste 3": 1000}
    menu("Sistema Teste",**opcoes)



