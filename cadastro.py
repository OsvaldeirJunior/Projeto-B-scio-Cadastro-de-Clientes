

import os
cliente = [
    {"nome": "Carlos Silva", "cpf": "16899535009", "idade": 28, "login": "carlos", "senha": "123", "ativo": True},
    {"nome": "Ana Souza", "cpf": "52998224725", "idade": 34, "login": "ana", "senha": "abc", "ativo": True},
    {"nome": "Pedro Santos", "cpf": "12345678909", "idade": 22, "login": "pedro", "senha": "senha", "ativo": False},
    {"nome": "Lucas Lima", "cpf": "11144477735", "idade": 19, "login": "lucas", "senha": "123", "ativo": True},
    {"nome": "Fernanda Alves", "cpf": "93541134780", "idade": 31, "login": "fernanda", "senha": "abc", "ativo": True},

    {"nome": "Bruno Rocha", "cpf": "71460238001", "idade": 27, "login": "bruno", "senha": "123", "ativo": True},
    {"nome": "Juliana Costa", "cpf": "39053344705", "idade": 29, "login": "juliana", "senha": "abc", "ativo": False},
    {"nome": "Rafael Martins", "cpf": "15350946056", "idade": 33, "login": "rafael", "senha": "senha", "ativo": True},
    {"nome": "Patricia Gomes", "cpf": "29537914806", "idade": 40, "login": "patricia", "senha": "123", "ativo": True},
    {"nome": "Gabriel Ribeiro", "cpf": "76262358030", "idade": 21, "login": "gabriel", "senha": "abc", "ativo": True},

    {"nome": "Amanda Fernandes", "cpf": "08976943006", "idade": 26, "login": "amanda", "senha": "123", "ativo": False},
    {"nome": "Diego Carvalho", "cpf": "35719268000", "idade": 35, "login": "diego", "senha": "senha", "ativo": True},
    {"nome": "Larissa Barros", "cpf": "95175385200", "idade": 24, "login": "larissa", "senha": "abc", "ativo": True},
    {"nome": "Vinicius Melo", "cpf": "85245632104", "idade": 30, "login": "vinicius", "senha": "123", "ativo": True},
    {"nome": "Renata Pires", "cpf": "14725836993", "idade": 38, "login": "renata", "senha": "abc", "ativo": False},

    {"nome": "Thiago Nunes", "cpf": "96385274100", "idade": 28, "login": "thiago", "senha": "senha", "ativo": True},
    {"nome": "Camila Freitas", "cpf": "78945612366", "idade": 23, "login": "camila", "senha": "123", "ativo": True},
    {"nome": "Eduardo Teixeira", "cpf": "32165498700", "idade": 36, "login": "eduardo", "senha": "abc", "ativo": False},
    {"nome": "Beatriz Moura", "cpf": "45612378950", "idade": 27, "login": "beatriz", "senha": "senha", "ativo": True},
    {"nome": "Rodrigo Duarte", "cpf": "85274196300", "idade": 41, "login": "rodrigo", "senha": "123", "ativo": True},

    {"nome": "Marcos Araujo", "cpf": "74185296369", "idade": 32, "login": "marcos", "senha": "abc", "ativo": True},
    {"nome": "Daniela Batista", "cpf": "36925814706", "idade": 29, "login": "daniela", "senha": "senha", "ativo": False},
    {"nome": "Felipe Andrade", "cpf": "15935748608", "idade": 26, "login": "felipe", "senha": "123", "ativo": True},
    {"nome": "Carla Rezende", "cpf": "25814736900", "idade": 34, "login": "carla", "senha": "abc", "ativo": True},
    {"nome": "Paulo Mendes", "cpf": "65498732100", "idade": 45, "login": "paulo", "senha": "senha", "ativo": False},

    {"nome": "Sandra Lopes", "cpf": "75315984200", "idade": 37, "login": "sandra", "senha": "123", "ativo": True},
    {"nome": "Igor Farias", "cpf": "95135784249", "idade": 22, "login": "igor", "senha": "abc", "ativo": True},
    {"nome": "Tatiane Correia", "cpf": "45685296307", "idade": 31, "login": "tatiane", "senha": "senha", "ativo": False},
    {"nome": "Leonardo Borges", "cpf": "25836914700", "idade": 39, "login": "leonardo", "senha": "123", "ativo": True},
    {"nome": "Vanessa Cardoso", "cpf": "14736925800", "idade": 28, "login": "vanessa", "senha": "abc", "ativo": True},
]

