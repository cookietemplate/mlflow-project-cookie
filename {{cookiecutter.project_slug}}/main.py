import typer

app = typer.Typer()


@app.command(
    help="Say hello to NAME from the command line.",
    short_help="Say hello to NAME.",
    no_args_is_help=True,
)
def main(name: str = "fish"):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()
