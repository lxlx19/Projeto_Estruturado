import os
from pathlib import Path


class ProjetoExtruturado:
    """
    Gera extrutura de projeto
    """

    def __init__(self, path, projeto):
        self.path = path
        self.projeto = projeto

        self.gerador_pastas(self.projeto)
        self.gera_pastas()
        self.gera_arquivos()
        self.gera_conteudos()

    def gerador_pastas(self, pasta):
        Path(os.path.join(self.path, pasta)).mkdir(exist_ok=True)

    def gerador_arquivos(self, arquivo):
        Path(os.path.join(self.path, arquivo)).touch(exist_ok=True)

    def gera_arquivos(self):
        lista = [
            os.path.join(self.projeto, "README.md"),
            os.path.join(self.projeto, "requirements.txt"),
            os.path.join(self.projeto, "LICENSE"),
            os.path.join(self.projeto, ".gitignore"),
            os.path.join(self.projeto, "project", "__init__.py"),
            os.path.join(self.projeto, "project", "main.py"),
            os.path.join(self.projeto, "tests", "main_tests.py"),
        ]
        for arquivo in lista:
            self.gerador_arquivos(arquivo)

    def gera_pastas(self):
        lista = [
            os.path.join(self.projeto, "project"),
            os.path.join(self.projeto, "tests"),
        ]
        for pasta in lista:
            self.gerador_pastas(pasta)

    def gerador_conteudos(self, arquivo):

        with open(os.path.join("templates", arquivo), "r") as template, open(
            os.path.join(self.path, self.projeto, arquivo), "w"
        ) as escrever:
            for linha in template.readlines():
                escrever.write(linha)

    def gera_conteudos(self):
        lista = [
            "README.md",
            "requirements.txt",
            "LICENSE",
            ".gitignore",
        ]
        for conteudo in lista:
            self.gerador_conteudos(conteudo)


if __name__ == "__main__":
    main()
