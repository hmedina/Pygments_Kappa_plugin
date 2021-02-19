#! /usr/bin/env python3

from setuptools import setup


setup(
    entry_points="""
        [pygments.lexers]
        kappa_lexer = core.KappaLexer:KappaLexer
        [pygments.styles]
        kappa_style_demo = core.KappaStyle:DemoStyle
        kappa_style_browser = core.KappaStyle:KaSimInBrowserStyle
        kappa_style_edit = core.KappaStyle:EditNotationDeltasStyle
        kappa_style_edit_dark = core.KappaStyle:EditNotationDeltasStyleDark
    """
)
