from templates import get_template
from os import system, path
from typing import List
from sys import argv

def file_existe(p: str) -> bool :
    try:
        _ = open(path.expanduser(p))
        return True
    except :
        return False

def formata_nome(nome: str) -> str :
    nomes = nome.split(" ")
    nomes_capitalize = list(map(lambda x : x.capitalize(), nomes))
    return "".join(nomes_capitalize)

def le_facila_file() -> List :
    try :
        facila    = open(path.expanduser("~/Facila/facila.txt"), "r")
        linhas    = facila.readlines()
        token     = linhas[0].strip()
        nome      = linhas[1].strip()
        matricula = linhas[2].strip()
        facila.close()
        return token, nome, matricula
    except :
        print("Arquivo facila.txt não encontrado ou com problema")
        print("Digite 'facila config' para corrigir")

def le_info_projeto() -> List :
    try :
        info   = open(path.expanduser("./.info.txt"), "r")
        linhas = info.readlines()
        token  = linhas[0].strip()
        nome   = linhas[1].strip()
        info.close()
        return token, nome
    except :
        print("Arquivo .info.txt não encontrado ou com problema")

def get_escolha(label: str) -> bool :
    ESCOLHAS = ['s', 'sim', 'n', 'não', 'nao']
    while True :
        escolha = input(label)
        if escolha.lower() in ESCOLHAS :
            print(" ")
            return escolha.lower() in ['s', 'sim']
        else :
            print(f"    '{escolha}' não é uma opção valida")

def get_info(label: str) -> str :
    while True :
        info = input(f"    {label}")
        if get_escolha(f"    Confirmar: {info}? [s/n]: ") :
            return info

def msg_erro(etapa: str) :
    print(" Algo deu errado durante o processo - ")
    print(f"     - {etapa} ")
    print(" Favor reportar ao dono do repositorio")
    exit()

def salva_info(label: str, erro: str) -> bool :
    result = system(label) 
    if result != 0 :
        msg_erro(erro)
        return False
    return True

def create_facil_file() -> bool :
    print(" -- Criando arquivo facila.txt ")
    print(" -- Executando | touch ~/facila/facila.txt ")
    print(" ")
    if system("touch ~/Facila/facila.txt") == 0 :
        print(" -- Arquivo facila.txt criado com sucesso ")
        print(" ")
        return True
    else :
        msg_erro("Criar arquivo de facila.txt")
        return False

def preenche_facila() -> bool :
    token     = get_info("Qual o seu TOKEN de acesso ao Dirlididi: ")
    nome      = get_info("Qual nome colocar nos cabeçalhos: ")
    matricula = get_info("Qual matricula colocar nos cabeçalhos: ")

    print(" ")
    print(" -- Executando | echo {seu token}     > ~/Facila/facila.txt ")
    print(" -- Executando | echo {seu nome}      >> ~/Facila/facila.txt ")
    print(" -- Executando | echo {sua matricula} >> ~/Facila/facila.txt ")
    print(" ")
    
    sv_token     = salva_info(f"echo {token} > ~/Facila/facila.txt",      "Salvar Token")    
    sv_nome      = salva_info(f"echo {nome} >> ~/Facila/facila.txt",      "Salvar Nome")    
    sv_matricula = salva_info(f"echo {matricula} >> ~/Facila/facila.txt", "Salvar Matricula")

    if sv_token and sv_nome and sv_matricula :
        facila = open(path.expanduser("~/Facila/facila.txt"), "r").readlines()

        print(" ")
        print(f"    Token:     {facila[0].strip()}")
        print(f"    Nome:      {facila[1].strip()}")
        print(f"    Matricula: {facila[2].strip()}")
        print(" ")

        escolha = get_escolha("    Os valores estão corretos? [s/n]: ")

        if not escolha :
            msg_erro("Salvar Informaçaões em ~/Facila/facila.txt 2")
        return True

    else :
        msg_erro("Salvar Informações em ~/Facila/facila.txt 1")

def get_extensao(lang: str) -> str :
    linguagens = {
        "java" : "java",
        "python" : "py",
        "haskell" : "hs",
        "prolog" : "pl",
        "c++" : "cpp",
        "c" : "c"
    }
    if lang in linguagens.keys() :
        return linguagens[lang]
    return "error"

def help() :
    print(" Facila | Facilitador de uso do Dirlididi")
    print(" Uso ")
    print('   | facila new [token da questão] "[nome da questão]"(opcional) [linguagem](opcional) ')
    print("   |--- Ira criar uma pasta e um arquivo com o nome da questão com a extenção")
    print("   |  | da linguagem especificada. Caso a linguagem for especificada, sera criado")
    print("   |  | um arquivo Java. E caso o nome da qestão também não for especificado, ")
    print("   |  | sera criado com nome de Programa.java e o nome da pasta sera o token")
    print("   | ")
    print("   | facila submit ")
    print("   |--- Ira submeter a questão local ")
    print("   | ")
    print("   | facila config ")
    print("   |--- Ira inciar o processo para reconfigurar o arquivo .facila ")
    print("   | ")
    print("   | facila run ")
    print("   |--- Ira executar o programa ")

