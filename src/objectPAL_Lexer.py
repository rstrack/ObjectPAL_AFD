import ply.lex as lex

from src.keywords import palavrasReservadas

class ObjectPAL_Lexer():
    def __init__(self) -> None:
        self.build()

    regexPRS = '|'.join(palavrasReservadas)

    dictPRS = {pr:'PRS' for pr in palavrasReservadas}

    # List of token names.   This is always required
    tokens = [
    'NUM',
    'LPAR',
    'RPAR',
    'LCOL',
    'RCOL',
    'OARS',
    'IDN',
    'ATR',
    'BOO',
    'STR',
    'CAR',
    'PRS',
    'PTO',
    'COM',
    'NIN'
    ]

    t_LPAR  = r'\('
    t_RPAR  = r'\)'
    t_LCOL  = r'\['
    t_RCOL  = r'\]'
    t_PTO = r','

    @lex.TOKEN(r'\d+([.]\d*)?')
    def t_NUM(self, t):
        t.value = t.value 
        return t

    @lex.TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
    def t_IDN(self, t):
        t.type = self.dictPRS.get(t.value,'IDN')
        return t

    @lex.TOKEN(r'(and|or|not|<(>|=)?|>(=)?|[-*=+/])')
    def t_OARS(self, t):
        t.value = t.value
        return t

    @lex.TOKEN(r'=')
    def t_ATR(self, t):
        t.value = t.value 
        return t

    @lex.TOKEN(r'True|False')
    def t_BOO(self, t):
        t.type = self.dictPRS.get(t.value,'BOO')
        return t

    @lex.TOKEN(r'"[^"]*"')
    def t_STR(self, t):
        t.value = t.value 
        return t

    @lex.TOKEN(r';.*|{[^}]*}')
    def t_COM(self, t):
        t.value = t.value 
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore  = ' \t'

    def t_error(self, t):
        _t = t
        _t.type = 'NIN'
        _t.value = t.value[0]
        t.lexer.skip(1)
        return _t

    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, line):
        self.lexer.input(line)

    def token(self):
        return self.lexer.token()