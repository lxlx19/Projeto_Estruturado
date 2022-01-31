import os
import shutil
from pathlib import Path


class ProjExt:
    """
    Gera extrutura de projeto
    """

    def __init__(self, path, projeto):
        self.path = path
        self.projeto = projeto
        self.path_pasta = [
            os.path.join(self.projeto, "src"),
            os.path.join(self.projeto, "tests"),
        ]
        self.path_arquivo = [
            os.path.join(self.projeto, "README.md"),
            os.path.join(self.projeto, "requirements.txt"),
            os.path.join(self.projeto, "LICENSE"),
            os.path.join(self.projeto, ".gitignore"),
            os.path.join(self.projeto, "__init__.py"),
            os.path.join(self.projeto, "main.py"),
            os.path.join(self.projeto, "main_test.py"),
        ]

        self.path_endereco = [
            os.path.join(self.path, self.projeto, "__init__.py"),
            os.path.join(self.path, self.projeto, "main.py"),
            os.path.join(self.path, self.projeto, "main_test.py"),
        ]

        self.path_destino = [
            os.path.join(self.path, self.projeto, "src", "__init__.py"),
            os.path.join(self.path, self.projeto, "src", "main.py"),
            os.path.join(self.path, self.projeto, "tests", "main_test.py"),
        ]

        self.gerador_pastas(self.projeto)
        self.gera_pastas()
        self.gera_arquivos()
        self.gera_conteudos()
        self.move_arquivos()

    def gerador_pastas(self, pasta):
        Path(os.path.join(self.path, pasta)).mkdir(exist_ok=True)

    def gerador_arquivos(self, arquivo):
        Path(os.path.join(self.path, arquivo)).touch(exist_ok=True)

    def gera_arquivos(self):
        for arquivo in self.path_arquivo:
            self.gerador_arquivos(arquivo)

    def gera_pastas(self):
        for pasta in self.path_pasta:
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
            "__init__.py",
            "main.py",
            "main_test.py",
        ]
        for conteudo in lista:
            self.gerador_conteudos(conteudo)

    def move_arquivos(self):
        for path1, path2 in zip(self.path_endereco, self.path_destino):
            shutil.move(path1, path2)
