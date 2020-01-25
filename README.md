# Pygments Kappa plugin

## About
A plugin for the [Pygments package](https://pygments.org/) adding lexing and styling support for the [Kappa language](https://kappalanguage.org/).


### Installation
The plugin uses `setuptools` "entry points" to extend the lexers and styles known to Pygments. It thus works on a stock Pygments installation. To install, optionally to the `user` directory:

`./setup.py install [--user]`


### Uninstallation
Recent versions of the Python package manager are able to find and remove a package installed locally. Use `pip freeze` to display the list of packages pip is aware of. Then:

`pip uninstall Pygments-Kappa-plugin`


### Usage
Once installed, the entire Pygments stack will be aware of the new lexer and styles. This includes the [command-line script](https://pygments.org/docs/cmdline/) `pygmentize`. For example, to highlight a file called `foo.ka` using the style `kappa_style_edit`, formatting into an HTML file that contains the CSS style-sheet (i.e. a "full" file) called `foo.html`: 

``pygmentize -f html -O style=kappa_style_edit,full -o foo.html foo.ka``

As the lexer declares `.ka` as the extension for kappa files, it doesn't have to be specified so long as the input file has that extension. The Pygments-provided formatters to `LaTeX` and various image formats are supported.


## Contents
Pygments works by having a lexer issue a token for every component it finds. Those tokens are then styled by a user-given style-sheet. Thus the plugin consists of a module `core` containing three files, `KappaLexer`, `KappaStyle`, and `KappaToken`, each for a class type.

### KappaLexer
`KappaLexer` contains the lexer, a multi-state parser based on regular expressions. As of this writing, it lexes the entire KaSim4 test suite successfully (the files that pass the test suite anyhow...).

### KappaToken
Given the hierarchy of Kappa expressions, I designed the token structure to take advantage of inheritance to form a tree. `KappaToken` declares this tree, and is meant to be modular.

For example, a style that applies to `Token.Kappa.Rule.Agent` will be inherited to all its children, including:
 ```
 Token.Kappa.Rule.Agent.Name
 Token.Kappa.Rule.Agent.Signature.Site
 Token.Kappa.Rule.Agent.Signature.Site.Internal.State
 ```
By the same logic, a style that applies to `Token.Kappa.Rule.Agent.Name` will not apply to `Token.Kappa.Rule.Agent.Signature`.

### KappaStyle
The token inheritance behavior allows one to define a style for the various components of a kappa file. These are defined in the `KappaStyle` file. Three are provided:
* `kappa_style_demo`
  * Showcases some nuances the lexer is capable of.
* `kappa_style_browser`
  * Mimics the style used in the [GUI](https://tools.kappalanguage.org/try/?model=https%3A//raw.githubusercontent.com/Kappa-Dev/KaSim/master/models/abc-pert.ka), with proper handling of counter syntax in agent declarations.
* `kappa_style_edit`
  * Agent names will be bolded, edit operations will have a colored background according to their type.