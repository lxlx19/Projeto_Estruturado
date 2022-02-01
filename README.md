# Projext - Projeto Extruturado

Esse Script cria todas estrutura de projeto necessário para um projeto simples
em Python.

## Árvore de projeto

A seguinte arvore de projeto é criada ao executar o script:

```
Nome_Projeto
├── src
│   ├── main.py
│   ├── __init__.py
│   └── tests
│       └── tests_main.py
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

### Instruções

Ao executar o script, você precisa informar apenas o caminho do projeto e o nome do arquivo.

```
> python3 projext_CLI.py --option="./Diretório" NOME_DO_PROJETO
```

Caso não sej informado a opção diretório, ele vai criar na própria pasta de execução.

Para obter ajuda, pode utilizar:

```
> python3 projext_CLI.py --help
```

Para instalar as dependência necessárias para rodas o scrip, use o arquivo requirements.txt

```
> pip install -r requirements.txt
```