def formatar_cpf(cpf):
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    resultado_ant = []
    for cpf_format in cpf:
        if cpf_format in numeros:
            resultado_ant.append(cpf_format)
        else:
            continue

    cpf_ok = "".join(resultado_ant)
    return cpf_ok

def verificar_cpf_valido(cpf):
    cpf_ok = formatar_cpf(cpf)
    if len(cpf_ok) == 11:
        #print("CPF VALIDO 11 DIGITOS")
        return True
    else:
        print("CPF INVALIDO insira 11 digitoss")
        return False
    
def vericar_cpf_valido_avancado(cpf):
    valida_quantidade_cpf = verificar_cpf_valido(cpf)
    cpf_na_lista = formatar_cpf(cpf)
    for cpf_lista in cliente:
        if cpf_na_lista == cpf_lista["cpf"]:
            print("CPF JA CADASTRADO")
            return False
    else:
        if valida_quantidade_cpf:
            cpf_separado = []
            cpf123 = formatar_cpf(cpf)
            for cpf_2 in cpf123:
                cpf_separado.append(int(cpf_2))

            L = (cpf_separado[0] * 10 + cpf_separado[1] * 9 + cpf_separado[2] * 8 + cpf_separado[3] * 7 + cpf_separado[4] * 6 + cpf_separado[5] * 5 + cpf_separado[6] * 4 + cpf_separado[7] * 3 + cpf_separado[8] * 2 )
            Z = (cpf_separado[0] * 11 + cpf_separado[1] * 10 + cpf_separado[2] * 9 + cpf_separado[3] * 8 + cpf_separado[4] * 7 + cpf_separado[5] * 6 + cpf_separado[6] * 5 + cpf_separado[7] * 4 + cpf_separado[8] * 3 + cpf_separado[9] * 2)

            R = L % 11
            Zr = Z % 11

            Zx = 11 - Zr
            X = 11 - R

            if X >= 10:
                X = 0
            if Zx >= 10:
                Zx = 0

            if X == cpf_separado[9] and Zx == cpf_separado[10]:
                #print("CPF Válido")
                return True
            else:
                print("CPF Inválido")
                return False
        else:
            return False
    
def formatar_nome(nome):
    nome_passo_um = nome.lower().split()
    execoes = ["das","dos","da","do","de"]
    resultado = []

    for nome_passo_dois in nome_passo_um:
        if nome_passo_dois in execoes:
            resultado.append(nome_passo_dois)
        else:
            resultado.append(nome_passo_dois.capitalize())

    nome_formatado = " ".join(resultado)
    return nome_formatado

def verificar_nome_existe_lista(nome_verificador):
    for nome_na_lista in cliente:
        if nome_verificador == nome_na_lista["nome"]:
            return False
    else:
        return True

def verificar_nome(nome_cadastro):
    quantidade_palavras = nome_cadastro.split()
    verificar_existe = verificar_nome_existe_lista(nome_cadastro)
    if verificar_existe:

        if len(quantidade_palavras) == 3:
            return True
        elif len(quantidade_palavras) == 2:
            return True
        else:
            print("Insira nome e sobrenome!\n")
            return False
    else:
        print("Nome ja existe na lista!\n")
        return False

def verificar_idade(idade):
    if idade > 120:
        print("Idade inválida\n")
        cor_vermelha()
        return False
    else:
        return True

def cadastro_cliente(nome_cadastro,cpf,idade,login,senha):
    nome_situacao = verificar_nome(nome_cadastro)
    cpf_situacao = vericar_cpf_valido_avancado(cpf)
    situacao_idade = verificar_idade(idade)
    if nome_situacao and cpf_situacao and situacao_idade:
        novo_cliente = {"nome" : nome_cadastro,"cpf" : cpf,"idade" : idade,"login" : login,"senha" : senha,"ativo" : True}
        cliente.append(novo_cliente)
        print("Cadastro realizado com sucesso!")
        cor_branca()
    else:
        cor_vermelha()
        print("Não foi possivel realizar o cadastro")

def lista_clientes():
    print("-=-=-=-=-=-=-=-=-=-CLIENTES=-=-=-=-=-=-=-=-=-=-")
    for pessoa in cliente:
        if pessoa["ativo"] == True:
            cpf1 = pessoa["cpf"]
            cpf_formatado = "{}.{}.{}-{}".format(cpf1[:3],cpf1[3:6],cpf1[6:9],cpf1[9:]) 
            print(f"""
    Nome:{pessoa["nome"]}
    CPF:{cpf_formatado}
    Idade:{pessoa["idade"]}
    Ativo: {pessoa["ativo"]}""")
        else:
            continue
    print(" ")

