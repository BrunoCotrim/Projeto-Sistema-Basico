import json


def save(file_name,modo="w+",*args):
    with open(file_name, modo) as file:
        buffer = list(args)
        json.dump(buffer,file)
        # for line in args:
        #     instancias = json.dumps(line)
        #     file.write(f"{instancias}\n")


def reload_data(file_name):
    with open(file_name, "r+") as file:
        novo_dic = json.load(file)
        return novo_dic



if __name__ == '__main__':

    cores = {"branco": " ",
             "preto": 30,
             "vermelho": 31,
             "verde": 32,
             "amarelo": 33,
             "azul": 34,
             "roxo": 35,
             "ciano": 36,
             "cinza": 37}

    save("nome.json","w+", cores)
    dicionario = reload_data("nome.json")
    print(cores)
    print(dicionario)

    # save("nome.json",jason)


