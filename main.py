from pathlib import Path 
import os

def existe_dirlididi() -> int :
    return os.system("cat ~/../../bin/dirlididi.py > /dev/null")

def check_dirlididi() -> bool:
    existe = existe_dirlididi()
    os.system("clear")
    if existe == 0:
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
    print(check_dirlididi())
        

main()