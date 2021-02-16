#! /usr/bin/env python3

from setuptools import setup
"""
    Plugin for Pygments providing a lexer and various stylers for pretty printing code written in the Kappa agent- and rule-based modeling language.
"""


setup(
    name='Pygments_Kappa_plugin',
    version='0.1',
    packages=['core'],
    package_dir={'': '.'},
    url='https://github.com/hmedina/Pygments_Kappa_plugin',
    license='MIT',
    author='Hector Medina',
    author_email='hector.f.medina.a@gmail.com',
    description='Plugin for Pygments to highlight Kappa.',
    long_description=__doc__,
    python_requires='>=3.6'
    install_requires=['Pygments>=2.5.1'],
    entry_points="""
        [pygments.lexers]
        kappa_lexer = core.KappaLexer:KappaLexer
        [pygments.styles]
        kappa_style_demo = core.KappaStyle:DemoStyle
        kappa_style_browser = core.KappaStyle:KaSimInBrowserStyle
        kappa_style_edit = core.KappaStyle:EditNotationDeltasStyle
    """
)
