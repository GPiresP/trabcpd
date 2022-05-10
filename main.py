import os

import pandas as pd
#import numpy as np


class Municipio:

    def __init__(self, exerc, ano_apur, cod, nome, iegm, iplan, ifisc, ieduc, isaude, iamb, icid, igov):

        self.cod = cod
        self.nome = nome

        self.exerc = exerc
        self.apur = ano_apur

        self.iegm = iegm
        self.iplan = iplan
        self.ifisc = ifisc
        self.ieduc = ieduc
        self.isaude = isaude
        self.iamb = iamb
        self.icid = icid
        self.igov = igov

def part(arr_mun, l, h):
    i = (l - 1)
    p = arr_mun[h].cod

    for j in range(l, h):

        if arr_mun[j].cod <= p:

            i += 1
            arr_mun[i], arr_mun[j] = arr_mun[j], arr_mun[i]

    arr_mun[i + 1], arr_mun[h] = arr_mun[h], arr_mun[i + 1]

    return (i + 1)

def quickMun(arr_mun, l, h):
    if len(arr_mun) == 1:
        return arr_mun

    if l < h:

        pi = part(arr_mun, l, h)

        quickMun(arr_mun, l, pi - 1)

        quickMun(arr_mun, pi + 1, h)

def munBinSearch(arr_mun, mun):
    l = 0
    r = len(arr_mun) - 1

    while l <= r:
        m = l + (r - l)/2

        m = int(m)

        res = -1

        if (mun == (arr_mun[m].nome)):
            res = 0

        if (res == 0):
            return m

        if mun > arr_mun[m].nome:
            l = m + 1

        else:
            r = m - 1

    return -1

estado = 1

