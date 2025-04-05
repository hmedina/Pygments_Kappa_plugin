#! /usr/bin/env python3

from pygments.lexer import RegexLexer, bygroups
from core.KappaToken import *
from core.KappaLexer import ka_identifier, agent_rule_components, agent_declaration_components, declaration_bond_type_components, declaration_internal_list_components, comment_components
from core.KaTieToken import *


class KaTieLexer(RegexLexer):
    """Pygments lexer for the Kappa Trace inquiry engine (https://github.com/jonathan-laurent/KaTie)"""
    name = 'KaTie'
    aliases = ['katie', 'KaTIE']
    filenames = ['*.katie']

    ident = r'(' + ka_identifier + r')'

    tokens = {
        'root': [
            # comments
            (r'//.*?$', Comment.Singleline),
            (r'/\*', Comment.Multiline, 'comment'),
            # top level KaTIE keywords
            (r"(query)(\s*)(')([^']+)(')", bygroups(Pert_Keyword, Whitespace, String, String, String)),
            (r'match', Pert_Keyword, 'clause'),
        ],
        'clause': [
            (r'(\s*)' + ident + r'(\s*)(:)(\s*)({)(\s*)', bygroups(Whitespace, Match_Event_Label, Whitespace, Pert_Decor, Whitespace, Pert_Decor, Whitespace), 'event_pattern'),
            (r'(\s*)(first)(\s*)' + ident + r'(\s*)(:)(\s*)({)(\s*)', bygroups(Whitespace, Pert_Keyword, Whitespace, Match_Event_Label, Whitespace, Pert_Decor, Whitespace, Pert_Decor, Whitespace), 'event_pattern'),
            (r'(\s*)(last)(\s*)' + ident + r'(\s*)(:)(\s*)({)(\s*)', bygroups(Whitespace, Pert_Keyword, Whitespace, Match_Event_Label, Whitespace, Pert_Decor, Whitespace, Pert_Decor, Whitespace), 'event_pattern'),
            (r'(\s*)(before)(\s*)' + ident, bygroups(Whitespace, Pert_Keyword, Whitespace, Match_Event_Label)),
            (r'(\s*)(after)(\s*)' + ident, bygroups(Whitespace, Pert_Keyword, Whitespace, Match_Event_Label)),
            (r'(\s*)(and)(\s*)', bygroups(Whitespace, Pert_Keyword, Whitespace)),
            (r'(\s*)(return)(\s*)({)', bygroups(Whitespace, Pert_Keyword, Whitespace, Pert_Decor), 'return_measure_list')
        ],
        'event_pattern': [
            (r'([+-]?)' + ident + r'(\s*)(:)(\s*)', bygroups(Agent_Oper, Match_Agent_Label, Whitespace, Pert_Decor, Whitespace), 'edit_rule_part'),
            (r'(\s*)(,)(\s*)', bygroups(Whitespace, Pert_Decor, Whitespace)),
            (r'}', Pert_Decor, '#pop')
        ],
        'edit_rule_part' : [
            (r'(,)?(\s*)' + ident + r'(\()', bygroups(Rule_Decor, Whitespace, Agent_Name, Agent_Decor), 'agent_rule'),
            (r'\s*', Whitespace, '#pop')
        ],
        'return_measure_list': [
            (r"(\s*)(')" + ident + r"(')(\s*)(:)(\s*)", bygroups(Whitespace, Return_Label, Return_Label, Return_Label, Whitespace, Pert_Decor, Whitespace), 'return_measure'),
            (r'(\s*)(,)', bygroups(Whitespace, Pert_Decor)),
            (r'(\s*)(})', bygroups(Whitespace, Pert_Decor), '#pop'),
        ],
        'return_measure': [
            (r'(time)(\[)' + ident + r'(\])', bygroups(Pert_Oper, Pert_Decor, Match_Event_Label, Pert_Decor), '#pop'),
            (r'(rule)(\[)' + ident + r'(\])', bygroups(Pert_Oper, Pert_Decor, Match_Event_Label, Pert_Decor), '#pop'),
            (r'(sim_event_id)(\[)' + ident + r'(\])', bygroups(Pert_Oper, Pert_Decor, Match_Event_Label, Pert_Decor), '#pop'),
            (r'(event_id)({)' + ident + r'(})', bygroups(Pert_Oper, Pert_Decor, Match_Event_Label, Pert_Decor), '#pop'),
            (r'(debug_event)(\[)' + ident + r'(\])', bygroups(Pert_Oper, Pert_Decor, Match_Event_Label, Pert_Decor), '#pop'),
            (r'(agent_id)({)' + ident + r'(})', bygroups(Pert_Oper, Pert_Decor, Match_Agent_Label, Pert_Decor), '#pop'),
            (r"(count)({)(')" + ident + r"(')(}{)", bygroups(Pert_Oper, Pert_Decor, String, String, String, Pert_Decor), 'mixture_component'),
            (r'(size)({)', bygroups(Pert_Oper, Pert_Decor), 'mixture_component'),
            (r'(int_state)(\[)(\.)?' + ident + r'(\.)?(\]{)' + ident + r'(.)' + ident + r'(})(\s*)(})', bygroups(Pert_Oper, Pert_Decor, Pert_Decor, Match_Event_Label, Pert_Decor, Pert_Decor, Agent_Name, Agent_Sign_Decor, Site_Name, Pert_Decor, Whitespace, Pert_Decor), '#pop'),
            (r'(print_cc)(\[)(\.)?' + ident + r'(\.)?(\]{)' + ident + r'(})(\s*)(})', bygroups(Pert_Oper, Pert_Decor, Pert_Decor, Match_Event_Label, Pert_Decor, Pert_Decor, Match_Agent_Label, Pert_Decor, Whitespace, Pert_Decor), '#pop'),
            (r'(snapshot)(\[)(\.)?' + ident + r'(\.)?(\])', bygroups(Pert_Oper, Pert_Decor, Match_Event_Label, Pert_Decor, Pert_Decor), '#pop'),
        ],
        'mixture_component': [
            (r'(component)(\[)(\.)?' + ident + r'(\.)?(\]{)' + ident + r'(})(\s*)(})', bygroups(Pert_Oper, Pert_Decor, Pert_Decor, Match_Event_Label, Pert_Decor, Pert_Decor, Match_Agent_Label, Pert_Decor, Whitespace, Pert_Decor), '#pop:2'),
        ],
        # reusing these from the Kappa Lexer
        'comment': comment_components,
        'agent_rule': agent_rule_components,
        'agent_declaration' : agent_declaration_components,
        'declaration_bond_type' : declaration_bond_type_components,
        'declaration_internal_list' : declaration_internal_list_components
    }