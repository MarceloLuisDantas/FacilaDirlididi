from os import system, path
from typing import List
from sys import argv

def formata_nome(nome: str) -> str :
    nomes = nome.split(" ")
    nomes_capitalize = list(map(lambda x : x.capitalize(), nomes))
    return "".join(nomes_capitalize)

def le_facila_file() -> List :
    try :
        facila = open(path.expanduser("~/.facila.txt"), "r")
        linhas = facila.readlines()
        token = linhas[0]
        nome = linhas[1]
        matricula = linhas[2]
        facila.close()
        return token.strip(), nome.strip(), matricula.strip()
    except :
        print("Arquivo .facila.txt não encontrado ou com problema")
        print("Digite 'facila config-file' para corrigir")

def le_info_projeto() -> List :
    try :
        info = open(path.expanduser("./.info.txt"), "r")
        linhas = info.readlines()
        token = linhas[0]
        nome = linhas[1]
        info.close()
        return token.strip(), nome.strip()
    except :
        print("Arquivo .info.txt não encontrado ou com problema")

def main() :
    modo = argv[1]
    if modo == "help" :
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
        print("   | facila config-file ")
        print("   |--- Ira inciar o processo para reconfigurar o arquivo .facila ")
        
    elif modo == "new" :
        if len(argv) not in [3, 4] :
            print("Quantidade de parametros erradas")
            print("facila new [token da questão] [nome da questão]")
            print("facila new [token da questão]")
        else :
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
    elif modo == "submit" :
        if len(argv) == 2 :
            try :
                token, nome = le_info_projeto()
                if token != "" :
                    token_acesso, _, _ = le_facila_file()
                    system(f"python3 ~/../../bin/dirlididi.py submit {token} {token_acesso} {nome}.java")
            except :
                print("Arquivo .info não encontrado")
main()