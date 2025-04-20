import typer

app = typer.Typer()

@app.command("greet")
def greet(
    name: str = typer.Option(..., "--name", "-n", help="Tên của bạn")
):
    print(f"👋 Hello, {name}!", flush=True)

@app.command("bye")  # 👈 PHẢI có dòng này để Typer nhận biết đây là command
def bye(
    name: str = typer.Option(..., "--name", "-n", help="Tên của bạn")
):
    print(f"👋 Bye, {name}!", flush=True)
