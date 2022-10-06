# Facila
Ferramenta criada para auxiliar no uso do Dirlididi.

## Instalação

Para instalar basta clonar o Rep e executar o Installer.py. 
Ele ira baixar o arquivo do Dirlididi do site [oficial](http://dirlididi.com/tools/dirlididi.py) e instalar na pasta /bin do seu usuario.
Apos a instalação sera pedido o seu *Token de Acesso* ao Dirlididi, o seu nome e a sua Matricula da UFCG. O Token é abviamente para submeter as questões, o nome e matricula são para a criação dos cabeçalhos nos programas. Todas essas informações seram salvas em **~/.facila.txt** e podem ser alteradas a qualquer momento tanto manualmente quanto por meio do porprio Facila

## Uso
Como o propio objetivo é facilitar o uso do Dirlididi, o Facila possui um uso simples. Existem 2 principais utilidades, criar novos projetos e submeter projetos. 

### Facila new
```
facila new [token da questão] "[nome da questão]"
 ou
facila new [token da questão]
```

Pela primeira opção, sera criada uma pasta com nome da questão em CamelCase e um arquivo .java com mesmo nome. Já pelo segundo, a pasta tera o token da questão como nome e o .java sera chamado de Programa. Ambos iram criar um arquivo .info com as informações da questão precissas para submeter. 

```
User $> facila new KaD02IAad "Cotacao do Dolar"
Criando projeto Dirlididi

User $> tree -a
└── TesteTeste
    ├── .info.txt
    └── CotacaoDoDolar.java
```

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

Alem de criar novos atividades e submeter atividades, é possivel configurar o arquivo **.facila** a partir do propio Facila. Sera pedido as suas informações de Token, Nome e Matricula novamente e as alterações seram salvas. 