import os

def file_existe(path: str) -> bool :
    try:
        _ = open(os.path.expanduser(path))
        return True
    except :
        return False

def facila_prenchido() -> bool:
    facila = open(os.path.expanduser("~/.facila.txt"), "r")
    linhas = facila.readlines()
    facila.close()
    return len(linhas) == 3

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

def salva_info(info: str, path: str, erro: str) -> bool :
    result = os.system(f"echo {info} >> {path}") 
    if result != 0 :
        msg_erro(erro)
        return False
    return True

def preenche_facila() -> bool :
    token     = get_info("Qual o seu TOKEN de acesso ao Dirlididi: ")
    nome      = get_info("Qual nome colocar nos cabeçalhos: ")
    matricula = get_info("Qual matricula colocar nos cabeçalhos: ")

    print(" ")
    print(" -- Executando | echo {seu token}     >> ~/.facila.txt ")
    print(" -- Executando | echo {seu nome}      >> ~/.facila.txt ")
    print(" -- Executando | echo {sua matricula} >> ~/.facila.txt ")
    print(" ")
    
    sv_token     = salva_info(token,     "~/.facila.txt", "Salvar Token")    
    sv_nome      = salva_info(nome,      "~/.facila.txt", "Salvar Nome")    
    sv_matricula = salva_info(matricula, "~/.facila.txt", "Salvar Matricula")

    if sv_token and sv_nome and sv_matricula :
        facila = open(os.path.expanduser("~/.facila.txt"), "r").readlines()

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

def create_facil_file() -> bool :
    print(" ----- Configurando arquivo .facila ----- ")
    print(" ----- Neste arquivo sera guardado o seu token de acesso ao Dirlididi")
    print("       e o seu nome e matricula para criação dos cabeçalhos")
    print(" ")

    if file_existe("~/.facila.txt") :
        print(" -- Arquivo ~/.facila.txt já existente")
        if facila_prenchido() :
            return True
        else :
            print(" -- Arquivo .facila mal preenchido")
            escolha = get_escolha("    deseja reescrevelo? [s/n]: ")
            if escolha :
                os.system("rm -rf ~/.facila.txt")
                os.system("touch ~/.facila.txt")
                preenche_facila()
            return True
    else :
        print(" -- Arquivo .facila não encontrado")
        print(" -- Executando | touch ~/.facila.txt")
        print(" ")
        if os.system("touch ~/.facila.txt") == 0 :
            print(" -- Arquivo .facila criado com sucesso ")
            print(" ")
            preenche_facila()
            return True
        else :
            msg_erro("Criar arquivo de .facila")
            return False
                    
def check_dirlididi() -> bool :
    print(" ")
    print(" ----- Configurando dirlididi.py na pasta /bin -----")
    print(" ")
    if file_existe("~/../../bin/dirlididi.py") :
        print(" -- Dirlididi.py já instalado e na pasta /bin")
        print(" ")
        return True
    else :
        print(" -- Dirlididi.py não encontrado na pasta /bin")
        print(" -- Baixando Dirlididi.py via wget")
        print(" -- Executando | wget http://dirlididi.com/tools/dirlididi.py")
        print(" ")
        os.system("wget http://dirlididi.com/tools/dirlididi.py")
        if os.path.isfile("./dirlididi.py") :
            print(" -- Dirlididi baixo com sucesso")
            print(" -- Movendo Dirlididi.py para a pasta /bin")
            print(" -- Executando | sudo mv ./dirlididi.py ~/../../bin")
            print(" ")
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
    os.system("rm -rf suporte.txt")
    return shell
    
def instala_facila() -> bool :
    print(" Instalando facila.py em /bin")
    print(" ")
    terminal = get_terminal()

    if file_existe("~/../../bin/facila.py") :
        print(" facila.py já instalado em /bin")
    else :
        if os.system("sudo cp ./facila.py ~/../../bin") != 0 :
            msg_erro("Instalando facila.py em /bin")
            return False

    if terminal == "zsh" :
        os.system('echo "alias facila=\'python3  ~/../../bin/facila.py\'" >> ~/.zshrc')
        return True
    elif terminal == "bash" :
        os.system('echo "alias facila=\'python3  ~/../../bin/facila.py\'" >> ~/.bashrc')
        return True

    else :
        print(" ")
        print(f" O seu terminal é - {terminal}")
        print(" O qual esta fora do escopo de compatibilidade")
        print(" Favor, notifique ao dono do repositorio sobre")
        print(" ")

    return False

def main() :
    os.system("clear")
    if check_dirlididi() :
        print(" Dirlididi configurado com sucesso")
        print(" ")
        if create_facil_file() :
            print(" .facila configurado com sucesso")
            print(" ")
            if instala_facila() :
                print(" Facila instalado com sucesso ")
                print(" ")
                print(" Digite 'facila help' para mais informações")
                print(" ")
            else :
                msg_erro("Erro ao instalar facila em /bin")
        else :
            msg_erro("Erro ao verificar .facila.txt")
    else :
        msg_erro("Erro a overifica Dirlididi.py")

main()