def lista_cliente_alteracao():
    print("-=-=-=-=-=-=-=-=-=-CLIENTES=-=-=-=-=-=-=-=-=-=-")
    for pessoa in cliente:
        cpf1 = pessoa["cpf"]
        cpf_formatado = "{}.{}.{}-{}".format(cpf1[:3],cpf1[3:6],cpf1[6:9],cpf1[9:]) 
        print(f"""
Nome:{pessoa["nome"]}
CPF:{cpf_formatado}
Idade:{pessoa["idade"]}
Ativo: {pessoa["ativo"]}""")
    print(" ")

def buscar_cliente_nome(nome):
    nome_formatado = formatar_nome(nome)
    verificar = verificar_nome_existe_lista(nome_formatado)
    if not verificar:
        for nomes in cliente:
            if nome_formatado == nomes["nome"]:
                nome_encotrado = (f"""
=-=-=-=-=-=DADOS ENCONTRADOS=-=-=-=-=-=
Nome:{nomes['nome']}
CPF:{nomes['cpf']}
Idade:{nomes['idade']}
Ativo:{nomes['ativo']}
""")
                return nome_encotrado
    else:
        return False

def buscar_cliente_cpf(cpf):
    valida = True
    for cpf_busca in cliente:
        if cpf == cpf_busca["cpf"]:
            cpf_encontrado = (f"""
=-=-=-=-=-=DADOS ENCONTRADOS=-=-=-=-=-=
Nome:{cpf_busca['nome']}
CPF:{cpf_busca['cpf']}
Idade:{cpf_busca['idade']}
Ativo:{cpf_busca['ativo']}
""")
            return cpf_encontrado
    else:
        return False

def alterar_nome(cpf,novo_nome_user):
    for novo_nome in cliente:   
        if cpf == novo_nome["cpf"]:
            novo_nome["nome"] = novo_nome_user
            return True
    else:
        print("Algo deu errado...")
        return False
        
    print("Em desenvolvimeto")

def alterar_cpf(cpf_escolhido):
    while True:
        sair = False
        novo_cpf = input("Insira o novo CPF: ")
        novo_cpf_formatado = formatar_cpf(novo_cpf)
        verificar_novo_cpf_na_lista = vericar_cpf_valido_avancado(novo_cpf_formatado)
        if novo_cpf == "0":
            break
        else:
            if verificar_novo_cpf_na_lista:
                for novo_cpf1 in cliente:
                    if cpf_escolhido == novo_cpf1["cpf"]:
                        novo_cpf1["cpf"] = novo_cpf_formatado
                        print("Alteração realizada com sucesso!")
                        pausa()
                        sair = True
                        break
                else:
                    pausa()
                    continue
            if sair == True:
                break
            else:
                print("\033[31mPressione 0 p/ voltar\033[0m")
                continue

        #input 0 sair

def verifar_cpf_cadastrado(cpf_user):
    for lista_cliente in cliente:
        if cpf_user == lista_cliente["cpf"]:
            return True
    else:
        return False

def alterar_idade(idade,cpf):
    if idade > 120:
        return False
    else:
        for lista_cliente in cliente:
            if cpf == lista_cliente["cpf"]:
                lista_cliente["idade"] = idade
                return True
            else:
                continue

def alterar_login(login,cpf):
    for dicionario_cliente in cliente:
        if cpf == dicionario_cliente["cpf"]:
            if dicionario_cliente["login"] == login:
                return False
            else:
                dicionario_cliente["login"] = login
                return True
        else:
            continue

def alterar_senha(senha,cpf):
    for dicionario_cliente in cliente:
        if cpf == dicionario_cliente["cpf"]:
            if dicionario_cliente["senha"] == senha:
                return False
            else:
                dicionario_cliente["senha"] = senha
                return True
        else:
            continue

def ativar_user(cpf):
    for lista_cliente in cliente:
        if cpf == lista_cliente["cpf"]:
            if lista_cliente["ativo"] == True:
                return False
            else:
                lista_cliente["ativo"] = True
                return True
        else:
            continue

def desativar_user(cpf):
    for lista_cliente in cliente:
        if cpf == lista_cliente["cpf"]:
            if lista_cliente["ativo"] == False:
                return False
            else:
                lista_cliente["ativo"] = False
                return True
        else:
            continue

