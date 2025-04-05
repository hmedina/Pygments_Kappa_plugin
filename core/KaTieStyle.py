#! /usr/bin/env python3

from pygments.style import Style
from core.KappaToken import *
from core.KaTieToken import *
from core.KappaStyle import *

class KaTieStyleDeltas(Style):
    """Inspired by the Deltas style for Kappa's edit notation, extended to distinguish KaTie's various labels."""
    default_style = ''
    styles = {
        String: '#808080 italic',
        Agent_Name: 'bold',
        Site_Bond_State_Agent: 'bold',
        Site_Bond_Oper_State_Agent: 'bold',
        Site_Bond_Oper: 'bg:#c9f2d6',
        Site_Int_Oper: 'bg:#c9e4f2',
        Agent_Oper: 'bg:#f2c9e4',
        Site_Count_Oper: 'bg:#f2d6c9',
        Rule_Decor: '#cc0000',
        Comment: 'bg:#b3b3b3',
        Match_Event_Label: '#990000 italic',
        Match_Agent_Label: '#674ea7 italic',
        Return_Label: '#bf9000 italic'
    }

class KaTieStyleDeltasDark(Style):
    """Related to KaTie's Deltas style, but adapted for dark backgrounds."""
    default_style = ''
    background_color = '#000'
    styles = {
        Token.Kappa: '#eee',
        String: '#aaa italic',
        Agent_Name: 'bold',
        Site_Bond_State_Agent: 'bold',
        Site_Bond_Oper_State_Agent: 'bold',
        Site_Bond_Oper: '#fff bg:#0e750e',
        Site_Int_Oper: '#fff bg:#0e0e75',
        Site_Count_Oper: '#fff bg:#0e0e75',
        Agent_Oper: '#fff bg:#750e0e',
        Rule_Decor: '#a31414',
        Comment: 'bg:#666',
        Match_Event_Label: '#f4cccc italic',
        Match_Agent_Label: '#b4a7d6 italic',
        Return_Label: '#ffe599 italic'
    }
