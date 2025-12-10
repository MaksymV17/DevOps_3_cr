import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', help='Введіть ім\'я')
def say(name):
    # Перевірка: якщо ім'я починається на 'p' або 'P'
    if name and name.lower().startswith('p'):
        print("Ім’я не підходить")
    else:
        print(name)

cli.add_command(say)

if __name__ == '__main__':
    cli()