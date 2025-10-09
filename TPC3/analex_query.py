
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<SELECT>select)|(?P<WHERE>where)|(?P<LIMIT>LIMIT)|(?P<A>a)|(?P<VAR>\?[a-zA-Z_][a-zA-Z0-9_]*)|(?P<STRING>"[^"]*")|(?P<ID_NS>[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*)|(?P<ID>[a-zA-Z_][a-zA-Z0-9_]*)|(?P<INT>\d+)|(?P<LBRACE>\{)|(?P<RBRACE>\})|(?P<DOT>\.)|(?P<AT>@)|(?P<SKIP>[ \t])|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())

        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['A']:
            t = ("A", dic['A'], linha, m.span())
    
        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
    
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
    
        elif dic['ID_NS']:
            t = ("ID_NS", dic['ID_NS'], linha, m.span())
    
        elif dic['ID']:
            t = ("ID", dic['ID'], linha, m.span())
    
        elif dic['INT']:
            t = ("INT", dic['INT'], linha, m.span())
    
        elif dic['LBRACE']:
            t = ("LBRACE", dic['LBRACE'], linha, m.span())
    
        elif dic['RBRACE']:
            t = ("RBRACE", dic['RBRACE'], linha, m.span())
    
        elif dic['DOT']:
            t = ("DOT", dic['DOT'], linha, m.span())
    
        elif dic['AT']:
            t = ("AT", dic['AT'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)    

