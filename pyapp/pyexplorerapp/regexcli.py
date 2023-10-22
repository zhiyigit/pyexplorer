import typer

from pyshared.regexutils.regexutilities import is_alpha_or_numberic

tapp = typer.Typer()


@tapp.command()
def check_alpha_numeric(expression: str):
    print(expression + " is " + str(is_alpha_or_numberic(expression)))



@tapp.command()
def hello(name: str):
    print("Greetings: " + name)

if __name__ == "__main__":
    tapp()
