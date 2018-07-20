#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    tests.review_parser
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for data parsing out of review pages.

"""
from amazon_review_lookup.parser import review_parser


def test_review_parser():
    asin = 'B000VK5UO0'
    data = review_parser(asin)
    print(data)