def new() :
    print(" Criando novo projeto Dirlididi")
    token = argv[2].split(" ")
    if len(token) != 1 :
        print(f"'{argv[2]}' não é um token valido")
    else :
        extensao = "java"
        linguagem = "java"
        if len(argv) == 5 :
            linguagem = argv[4]
            extensao = get_extensao(linguagem)
            if extensao == "error" :
                msg_erro(f"Linguagem {linguagem} não conhecida")
            else :
                nome_formatado = formata_nome(argv[3])
                nome_formatado_pasta = nome_formatado
        elif len(argv) == 4 :
            nome_formatado = formata_nome(argv[3])
            nome_formatado_pasta = nome_formatado
        else :
            nome_formatado = "Programa"
            nome_formatado_pasta = argv[2]

        if system(f"mkdir ./{nome_formatado_pasta}") == 0 :
            system(f"touch ./{nome_formatado_pasta}/.info.txt")
            info = open(f"./{nome_formatado_pasta}/.info.txt", "w")
            info.write(argv[2] + "\n")
            info.write(nome_formatado + "\n")
            info.write(extensao + "\n")
            info.close()

            system(f"touch ./{nome_formatado_pasta}/{nome_formatado}.{extensao}")
            _, nome, matricula = le_facila_file()
            template = get_template(linguagem, nome, matricula, nome_formatado)
            file = open(f"./{nome_formatado_pasta}/{nome_formatado}.{extensao}", "w")
            file.write(template)
            file.close()            

def submit() :
    try :
        token, nome = le_info_projeto()
        if token != "" :
            token_acesso, _, _ = le_facila_file()
            print(f"Submetendo projeto: {token} - {nome}.java")
            system(f"python3 ~/Facila/dirlididi.py submit {token} {token_acesso} {nome}.java")
    except :
        print("Arquivo .info não encontrado")

def config() :
    if not file_existe("~/Facila/facila.txt") :
        create_facil_file()
    preenche_facila()

def run() :
    argumentos = []
    if len(argv) != 2 :
        for i in argv[2:] :
            argumentos.append(i)
    argumentos = " ".join(argumentos)

    if file_existe("./.info.txt") :
        info = open("./.info.txt").readlines()
        arquivo = info[1].strip()
        extensao = info[2].strip()
        nome_completo = f"{arquivo}.{extensao}"

        if extensao == "java" :
            print(f"Facila - Compilando: {nome_completo}")
            if system(f"javac {nome_completo}") == 0 :
                print(" Facila - OK ")
                print(f"Facila - Rodando: {nome_completo}")
                print(" ")
                system(f"java {nome_completo} {argumentos}")
        
        elif extensao == "py" :
            print(f"Facila - Rodando: {nome_completo}")
            print(" ")
            system(f"python3 {nome_completo} {argumentos}")
        
        elif extensao == "c" :
            print(f"Facila - Compilando: {nome_completo}")
            if system(f"gcc {nome_completo} -o {arquivo}") == 0 :
                print("Facila - OK")
                print(f"Facila - Rodando: {nome_completo}")
                print(" ")
                system(f"./{arquivo} {argumentos}")
       
        elif extensao == "cpp" :
            print(f"Facila - Compilando: {nome_completo}")
            if system(f"g++ {nome_completo} -o {arquivo}") == 0 :
                print("Facila - OK")
                print(f"Facila - Rodando: {nome_completo}")
                print(" ")
                system(f"./{arquivo} {argumentos}")
        
        elif extensao == "hs" :
            print(f"Facila - Compilando: {nome_completo}")
            if system(f"ghc {nome_completo}") == 0 :
                print("Facila - OK")
                print(f"Facila - Rodando: {nome_completo}")
                print(" ")
                system(f"./{arquivo} {argumentos}")
        
        elif extensao == "pl" :
            print("ainda não implementado")
        
        else :
            print("linguagem não catalogada")
    else :
        msg_erro("Arquivo .info.txt não encontrando")

def main() : 
    modo = argv[1]
    if modo == "help" :
        help()        
        
    elif modo == "new" :
        if len(argv) not in [3, 4, 5] :
            print(" Quantidade de parametros erradas")
            print("  Uso - facila new [token da questão] [nome da questão] [linguagem]")
            print("  Uso - facila new [token da questão] [nome da questão]")
            print("  Uso - facila new [token da questão]")
        else :
            new()

    elif modo == "submit" :
        if len(argv) == 2 :
            submit()
        else :
            print(" Quantidade de parametros erradas")
            print("  Uso - facila submit ")

    elif modo == "config" :
        if len(argv) == 2 :
            config()
        else :
            print(" Quantidade de parametros erradas")
            print("  Uso - facila config ")

    elif modo == "run" :
        run()    

main()
