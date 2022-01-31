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
            os.path.join(self.projeto),
            os.path.join(self.projeto, "src"),
            os.path.join(self.projeto, "tests"),
        ]
        self.lista_conteudos = [
            "README.md",
            "requirements.txt",
            "LICENSE",
            ".gitignore",
            "__init__.py",
            "main.py",
            "main_test.py",
        ]
        self.path_arquivo = []
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

        self.gera_path_arquivos()
        self.gera_pastas()
        self.gera_arquivos()
        self.gera_conteudos()
        self.move_arquivos()

    def gera_path_arquivos(self):
        for arquivo in self.path_arquivo:
            path_novo = os.path.join(self.projeto, arquivo)
            self.path_arquivo.append(path_novo)

    def gera_arquivos(self):
        for arquivo in self.path_arquivo:
            Path(os.path.join(self.path, arquivo)).touch(exist_ok=True)

    def gera_pastas(self):
        for pasta in self.path_pasta:
            Path(os.path.join(self.path, pasta)).mkdir(exist_ok=True)

    def gera_conteudos(self):
        for conteudo in self.lista_conteudos:
            with open(os.path.join("templates", conteudo), "r") as template, open(
                os.path.join(self.path, self.projeto, conteudo), "w"
            ) as escrever:
                for linha in template.readlines():
                    escrever.write(linha)

    def move_arquivos(self):
        for path1, path2 in zip(self.path_endereco, self.path_destino):
            shutil.move(path1, path2)