def pausa():
    input("Pressione enter p/ continuar...")

def limpar_cmd():
    os.system("cls")

def cor_vermelha():
    os.system("color 4")

def cor_branca():
    os.system("color 7")

LOGIN_USER = "Osvaldo"
LOGIN_PASSWORD = "gm123"

while True:
    limpar_cmd()
    cor_branca()
    escolha_usuario_login = input("""
-=-=-=-=-=-=-=-=-=-LOGIN CADASTRO CLIENTES=-=-=-=-=-=-=-=-=-=-
1.Realizar Login
2.Alterar senha
0.Sair
Escolha: """)
    if escolha_usuario_login == "1":
        login = input("Login: ")# "Osvaldo"#input("Insira seu login: ")
        senha = input("Senha: ") #gm123#input("Insira a senha: ")

        if login == LOGIN_USER and senha == LOGIN_PASSWORD:
            print("Login realizado")
            while True:
                limpar_cmd()
                cor_branca()
                escolha_usuario = input("""
-=-=-=-=-=-=-=-=-=-SISTEMA CADASTRO CLIENTES=-=-=-=-=-=-=-=-=-=-
Escolha a função desejada:
1.Cadastrar cliente
2.Listar clientes
3.Buscar cliente
4.Alterar cadastro cliente
0.Sair
Escolha: """)
                if escolha_usuario == "1":
                    while True:
                        nome_cliente = input("Nome: ")
                        if nome_cliente.replace(" ","").isalpha():
                            cor_branca()
                            break
                        else:
                            print("insira somente letras")
                            cor_vermelha()
                            pausa()
                    nome_cliente_formatado = formatar_nome(nome_cliente)
                    
                    while True:
                        cpf_teste = input("CPF: ")   
                        if cpf_teste.isalpha():
                            print("Insira somente numero e simbolos")
                        else:
                            cpf_teste
                            break

                    try:
                        idade = int(input("Idade: "))
                        cor_branca()
                    except ValueError as e:
                        print(f"Insira um valor valido p/ idade")
                        cor_vermelha()
                        continue
                    cpf_teste1 = formatar_cpf(cpf_teste)
                    login = ("Login User: ") #falta botar input esta sem pra dev
                    senha = ("Senha User: ")

                    cadastro_cliente(nome_cliente_formatado,cpf_teste1,idade,"teste","123")
                    pausa()

                elif escolha_usuario == "2": 
                    lista_clientes()
                    pausa()

                elif escolha_usuario == "3":#busca
                    while True:
                        limpar_cmd()
                        escolha_busca_usuario = input("""
Qual meio de busca deseja:
1.Nome
2.CPF
0.Voltar
Escolha: """)
                        if escolha_busca_usuario == "1":
                            while True:
                                nome_busca = input("Insira nome p/ consulta: ")
                                if nome_busca.replace(" ","").isalpha():
                                    break
                                else:
                                    print("Insira um nome válido")

                            nome_buscar_def = buscar_cliente_nome(nome_busca)

                            if nome_buscar_def:
                                print(nome_buscar_def)
                                pausa()
                            else:
                                print("Nome não encontrado")
                                pausa()

                        elif escolha_busca_usuario == "2":
                            while True:
                                cpf_busca = input("Insira cpf p/ consulta: ")
                                cpf_buscar_formatado = formatar_cpf(cpf_busca)

                                if cpf_busca == "0":
                                    break
                                if cpf_busca.replace(" ","").isalpha():
                                    print("CPF inválido insira - (Numeros e '.','-') \033[31mPressione 0 p/ voltar\033[0m")
                                    continue
                                elif len(cpf_buscar_formatado) == 11:
                                    break
                                else:
                                    print("Insira 11 digitos - \033[31mPressione 0 p/ voltar\033[0m")
                                    continue

                            guardar_valor_cpf = buscar_cliente_cpf(cpf_buscar_formatado)
                            if guardar_valor_cpf:
                                print(guardar_valor_cpf)
                                pausa()
                            else:
                                print("Não encontrado")
                                pausa()


                        elif escolha_busca_usuario == "0":
                            break

                elif escolha_usuario == "4":#alterar
                    print("\033[32mFunção em desenvolvimento\033[0m")
                    lista_cliente_alteracao()
                    print("\nInsira o cpf do Usuario que será realizado a alteração!")
                    while True: 
                        cpf_p_alterar = input("CPF: ")
                        cpf_alterar_formatado = formatar_cpf(cpf_p_alterar)
                        if len(cpf_alterar_formatado) == 11:
                            break
                        else:
                            print("Insira 11 Digitos")
                            continue

                    verificar_cpf_na_lista = verifar_cpf_cadastrado(cpf_alterar_formatado)

                    if verificar_cpf_na_lista:
                        while True:
                            limpar_cmd()
                            cliente_escolhido = buscar_cliente_cpf(cpf_alterar_formatado)
                            print(cliente_escolhido)
                            escolha_usuario_alteracao = input(f"""
Escolha oque deseja alterar no Usuario: 
    1.Nome
    2.CPF
    3.Idade
    4.Login
    5.Senha
    6.Ativar usuário
    7.Desativar usuário
    0.Voltar                                                     
Escolha: """)


                            if escolha_usuario_alteracao == "1":
                                while True:
                                    novo_nome_user = input("Novo nome Usuario: ")
                                    novo_nome_verificado = novo_nome_user.replace(" ","").isalpha()
                                    if novo_nome_verificado:
                                        formatar_novo_nome = formatar_nome(novo_nome_user)
                                        verificar_novo_nome = verificar_nome(formatar_novo_nome)
                                        if verificar_novo_nome:
                                            alteracao = alterar_nome(cpf_alterar_formatado,formatar_novo_nome)
                                            if alteracao:
                                                print("Alteração realizada com sucesso")
                                                pausa()
                                                break
                                            else:
                                                print("Algo deu erro")
                                                pausa()
                                                break
                                        print("Nome inválido \033[31mPressione 0 p/ voltar\033[0m")
                                        continue
                                    elif novo_nome_verificado == 0:
                                        break
                                    else:
                                        print("Nome inválido \033[31mPressione 0 p/ voltar\033[0m")
                                        continue

                            elif escolha_usuario_alteracao == "2":
                                alterar_cpf(cpf_alterar_formatado)
                                break

                            elif escolha_usuario_alteracao == "3":
                                while True:
                                    try:
                                        alterar_idade_usuario = int(input("Insira a nova idade: "))
                                        break
                                    except:
                                        print("Insira somente numeros")
                                        continue
                                verificar_nova_idade_ok = alterar_idade(alterar_idade_usuario,cpf_alterar_formatado)
                                if verificar_nova_idade_ok:
                                    print("Idade atualizada com sucesso!")
                                    pausa()
                                else:
                                    print("Insira uma idade válida!")
                                    pausa()
                            
                            elif escolha_usuario_alteracao == "4":
                                login_novo = input("Insira novo login: ")
                                verificar_login_novo = alterar_login(login_novo,cpf_alterar_formatado)
                                if verificar_login_novo:
                                    print("Login Atualizado com sucesso!")
                                    pausa()                    

                                else:
                                    print("Ultize um login diferente!")
                                    pausa()  

                            elif escolha_usuario_alteracao == "5":
                                nova_senha_usuario = input("Insira a nova senha: ")
                                alterar_senha(nova_senha_usuario,cpf_alterar_formatado)
                                if verificar_login_novo:
                                    print("Senha Atualizado com sucesso!")
                                    pausa()                    

                                else:
                                    print("Ultize uma senha diferente!")
                                    pausa()  

                            elif escolha_usuario_alteracao == "6":
                                ativar_user_new = ativar_user(cpf_alterar_formatado)
                                if ativar_user_new:
                                    print("Usuário Ativado com sucesso!")
                                    pausa()
                                else:
                                    print("Usuário já está ativo!")
                                    pausa()
                                    
                            elif escolha_usuario_alteracao == "7":
                                desativa_user_new = desativar_user(cpf_alterar_formatado)
                                if desativa_user_new:
                                    print("Usuário desativado com sucesso!")
                                    pausa()
                                else:
                                    print("Usuário ja está desativado!")
                                    pausa()

                            elif escolha_usuario_alteracao == "0":
                                break                 
                            else:
                                print("Opção inválida")
                    
                                pausa()
                    else:
                        print("Usuario não cadastrado")
                        pausa()
                        continue

                elif escolha_usuario == "0":
                    print("Saindo...")
                    break

                else:
                    print("Opção inválida")
                    pausa()

        else:
            print("Login ou Senha invalida")
            cor_vermelha()
            pausa()

    elif escolha_usuario_login == "2":
        print("Em desenvolvimento para alterar senha pae")
        pausa()

    elif escolha_usuario_login == "0":
        print("Saindo..")
        break
    else:
        print("Opção inválida")
        pausa()