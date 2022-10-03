from pathlib import Path 
import os

def file_existe(path: str) :
    comando = "cat {} > /dev/null".format(path)
    return os.system(comando)

def get_token() -> str :
    while True :
        print("")
        token = input("Digite o seu TOKEN de acesso: ")
        suporte = input("Digite novamente: ")
        if token != suporte :
            print("")
            print("Os TOKENS não são iguais")
            print("Favor, tentar novamente")
        else :
            return token

def create_token_file() -> bool :
    existe = file_existe("~/.token_dirlididi.txt")
    if existe == 0 :
        return True
    else :
        print("")
        print("Arquivo com o TOKEN de acesso ao Dirlididi não encontrado")
        print("Sem esse arquivo sempre que você for enviar uma atividade")
        print("sera preciso informar o seu TOKEN de acesso")
        print("")
        escolha = input("Deseja criar o arquivo com o TOKEN de Acesso? [s/n]: ")
        if escolha.lower() == "s" :
            print("\n ---- Executando | touch ~/.token_dirlididi.txt")
            if os.system("touch ~/.token_dirlididi.txt") == 0 :
                print("Arquivo .token_dirlididi.txt criado com sucesso")
                token = get_token()
                print("\n ---- Executando | echo {seu token} > ~/.token_dirlididi.txt")
                if os.system(f"echo {token} > ~/.token_dirlididi.txt") == 0 :
                    os.system("cat ~/.token_dirlididi.txt")
                    escolha = input("É o seu token de acesso é: [s/n]: ")
                    if escolha.lower() == "s" :
                        print("")
                        print("TOKEN de acesso salvo com sucesso")
                        return True
                    else :
                        print("")
                        print("Algo deu errado durante o processo - Salvar Token Part 2")
                        print("Favor reportar ao dono do repositorio")
                        return False
                else :
                    print("")
                    print("Algo deu errado durante o processo - Salvar Token Part 1")
                    print("Favor reportar ao dono do repositorio")
                    return False
            else :
                print("")
                print("Algo deu errado durante o processo - Criar arquivo de Token")
                print("Favor reportar ao dono do repositorio")
                return False
        else :
            print("")
            print("Ok, arquivo de TOKEN não sera criado")
            return True
                    

def check_dirlididi() -> bool:
    existe = file_existe("~/../../bin/dirlididi.py")
    if existe == 0:
        print("")
        print("Dirlididi.py já instalado e na pasta /bin")
        return True
    else :
        print("Dirlididi.py não encontrado na pasta /bin")
        escolha = input("Desejá realizar o download e mover para a pasta /bin? [s/n]")
        if escolha.lower() == "s" :
            print("Baixando Dirlididi.py via wget")
            print(" ---- Executando | wget http://dirlididi.com/tools/dirlididi.py")
            os.system("wget http://dirlididi.com/tools/dirlididi.py")
            if os.path.isfile("./dirlididi.py") :
                print("Dirlididi baixo com sucesso")
                print("Movendo Dirlididi.py para a pasta /bin")
                print (" ---- Executando | sudo mv ./dirlididi.py ~/../../bin")
                os.system("sudo mv ./dirlididi.py ~/../../bin")
                return True
            else :
                print("Erro baixar Dirlididi.py")
                return False
        else :
            return False
            
def main() :
    print("Verificando dirlididi.py: ")
    if check_dirlididi() :
        print("\n ------- \n")

        print("Verificando arquivo de TOKEN de acesso")
        if create_token_file() :
            print("ok")        

main()