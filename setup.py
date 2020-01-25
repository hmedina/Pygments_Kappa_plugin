#! /usr/bin/env python3

from setuptools import setup


setup(
    name='Pygments_Kappa_plugin',
    version='0.1',
    packages=['core'],
    package_dir={'': '.'},
    url='https://github.com/hmedina/Pygments_Kappa_plugin',
    author='Hector Medina',
    author_email='hector.f.medina.a@gmail.com',
    install_requires=['Pygments>=2.5.2'],
    entry_points="""
        [pygments.lexers]
        kappa_lexer = core.KappaLexer:KappaLexer
        [pygments.styles]
        kappa_style_demo = core.KappaStyle:DemoStyle
        kappa_style_browser = core.KappaStyle:KaSimInBrowserStyle
        kappa_style_edit = core.KappaStyle:EditNotationDeltasStyle
    """
)