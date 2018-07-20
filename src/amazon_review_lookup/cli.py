#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    amazon-review-lookup.cli
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A command line application to run amazon-review-lookup app

"""
import csv
import sys

import click

from amazon_review_lookup.parser import AMAZON_URL_ROOT, review_parser


@click.command()
@click.option('--asin', default='asins.txt', help='asin file location')
@click.option(
    '--output', default='reviews.csv', help='output csv file location'
)
def main(asin, output):
    """Console script for amazon_review_lookup."""
    asins = []
    with open(asin, 'r') as asin_fw:
        asins = [line.strip() for line in asin_fw]
    assert len(asins) > 0, 'no asins content found'
    fieldnames = [
        'name',
        'asin_id',
        'url',
        'review_header',
        'review_rating',
        'review_author',
        'review_text',
        'review_posted_date',
        'review_comment_count',
    ]
    with open(output, 'w') as csvfile:
        csvwriter = csv.DictWriter(
            csvfile, delimiter='|', fieldnames=fieldnames, dialect=csv.excel
        )
        csvwriter.writeheader()
        for asin_id in asins:
            print(f'Processing page {AMAZON_URL_ROOT}{asin_id}/')
            review_data = review_parser(asin_id)
            reviews = review_data['reviews']
            for review in reviews:
                review['name'] = review_data['name']
                review['url'] = review_data['url']
                review['asin_id'] = asin_id
                print(review)
                csvwriter.writerow(review)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
