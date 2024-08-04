#!/usr/bin/env python
# When you activate a virtual environment, the PATH is modified to include the virtual environment's bin directory at the front.
import click
from mlib.mchange import change


@click.command()
@click.option("--amount", prompt="Amount: ", help="Change calculation")
def make_change(amount):
    "Gives change in coins"
    result = change(float(amount))
    message = click.style(f"Change for {amount}: ", fg="red")
    click.echo(message)
    for coin_change in result:
        for num, coin in coin_change.items():
            message = click.style(f"{coin}: {num}", fg="green")
            click.echo(message)


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    make_change()