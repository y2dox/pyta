import typer

app = typer.Typer(help="Pyta bypu")

@app.command()
def info(hint: str = ""):
    if not hint:
        typer.echo('try --hint =hint=')
    elif hint == '=hint=':
        typer.echo('Bingo')
    else:
        typer.echo(f"Nice {hint}")

def main():
    app()
    
if __name__ == '__main__':
    main()