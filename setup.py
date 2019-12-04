#! /usr/bin/env python3

from setuptools import setup


setup(
    name='Pygments_Kappa_plugin',
    version='0.1',
    packages=['Pygments_Kappa_plugin'],
    package_dir={'': '.'},
    url='https://github.com/hmedina/Pygments_Kappa_plugin',
    author='Hector Medina',
    author_email='hector.f.medina.a@gmail.com',
    entry_points="""
        [pygments.lexers]
        kappa_lexer = KappaLexer:KappaLexer
        [pygments.styles]
        kappa_style_demo = KappaStyle:DemoStyle
        kappa_style_browser = KappaStyle:KaSimInBrowserStyle
        kappa_style_edit = KappaStyle:EditNotationDeltasStyle
    """
)