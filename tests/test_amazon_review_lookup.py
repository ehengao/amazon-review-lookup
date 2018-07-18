#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `amazon-review-lookup` package."""
from click.testing import CliRunner

import amazon_review_lookup
from amazon_review_lookup import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'amazon_review_lookup.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_version():
    assert len(amazon_review_lookup.__version__.split('.')) == 3
