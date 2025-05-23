#! /usr/bin/env python3

from pygments.lexer import RegexLexer, bygroups, words
from core.KappaToken import *


ka_integer = r'[0-9]+'
ka_real = r'([0-9]+[eE][+-]?[0-9+])|((([0-9]+\.[0-9]*)|(\.[0-9]+))([eE][+-]?[0-9]+)?)'
ka_identifier = r'[_~][a-zA-Z0-9~+_]+|[a-zA-Z][a-zA-Z0-9_~+-]*'

# the declaration pods exists because counter syntax is identical for edit notation 
# in rules and for declaration statements in %agent:
# With this, I avoid issuing the wrong tokens (e.g. highlighting as edit operation 
# statements in agent declaration statement), at the expense of more token types.
agent_rule_components = [
    # comments
    (r'//.*?$', Comment.Singleline),
    (r'/\*', Comment.Multiline, 'comment'),
    # end of expression, agent edit operation
    (r'(\))([+-]?)', bygroups(Agent_Decor, Agent_Oper), '#pop'),
    # bond states
    (r'(\[\s*)(\d+|_|#|\.)(\s*\])',                                                             # [99]
        bygroups(Site_Bond_Decor, Site_Bond_State, Site_Bond_Decor)),
    (r'(\[\s*)(' + ka_identifier + r')(.)(' + ka_identifier + r')(\s*\])',                      # [site.Agent]
        bygroups(Site_Bond_Decor, Site_Bond_State_Site, Site_Bond_Decor, Site_Bond_State_Agent, Site_Bond_Decor)),
    (r'(\[\s*)(\d+|_|#|\.)(\s*/\s*)(\d+|\.)(\s*\])',                                            # [99/56]
        bygroups(Site_Bond_Oper_Decor, Site_Bond_Oper_State, Site_Bond_Oper_Decor, Site_Bond_Oper_State, Site_Bond_Oper_Decor)),
    (r'(\[\s*)(' + ka_identifier + r')(\.)(' + ka_identifier + r')(\s*/\s*)(\d+|\.)(\s*\])',    # [site.Agent/.]
        bygroups(Site_Bond_Oper_Decor, Site_Bond_Oper_State_Site, Site_Bond_Oper_Decor, Site_Bond_Oper_State_Agent, Site_Bond_Oper_Decor, Site_Bond_Oper_State, Site_Bond_Oper_Decor)),
        # internal states
    (r'({\s*)(' + ka_identifier + r'|#)(\s*})',                                                 # {ph}
        bygroups(Site_Int_Decor, Site_Int_State, Site_Int_Decor)),
    (r'({\s*)(' + ka_identifier + r'|#)(\s*/\s*)(' + ka_identifier + r')(\s*})',                # {ph/un}
        bygroups(Site_Int_Oper_Decor, Site_Int_Oper_State, Site_Int_Oper_Decor, Site_Int_Oper_State, Site_Int_Oper_Decor)),
    # counter states
    (r'({\s*(?:>=|>|=)\s*)(\d+)(\s*})',                                                         # {>55}
        bygroups(Site_Count_Decor, Site_Count_State, Site_Count_Decor)),
    (r'({\s*=\s*)(' + ka_identifier + r')(\s*})',                                               # {=x}
        bygroups(Site_Count_Decor, Site_Count_State, Site_Count_Decor)),
    (r'({\s*[-+]=\s*)(-?\d+)(\s*})',                                                            # {+= -55}
        bygroups(Site_Count_Oper_Decor, Site_Count_Oper_State, Site_Count_Oper_Decor)),
    (r'({\s*=\s*)(\d+)(\s*/\s*[+-]=\s*)(-?\d+)(\s*})',                                          # {= 55 / += -3}
        bygroups(Site_Count_Oper_Decor, Site_Count_Oper_State, Site_Count_Oper_Decor, Site_Count_Oper_State, Site_Count_Oper_Decor)),
    # rest of components
    (r'\s', Agent_Sign),
    (r',', Agent_Sign_Decor),
    (ka_identifier, Site_Name)
]

agent_declaration_components = [
    # comments
    (r'//.*?$', Comment.Singleline),
    (r'/\*', Comment.Multiline, 'comment'),
    # kappa
    (r'\)', Dec_Ag_Decor, '#pop'),                                  # end of expression
    (r'({\s*=\s*)(\d+)(\s*/\s*[+-]=\s*)(-?\d+)(\s*})',              # {= 55 / += 3} :: counters
        bygroups(Dec_Ag_Sign_Site_Ct_d, Dec_Ag_Sign_Site_Ct_s, Dec_Ag_Sign_Site_Ct_d, Dec_Ag_Sign_Site_Ct_s, Dec_Ag_Sign_Site_Ct_d)),
    (r'({\s*=\s*)(\d+)(\s*})',                                      # {= 55 } :: counters_cont
        bygroups(Dec_Ag_Sign_Site_Ct_d, Dec_Ag_Sign_Site_Ct_s, Dec_Ag_Sign_Site_Ct_d)),
    (r'\[', Dec_Ag_Sign_Site_Bd_d, 'declaration_bond_type'),        # change state
    (r'{', Dec_Ag_Sign_Site_In_d, 'declaration_internal_list'),     # change state
    # rest of components
    (r'\s+', Dec_Ag_Sign_Decor),
    (r',', Dec_Ag_Sign_Decor),
    (ka_identifier, Dec_Ag_Sign_Site_Name)
]

