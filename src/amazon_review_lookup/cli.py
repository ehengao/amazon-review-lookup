# -*- coding: utf-8 -*-

"""
    amazon-review-lookup.cli
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A command line application to run amazon-review-lookup app

    :copyright: NIA, Ericsson

"""
import sys
import click


@click.command()
def main(args=None):
    """Console script for amazon_review_lookup."""
    click.echo(
        "Replace this message by putting your code into "
        "amazon_review_lookup.cli.main"
    )
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