while estado != 0:

    #escolha de tarefa
    if estado == 1:

        print("Digite a opção desejada:")
        print("\t1 - Carregar arquivo .xsl e gerar um novo arquivo de dados.")
        print("\t2 - Carregar arquivo de dados gerado previamente.")
        print("\t3 - Sair.")

        opc = input()

        if opc == '1':
            os.system('cls')
            estado = 2
        elif opc == '2':
            os.system('cls')
            estado = 4
        elif opc == '3':
            estado = 0
            os.system('cls')
            print("Encerrando programa.")
        else:
            os.system('cls')
            print("A opção escolhida não foi válida, por favor escolha novamente.")

    #abertura do arquivo base
    elif estado == 2:

        print("Digite o nome do arquivo que deseja abrir:")

        f_nome = input()

        if os.path.isfile(f_nome):
            df = pd.read_excel(f_nome)
            estado = 3
            os.system('cls')
        else:
            os.system('cls')
            print("Arquivo não encontrado, por favor tente novamente.")

    #criação do arquivo processado
    elif estado == 3:

        print("Digite o nome para o arquivo a ser gerado:")

        f_nome = input()

        f_novo = open(f_nome, 'w')

        i = 0

        mun_lista = []

        while i < df.shape[0]:
            mun_lista.append(Municipio(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7], df.iloc[i, 8], df.iloc[i, 9], df.iloc[i, 10], df.iloc[i, 11]))

            f_novo.write(mun_lista[i].nome + ";")
            f_novo.write(str(mun_lista[i].cod) + ";")
            f_novo.write(str(mun_lista[i].exerc) + ";")
            f_novo.write(str(mun_lista[i].apur) + ";")
            f_novo.write(mun_lista[i].iegm + ";")
            f_novo.write(mun_lista[i].iplan + ";")
            f_novo.write(mun_lista[i].ifisc + ";")
            f_novo.write(mun_lista[i].ieduc + ";")
            f_novo.write(mun_lista[i].isaude + ";")
            f_novo.write(mun_lista[i].iamb + ";")
            f_novo.write(mun_lista[i].icid + ";")
            f_novo.write(mun_lista[i].igov + "\n")

            i += 1

        f_novo.close()

        os.system('cls')
        print("Arquivo gerado com sucesso.")

        estado = 1

    #leitura do arquivo processado
    elif estado == 4:
        print("Digite o nome do arquivo que deseja abrir:")

        f_nome = input()

        if os.path.isfile(f_nome):
            f_carg = open(f_nome, 'r')
            estado = 5
            os.system('cls')
        else:
            os.system('cls')
            print("Arquivo não encontrado, por favor tente novamente.")

    #criação da lista com base no arquivo
    elif estado == 5:

        mun_lista_carg = []

        while (line := f_carg.readline().rstrip()):
            split_string = line.split(";")

            mun_lista_carg.append(Municipio(split_string[2], split_string[3], split_string[1], split_string[0], split_string[4], split_string[5], split_string[6], split_string[7], split_string[8], split_string[9], split_string[10], split_string[11]))

        estado = 6

        os.system('cls')
        print("Arquivo lido com sucesso.")

    #escolha de pesquisa/ordenamento
    elif estado == 6:

        print("Digite a opção desejada:")
        print("\t1 - Ordenar os dados em relação a um parâmetro.")
        print("\t2 - Pesquisar dados com base em algum parâmetro.")

        opc = input()

        if opc == '1':
            os.system('cls')
            estado = 7
        elif opc == '2':
            os.system('cls')
            estado = 8
        else:
            os.system('cls')
            print("A opção escolhida não foi válida, por favor escolha novamente.")

    #escolha do parâmetro de ordenamento
    elif estado == 7:

        print("Digite a opção desejada:")
        print("\t1  - Ordenar os dados em relação ao nome dos municípios.")
        print("\t2  - Ordenar os dados em relação ao código dos municípios.")
        print("\t3  - Ordenar os dados em relação ao índice de efetividade de gestão municipal.")
        print("\t4  - Ordenar os dados em relação ao índice de planejamento.")
        print("\t5  - Ordenar os dados em relação ao índice de gestão fiscal.")
        print("\t6  - Ordenar os dados em relação ao índice educacional.")
        print("\t7  - Ordenar os dados em relação ao índice de saúde.")
        print("\t8  - Ordenar os dados em relação ao índice de meio ambiente.")
        print("\t9  - Ordenar os dados em relação ao índice de defesa civil.")
        print("\t10 - Ordenar os dados em relação ao índice de tecnologia.")

        opc = input()

        if opc == '1':
            i = 0

            os.system('cls')

            print("Lista ordenada em relação aos nomes dos municípios.")
            print("Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            while i < len(mun_lista_carg):
                print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " + mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '2':
            mun_lista_temp = mun_lista_carg

            quickMun(mun_lista_temp, 0, len(mun_lista_temp) - 1)

            os.system('cls')

            print("Lista ordenada em relação aos códigos dos municípios.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_temp):
                print(mun_lista_temp[i].nome + " || " + str(mun_lista_temp[i].cod) + " || " + mun_lista_temp[i].iegm + " || " + mun_lista_temp[
                    i].ieduc + " || " + mun_lista_temp[i].isaude + " || " + mun_lista_temp[i].iplan + " || " +
                      mun_lista_temp[i].ifisc + " || " + mun_lista_temp[i].iamb + " || " + mun_lista_temp[
                          i].icid + " || " + mun_lista_temp[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '3':
            os.system('cls')
            print("Lista ordenada em relação ao índice de efetividade de gestão municipal.")
            print("Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iegm == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " + mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iegm == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " + mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iegm == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " + mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iegm == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " + mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iegm == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " + mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '4':
            os.system('cls')
            print("Lista ordenada em relação ao índice de planejamento.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iplan == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iplan == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iplan == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iplan == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iplan == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '5':
            os.system('cls')
            print("Lista ordenada em relação ao índice de gestão fiscal.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ifisc == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ifisc == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ifisc == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ifisc == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ifisc == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '6':
            os.system('cls')
            print("Lista ordenada em relação ao índice educacional.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ieduc == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ieduc == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ieduc == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ieduc == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].ieduc == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '7':
            os.system('cls')
            print("Lista ordenada em relação ao índice de saúde.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].isaude == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].isaude == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].isaude == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].isaude == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].isaude == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '8':
            os.system('cls')
            print("Lista ordenada em relação ao índice de meio ambiente.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iamb == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iamb == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iamb == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iamb == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].iamb == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '9':
            os.system('cls')
            print("Lista ordenada em relação ao índice de defesa civil.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].icid == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].icid == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].icid == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].icid == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].icid == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        elif opc == '10':
            os.system('cls')
            print("Lista ordenada em relação ao índice de tecnologia.")
            print(
                "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].igov == 'A':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].igov == "B+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].igov == 'B':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].igov == "C+":
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            i = 0

            while i < len(mun_lista_carg):

                if mun_lista_carg[i].igov == 'C':
                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " + mun_lista_carg[
                        i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " + mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[i].igov)

                i += 1

            input("Pressione Enter para continuar.")

        else:
            os.system('cls')
            print("Opção inválida, por favor escolha novamente.")

        estado = 1

    elif estado == 8:

        print("Digite a opção desejada:")
        print("\t1  - Pesquisar em relação ao nome dos municípios.")
        print("\t2  - Pesquisar em relação ao código dos municípios.")
        print("\t3  - Pesquisar em relação ao índice de efetividade de gestão municipal.")
        print("\t4  - Pesquisar em relação ao índice de planejamento.")
        print("\t5  - Pesquisar em relação ao índice de gestão fiscal.")
        print("\t6  - Pesquisar em relação ao índice educacional.")
        print("\t7  - Pesquisar em relação ao índice de saúde.")
        print("\t8  - Pesquisar em relação ao índice de meio ambiente.")
        print("\t9  - Pesquisar em relação ao índice de defesa civil.")
        print("\t10 - Pesquisar em relação ao índice de tecnologia.")

        opc = input()

        if opc == '1':
            os.system('cls')

            print("Digite o nome a ser pesquisado:")
            nom_pesq = input()

            ind_pesq = munBinSearch(mun_lista_carg, nom_pesq)

            if ind_pesq != -1:
                os.system('cls')
                print("Resultado da pesquisa:")
                print("Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                print(mun_lista_carg[ind_pesq].nome + "\t|| " + str(mun_lista_carg[ind_pesq].cod) + " || " + mun_lista_carg[
                        ind_pesq].iegm + " || " + mun_lista_carg[ind_pesq].ieduc + " || " + mun_lista_carg[ind_pesq].isaude + " || " +
                          mun_lista_carg[ind_pesq].iplan + " || " + mun_lista_carg[ind_pesq].ifisc + " || " + mun_lista_carg[
                              ind_pesq].iamb + " || " + mun_lista_carg[ind_pesq].icid + " || " + mun_lista_carg[ind_pesq].igov)

                input("Pressione Enter para continuar.")
                estado = 1

            else:
                os.system('cls')
                print("Nenhuma entrada correspondente encontrada.")
                estado = 1

        elif opc == '2':
            os.system('cls')

            print("Digite o código a ser pesquisado:")
            cod_pesq = input()

            i = 0
            find = 0

            while i < len(mun_lista_carg) and find == 0:
                if mun_lista_carg[i].cod == cod_pesq:
                    os.system('cls')
                    print("Resultado da pesquisa:")
                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                          mun_lista_carg[
                              i].iegm + " || " + mun_lista_carg[i].ieduc + " || " + mun_lista_carg[
                              i].isaude + " || " +
                          mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                          mun_lista_carg[
                              i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                              i].igov)


                    input("Pressione Enter para continuar.")
                    estado = 1
                    find = 1

                else:
                    i += 1

            if find == 0:
                os.system('cls')
                print("Nenhuma entrada correspondente encontrada.")
                estado = 1

        elif opc == '3':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print("Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].iegm == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        elif opc == '4':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].iplan == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        elif opc == '5':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].ifisc == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        elif opc == '6':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].ieduc == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        elif opc == '7':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].isaude == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        elif opc == '8':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].iamb == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        elif opc == '9':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].icid == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        elif opc == '10':
            not_ok = 0

            while not_ok == 0:
                print("Digite a nota que deseja pesquisar (A, B+, B, C+ ou C):")
                not_pesq = input()

                if not_pesq == 'A' or not_pesq == "B+" or not_pesq == 'B' or not_pesq == "C+" or not_pesq == 'C':
                    not_ok = 1

                    i = 0

                    print(
                        "Nome do Município || Código do Município || i-EGM || i-Educ || i-Saúde || i-Plan || i-Fiscal || i-Amb || i-Cidade || i-Gov TI ||")

                    while i < len(mun_lista_carg):
                        if mun_lista_carg[i].igov == not_pesq:
                            print(mun_lista_carg[i].nome + "\t|| " + str(mun_lista_carg[i].cod) + " || " +
                                  mun_lista_carg[
                                      i].iegm + " || " + mun_lista_carg[i].ieduc + " || " +
                                  mun_lista_carg[
                                      i].isaude + " || " +
                                  mun_lista_carg[i].iplan + " || " + mun_lista_carg[i].ifisc + " || " +
                                  mun_lista_carg[
                                      i].iamb + " || " + mun_lista_carg[i].icid + " || " + mun_lista_carg[
                                      i].igov)
                        i += 1

                    input("Pressione Enter para continuar.")
                    estado = 1

                else:
                    os.system('cls')
                    print("Por favor digite uma nota válida.")

        else:
            os.system('cls')
            print("A opção escolhida não foi válida, por favor escolha novamente.")















