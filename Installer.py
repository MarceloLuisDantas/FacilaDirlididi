from pathlib import Path
import os

def file_existe(path: str) -> bool :
    try:
        _ = open(os.path.expanduser(path))
        return True
    except :
        return False

def facila_prenchido() -> bool:
    facila = open(os.path.expanduser("~/Facila/facila.txt"), "r")
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
    os.close()

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
    print(" -- Executando | echo {seu token}     >> ~/Facila/facila.txt ")
    print(" -- Executando | echo {seu nome}      >> ~/Facila/facila.txt ")
    print(" -- Executando | echo {sua matricula} >> ~/Facila/facila.txt ")
    print(" ")
    
    sv_token     = salva_info(token,     "~/Facila/facila.txt", "Salvar Token")    
    sv_nome      = salva_info(nome,      "~/Facila/facila.txt", "Salvar Nome")    
    sv_matricula = salva_info(matricula, "~/Facila/facila.txt", "Salvar Matricula")

    if sv_token and sv_nome and sv_matricula :
        facila = open(os.path.expanduser("~/Facila/facila.txt"), "r").readlines()

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

def create_facila_file() -> bool :
    print(" ----- Configurando arquivo .facila ----- ")
    print(" ----- Neste arquivo sera guardado o seu token de acesso ao Dirlididi")
    print("       e o seu nome e matricula para criação dos cabeçalhos")
    print(" ")

    if file_existe("~/Facila/facila.txt") :
        print(" -- Arquivo ~/Facila/facila.txt já existente")
        if facila_prenchido() :
            return True
        else :
            print(" -- Arquivo .facila mal preenchido")
            escolha = get_escolha("    deseja reescrevelo? [s/n]: ")
            if escolha :
                os.system("rm -rf ~/Facila/facila.txt")
                os.system("touch ~/Facila/facila.txt")
                preenche_facila()
            return True
    else :
        print(" -- Arquivo .facila não encontrado")
        print(" -- Executando | touch ~/Facila/facila.txt")
        print(" ")
        if os.system("touch ~/Facila/facila.txt") == 0 :
            print(" -- Arquivo .facila criado com sucesso ")
            print(" ")
            preenche_facila()
            return True
        else :
            msg_erro("Criar arquivo de .facila")
            return False
                    
def check_dirlididi() -> bool :
    print(" ")
    print(" ----- Configurando dirlididi.py na pasta ~/Facila -----")
    print(" ")
    if file_existe("~/Facila") :
        print(" -- Dirlididi.py já instalado e na pasta ~/Facila")
        print(" ")
        return True
    else :
        print(" -- Dirlididi.py não encontrado na pasta ~/Facila")
        print(" -- Baixando Dirlididi.py via wget")
        print(" -- Executando | wget http://dirlididi.com/tools/dirlididi.py")
        print(" ")
        os.system("wget http://dirlididi.com/tools/dirlididi.py")
        if os.path.isfile("./dirlididi.py") :
            print(" -- Dirlididi baixo com sucesso")
            print(" -- Movendo Dirlididi.py para a pasta ~/Facila")
            print(" -- Executando | mv ./dirlididi.py ~/Facila")
            print(" ")
            os.system("mv ./dirlididi.py ~/Facila")
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
    print(" Instalando facila.py em ~/Facila")
    print(" ")
    terminal = get_terminal()

    if file_existe("~/Facila/facila.py") :
        print(" facila.py já instalado em ~/Facila")
        print(" A versão antiga sera apagada e a nova versão sera instalada")
        print(" ")
        os.system("rm ~/Facila/facila.py")

    if os.system("cp ./facila.py ~/Facila") != 0 :
        msg_erro("Instalando facila.py em ~/Facila")
        return False

    if file_existe("~/Facila/templates.py") :
        print(" templates.py já instalado em ~/Facila")
        print(" A versão antiga sera apagada e a nova versão sera instalada")
        print(" ")
        os.system("rm ~/Facila/templates.py")

    if os.system("cp ./templates.py ~/Facila") != 0 :
        msg_erro("Instalando templates.py em ~/Facila")
        return False

    if terminal == "zsh" :
        os.system('echo "alias facila=\'python3 ~/Facila/facila.py\'" >> ~/.zshrc')
        return True
    elif terminal == "bash" :
        os.system('echo "alias facila=\'python3 ~/Facila/facila.py\'" >> ~/.bashrc')
        return True

    else :
        print(" ")
        print(f" O seu terminal é - {terminal}")
        print(" O qual esta fora do escopo de compatibilidade")
        print(" Favor, notifique ao dono do repositorio sobre")
        print(" ")

    return False

def create_facila_folder() :
    if not Path.exists(Path(os.path.expanduser("~/Facila"))) :
        os.system("mkdir ~/Facila")

def main() :
    os.system("clear")

    create_facila_folder()

    if check_dirlididi() :
        print(" Dirlididi configurado com sucesso")
        print(" ")
        if create_facila_file() :
            print(" Facila configurado com sucesso")
            print(" ")
            if instala_facila() :
                print(" Facila instalado com sucesso ")
                print(" ")
                print(" Digite 'facila help' para mais informações")
                print(" ")
            else :
                msg_erro("Erro ao instalar facila em ~/Facila")
        else :
            msg_erro("Erro ao verificar facila.txt")
    else :
        msg_erro("Erro a overifica Dirlididi.py")

main()