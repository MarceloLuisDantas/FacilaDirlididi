# Facila
Ferramenta criada para auxiliar no uso do Dirlididi.

## Instalação

Para instalar basta clonar o Rep e executar o Installer.py. Ele ira baixar o arquivo do Dirlididi do site [oficial](http://dirlididi.com/tools/dirlididi.py) e instalar na pasta /bin do seu usuario e instalar na pasta /bin do seu usuario. Apos a instalação sera pedido o seu **Token de Acesso ao Dirlididi**, o seu **nome** e a sua **matrícula** da UFCG. O Token é obviamente para submeter as questões, o nome e matrícula são para a criação dos cabeçalhos nos programas. Todas essas informações serão salvas em **~/.facila.txt** e podem ser alteradas a qualquer momento tanto manualmente quanto por meio do próprio Facila

**PS**: Caso você altere o facila.py e queira instalar a nova versão, basta rodar o instalador de novo que ele ira apagar a versão antiga e instalar a nova.

## Uso
Como o proprio objetivo é facilitar o uso do Dirlididi, o Facila possui um uso simples. Existem 2 principais utilidades, criar  projetos e submeter projetos. 

### Facila new
```
facila new [token da questão] "[nome da questão]" [linguagem]
 ou
facila new [token da questão] "[nome da questão]" 
 ou
facila new [token da questão]
```
Dos 3 valores o único obrigatório é o token da questão, caso a linguagem não seja especificada, sera criado um arquivo Java, e caso o nome não seja especificado, o arquivo criado tera Programa como nome, e a pasta da atividade sera o token da questão.

```
User $> facila new KaD02IAad "Cotacao do Dolar" python
Criando projeto Dirlididi

User $> tree -a
└── CotacaoDoDolar
    ├── .info.txt
    └── CotacaoDoDolar.py

User $> facila new OAaPsZoiS
Criando projeto Dirlididi

User $> tree -a
├── CotacaoDoDolar
│   ├── .info.txt
│   └── CotacaoDoDolar.py
└── OAaPsZoiS
    ├── .info.txt
    └── Programa.java
```

**AVISO**: As linguagens compativeis são Java, Python, C, C++, Haskell e Prolog. Caso queira que alguma outra linguagem seja adicionada faça um pull request com suas mudanças ou abra uma nova issue. Os compiladores de C e C++ são o GCC e G++, caso queira mudar para CLang basta alterar no código fonte do facila.py

### Facila submit

```
facila submit
```

Ira submeter a questão da pasta atual. 

```
User $> facila submit
Submetendo projeto KaD02IAad - CotacaoDoDolar.java
Results: .....
```

### Facila config

```
facila config
```

Além de criar atividades e submeter atividades, é possível configurar o arquivo **.facila** a partir do próprio Facila. Sera pedido as suas informações de Token, Nome e Matrícula novamente e as alterações serão salvas. 

### Facila run

```
facila config [parametros]
```

Ao rodar **facila run** o seu programa sera compilado caso for preciso, e ira ser executado em seguida. Caso algum parametro sejá indicado ele ira ser passado ao programa

```
User $> facila run dromedario
Facila - Compilando: Hello.java
Facila - OK
Facila - Rodando: Hello.java

Hello Dromedario
```

