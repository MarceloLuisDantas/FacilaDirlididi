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
        facila    = open(path.expanduser("~/.facila.txt"), "r")
        linhas    = facila.readlines()
        token     = linhas[0].strip()
        nome      = linhas[1].strip()
        matricula = linhas[2].strip()
        facila.close()
        return token, nome, matricula
    except :
        print("Arquivo .facila.txt não encontrado ou com problema")
        print("Digite 'facila config-file' para corrigir")

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

def salva_info(label: str, erro: str) -> bool :
    result = system(label) 
    if result != 0 :
        msg_erro(erro)
        return False
    return True

def create_facil_file() -> bool :
    print(" -- Criando arquivo .facila ")
    print(" -- Executando | touch ~/.facila.txt ")
    print(" ")
    if system("touch ~/.facila.txt") == 0 :
        print(" -- Arquivo .facila criado com sucesso ")
        print(" ")
        return True
    else :
        msg_erro("Criar arquivo de .facila")
        return False

def preenche_facila() -> bool :
    token     = get_info("Qual o seu TOKEN de acesso ao Dirlididi: ")
    nome      = get_info("Qual nome colocar nos cabeçalhos: ")
    matricula = get_info("Qual matricula colocar nos cabeçalhos: ")

    print(" ")
    print(" -- Executando | echo {seu token}     > ~/.facila.txt ")
    print(" -- Executando | echo {seu nome}      >> ~/.facila.txt ")
    print(" -- Executando | echo {sua matricula} >> ~/.facila.txt ")
    print(" ")
    
    sv_token     = salva_info(f"echo {token} > ~/.facila.txt",      "Salvar Token")    
    sv_nome      = salva_info(f"echo {nome} >> ~/.facila.txt",      "Salvar Nome")    
    sv_matricula = salva_info(f"echo {matricula} >> ~/.facila.txt", "Salvar Matricula")

    if sv_token and sv_nome and sv_matricula :
        facila = open(path.expanduser("~/.facila.txt"), "r").readlines()

        print(" ")
        print(f"    Token:     {facila[0].strip()}")
        print(f"    Nome:      {facila[1].strip()}")
        print(f"    Matricula: {facila[2].strip()}")
        print(" ")

        escolha = get_escolha("    Os valores estão corretos? [s/n]: ")

        if not escolha :
            msg_erro("Salvar Informaçaões em ~/.facila 2")
            return False
        return True

    else :
        msg_erro("Salvar Informações em ~/.facila 1")
        return False

def help() :
    print(" Facila | Facilitador de uso do Dirlididi")
    print(" Uso ")
    print('   | facila new [token da questão] "[nome da questão]"  ')
    print("   |--- Ira criar o arquivo com o nome da questão em CamelCase")
    print("   | ")
    print("   | facila new [token da questão] ")
    print("   |--- Ira criar o arquivo como Programa.java ")
    print("   | ")
    print("   | facila submit ")
    print("   |--- Ira submeter a questão local ")
    print("   | ")
    print("   | facila config ")
    print("   |--- Ira inciar o processo para reconfigurar o arquivo .facila ")

def new() :
    print(" Criando novo projeto Dirlididi")
    token = argv[2].split(" ")
    if len(token) != 1 :
        print(f"'{argv[2]}' não é um token valido")
    else :
        print("")
        if len(argv) == 4 :
            nome_formatado = formata_nome(argv[3])
            nome_formatado_pasta = nome_formatado
        else :
            nome_formatado = "Programa"
            nome_formatado_pasta = argv[2]

        system(f"mkdir ./{nome_formatado_pasta}")
        system(f"touch ./{nome_formatado_pasta}/.info.txt")
        info = open(f"./{nome_formatado_pasta}/.info.txt", "w")
        info.write(argv[2] + "\n")
        info.write(nome_formatado)
        info.close()

        system(f"touch ./{nome_formatado_pasta}/{nome_formatado}.java")
        _, nome, matricula = le_facila_file()
        template = f"""/**
* Laboratório de Programação 2 - Lab X
*
* {nome} - {matricula}
*/

public class {nome_formatado} {{
    public static void main(String[] args) {{
        System.out.println(\"Hello World!!\");
    }}
}}
"""
        java = open(f"./{nome_formatado_pasta}/{nome_formatado}.java", "w")
        java.write(template)
        java.close()

def submit() :
    try :
        token, nome = le_info_projeto()
        if token != "" :
            token_acesso, _, _ = le_facila_file()
            print("Submetendo projeto")
            system(f"python3 ~/../../bin/dirlididi.py submit {token} {token_acesso} {nome}.java")
    except :
        print("Arquivo .info não encontrado")

def config() :
    if not file_existe("~/.facila.txt") :
        create_facil_file()
    preenche_facila()

def main() :
    print(" ")
    
    modo = argv[1]
    if modo == "help" :
        help()        
        
    elif modo == "new" :
        if len(argv) not in [3, 4] :
            print("Quantidade de parametros erradas")
            print("Uso - facila new [token da questão] [nome da questão]")
            print("Uso - facila new [token da questão]")
        else :
            new()

    elif modo == "submit" :
        if len(argv) == 2 :
            submit()
        else :
            print("Quantidade de parametros erradas")
            print("Uso - facila submit ")

    elif modo == "config" :
        if len(argv) == 2 :
            config()
        else :
            print("Quantidade de parametros erradas")
            print("Uso - facila config ")

main()