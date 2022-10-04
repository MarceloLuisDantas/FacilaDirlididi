import os

def file_existe(path: str) :
    comando = "cat {} > /dev/null".format(path)
    return os.system(comando)

def facila_prenchido() -> bool:
    facila = open(os.path.expanduser("~/.facila.txt"), "r")
    linhas = facila.readlines()
    facila.close()
    return len(linhas) == 3

def get_token() -> str :
    while True :
        print(" ")
        token = input("    Digite o seu TOKEN de acesso: ")
        suporte = input("    Digite novamente: ")
        if token != suporte :
            print(" ")
            print("     Os TOKENS não são iguais")
            print("     Favor, tentar novamente")
        else :
            return token

def get_nome() -> str :
    while True :
        print(" ")
        nome = input("    Qual nome colocar nos cabeçalhos: ")
        escolha = get_escolha(f"    Confirmar nome como: {nome}? [s/n]: ")
        if escolha :
            return nome

def get_matricula() -> str :
    while True :
        print(" ")
        matricula = input("    Qual sua matricula: ")
        escolha = get_escolha(f"    Confirmar matricual como: {matricula}? [s/n] ")
        if escolha :
            return matricula

def get_escolha(label: str) -> bool :
    ESCOLHAS = ['s', 'sim', 'n', 'não', 'nao']
    NEG = ['n', 'não', 'nao']
    POS = ['s', 'sim']
    while True :
        escolha = input(label)
        if escolha.lower() in ESCOLHAS :
            return escolha.lower() in POS
        else :
            print(f"    '{escolha}' não é uma opção valida")
            print(" ")

def preenche_facila() -> bool :
    token = get_token()
    nome = get_nome()
    matricula = get_matricula()
    print("")
    print(" -- Executando | echo {seu token} >> ~/.facila.txt ")
    print(" -- Executando | echo {seu nome} >> ~/.facila.txt ")
    print(" -- Executando | echo {sua matricula} >> ~/.facila.txt ")
    print("")
    sv_token = os.system(f"echo {token} >> ~/.facila.txt")
    sv_nome = os.system(f"echo {nome} >> ~/.facila.txt")
    sv_matricula = os.system(f"echo {matricula} >> ~/.facila.txt")
    if [sv_token, sv_nome, sv_matricula] == [0, 0, 0] :
        facila = open(os.path.expanduser("~/.facila.txt"), "r")
        print(f"Token: {facila[0]}")
        print(f"Nome: {facila[1]}")
        print(f"Matricula: {facila[2]}")
        escolha = get_escolha("    Os valores estão corretos? [s/n]: ")
        facila.close()
        if escolha :
            return True
        else :
            print(" ")
            print(" Algo deu errado durante o processo - ")
            print("     - Salvar informações 2 ")
            print(" Favor reportar ao dono do repositorio")
            return False
    else :
        print(" ")
        print(" Algo deu errado durante o processo - ")
        print("     - Salvar informações 1")
        print(" Favor reportar ao dono do repositorio")
        return False

def create_facil_file() -> bool :
    print(" ")
    print("  ---- Configurando arquivo .facila ----")
    print("  ---- Neste arquivo sera guardado o seu token de acesso ao Dirlididi")
    print("       e o seu nome e matricula para criação dos cabeçalhos")
    print(" ")
    existe = file_existe("~/.facila.txt")
    if existe == 0 :
        print(" Arquivo ~/.facila.txt já existente")
        if facila_prenchido() :
            return True
        else :
            print("")
            print(" Arquivo .facila mal preenchido")
            escolha = get_escolha(" deseja reescrevelo? [s/n]: ")
            if escolha :
                os.system("rm -rf ~/.facila.txt")
                os.system("touch ~/.facila.txt")
                preenche_facila()
            return True
    else :
        print(" ")
        print(" Arquivo .facila não encontrado")
        print(" ")
        print(" Executando | touch ~/.facila.txt")
        if os.system("touch ~/.facila.txt") == 0 :
            print(" Arquivo .facila criado com sucesso ")
            preenche_facila()
            
        else :
            print(" ")
            print(" Algo deu errado durante o processo - ")
            print("     - Criar arquivo de .facila" )
            print(" Favor reportar ao dono do repositorio")
            return False
                    
def check_dirlididi() -> bool :
    print("  ---- Configurando dirlididi.py na pasta /bin ----")
    existe = file_existe("~/../../bin/dirlididi.py")
    print(" ")
    if existe == 0:
        print(" ")
        print(" Dirlididi.py já instalado e na pasta /bin")
        return True
    else :
        print(" Dirlididi.py não encontrado na pasta /bin")
        print(" ")
        print(" Baixando Dirlididi.py via wget")
        print(" Executando | wget http://dirlididi.com/tools/dirlididi.py")
        os.system("wget http://dirlididi.com/tools/dirlididi.py")
        if os.path.isfile("./dirlididi.py") :
            print(" ")
            print(" Dirlididi baixo com sucesso")
            print(" Movendo Dirlididi.py para a pasta /bin")
            print(" ")
            print (" Executando | sudo mv ./dirlididi.py ~/../../bin")
            os.system("sudo mv ./dirlididi.py ~/../../bin")
            return True
        else :
            print(" Erro ao baixar Dirlididi.py")
            return False

def get_terminal() -> str :
    os.system("touch suporte.txt")
    os.system("echo $SHELL > suporte.txt")
    f = open("./suporte.txt")
    shell = f.readline().split("/")[-1][0:-1]
    f.close()
    return shell
    
def instala_facila() -> bool :
    print(" Instalando facila.py em /bin")
    terminal = get_terminal()
    if terminal == "zsh" :
        if file_existe("~/../../bin/facila.py") == 0 :
            print(" ")
            print(" facila.py já instalado em /bin")
            print(" ")
            return True
        else :
            os.system("sudo cp ./facila.py ~/../../bin")
            os.system('echo "alias facila=\'python3  ~/../../bin/facila.py\'" >> ~/.zshrc')
            return True
    return False

def main() :
    os.system("clear")
    if check_dirlididi() :
        print(" Dirlididi configurado com sucesso")
        print(" ")
        if create_facil_file() :
            print(" Arquivo de .facila configurado com sucesso")
            print(" ")
            if instala_facila() :
                print(" Facila instalado com sucesso ")
                print(" Digite 'facila help' para mais informações")
            else :
                print(" Erro ao instalar facila em /bin")
        else :
            print(" Erro ao verificar .facila.txt")
    else :
        print(" Erro a overifica Dirlididi.py")
main()