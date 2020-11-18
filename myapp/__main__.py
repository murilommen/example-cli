import sys
import click

from myapp.example import sum as sm

@click.group()
@click.version_option("1.0.0")
# @click.option("--x", default=1, help='Number X to sum')
# @click.option("--y", default=2, help='Number Y to sum')


def main():
    """A mockup CLI app example"""
    print("Hye")
    pass

@main.command()
@click.argument("x", required=True)
def sum(**kwargs):
    """Sum two values"""

    # x = click.echo(kwargs)['x']
    x = int(kwargs.get("x"))
    y = x + 2

    print(sm(x,y))
    
    pass


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("IRIS CLI Example")
    main()