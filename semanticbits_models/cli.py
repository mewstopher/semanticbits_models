# _*_ coding: utf-8 _*_

"""Console script for semanticbits_models."""
import sys
import click
from semanticbits_models.semanticbits_models import func1


@click.command()
def main(args=None):
    """console script for semanticbits_models."""
    click.echo("Hello, what would you like to search for?")
    return 0


if __name__ == "__main__":
    sys.exit(main()) # pragma: no cover