declaration_bond_type_components = [
    # comments
    (r'//.*?$', Comment.Singleline),
    (r'/\*', Comment.Multiline, 'comment'),
    # bond data
    (r'\]', Dec_Ag_Sign_Site_Bd_d, '#pop'),
    (r'(' + ka_identifier + r')(\.)(' + ka_identifier + r')', bygroups(Dec_Ag_Sign_Site_Bd_s, Dec_Ag_Sign_Site_Bd_d, Dec_Ag_Sign_Site_Bd_a)),
    (r'\s+', Dec_Ag_Sign_Site_Bd_d),
    (r',', Dec_Ag_Sign_Site_Bd_d)
]

declaration_internal_list_components = [
    # comments
    (r'//.*?$', Comment.Singleline),
    (r'/\*', Comment.Multiline, 'comment'),
    # internal state data
    (r'}', Dec_Ag_Sign_Site_In_d, '#pop'),
    (ka_identifier, Dec_Ag_Sign_Site_In_s),
    (r'\s+', Dec_Ag_Sign_Site_In_d),
    (r',', Dec_Ag_Sign_Site_In_d)
]

comment_components = [
    (r'[^*/]', Comment.Multiline),
    (r'/\*', Comment.Multiline, '#push'),
    (r'\*/', Comment.Multiline, '#pop'),
    (r'[*/]', Comment.Multiline)
]


class KappaLexer(RegexLexer):
    """Pygments lexer for the Kappa language (https://kappalanguage.org)"""
    name = 'Kappa'
    aliases = ['kappa']
    filenames = ['*.ka']

    tokens = {
        'root': [
            # comments
            (r'//.*?$', Comment.Singleline),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'\s+', Whitespace),
            # agent name
            (r'(' + ka_identifier + r')(\()', bygroups(Agent_Name, Agent_Decor), 'agent_rule'),
            # various keywords
            (r'(%agent:)(\s*)(' + ka_identifier + r')(\()', bygroups(Dec_Keyword, Whitespace, Dec_Ag_Name, Dec_Ag_Decor),
             'agent_declaration'),
            (r'(%token:)(\s*)(' + ka_identifier + r')', bygroups(Dec_Keyword, Whitespace, String)),
            (words(('obs', 'init', 'var', 'plot', 'def'),
                   prefix='%', suffix=':'), Misc_Keyword),
            (words(('?', ':', 'log', 'sin', 'cos', 'tan', 'exp', 'int', 'mod', 'sqrt', 'pi', 'max', 'min'),
                   prefix=r'\[\s*', suffix=r'\s*\]'), Misc_Func),
            # perturbation language
            (r'%mod:', Pert_Keyword),
            (r';', Pert_Keyword),
            (words(('INF', 'inf', 'alarm'),
                   prefix=r'\b', suffix=r'\b'), Pert_Constructs),
            (words(('true', 'false', 'not', 'E', 'E+', 'T', 'Tsim', 'Emax', 'Tmax'),
                   prefix=r'\[\s*', suffix=r'\s*\]'), Pert_Constructs),
            (words(('do', 'repeat'),
                   prefix=r'\b', suffix=r'\b'), Pert_Decor),
            (words(('APPLY', 'DEL', 'ADD', 'SNAPSHOT', 'STOP', 'DIN', 'TRACK', 'UPDATE', 'PRINT', 'PRINTF', 'RUN',
                    'SPECIES_OF'),
                   prefix=r'\$', suffix=r'\b'), Pert_Oper),
            (words(('&&', '||')), Pert_Constructs),
            # double-quoted, unquoted, and single-quoted strings
            (r'"[^"]+"', Pert_FileName),
            (r"([_~][a-zA-Z0-9~+_]+|[a-zA-Z][a-zA-Z0-9_~+-]*)|('[^']*')", String),
            # numbers
            (ka_real, Number),
            (ka_integer, Number),
            # rule decorations & markers
            (r'@|<->|->|{|}|:', Rule_Decor),
            (r',', Rule_Decor),
            (r'[-+/*^|><=()]', Alge_Oper),
            (r'\.', Rule_Decor)             # chemical notation placeholder marking agent creation/destruction
        ],
        'comment': comment_components,
        'agent_rule': agent_rule_components,
        'agent_declaration' : agent_declaration_components,
        'declaration_bond_type' : declaration_bond_type_components,
        'declaration_internal_list' : declaration_internal_list_components
    }
