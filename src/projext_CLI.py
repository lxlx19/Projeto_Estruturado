import click

from projext import ProjExt


@click.command()
@click.argument(
    "name",
    metavar="NOME_DO_PROJETO",
)
@click.option("--path", default="./", help="Path para o Projeto")
def cria_projeto(path, name):
    ProjExt(path, name)


if __name__ == "__main__":
    cria_projeto()
