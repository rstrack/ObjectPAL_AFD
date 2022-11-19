import ply.lex as lex

palavrasReservadas = r'active|and|array|as|case|caseInsensitive|const|container|create|database|descending|disableDefault|doDefault|dynArray|else|enableDefault|endConst|endCreate|endFor|eEndForEach|endIf|endIndex|endMethod|endProc|endQuery|endRecord|endScan|endSort|endSwitch|endSwitchMenu|endTry|endType|endUses|endVar|endWhile|for|forEach|from|if|iif|in|index|indexStruct|is|key|lastMouseClicked|lastMouseRightClicked|like|loop|maintained|method|not|ObjectPAL|of|on|onFail|or|otherwise|passEvent|primary|proc|query|quitLoop|record|refIntStruct|retry|return|scan|secStruct|self|sort|step|struct|subject|switch|switchMenu|tag|then|to|try|type|unique|uses|var|where|while|with|without'

# List of token names.   This is always required
tokens = (
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
)

# Regular expression rules for simple tokens
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_LCOL  = r'\['
t_RCOL  = r'\]'

# A regular expression rule with some action code
@lex.TOKEN(r'\d+([.]\d)*')
def t_NUM(t):
    t.value = t.value 
    return t

@lex.TOKEN(r'(and|or|Not|<(>|=)?|>(=)?|=)')
def t_OARS(t):
    t.value = t.value 
    return t
'''
#@lex.TOKEN(r'(?!'+palavrasReservadas+ r')?')
@lex.TOKEN(r'(?!for)?')
def t_IDN(t):
    t.value = t.value 
    return t
'''
@lex.TOKEN(r'=')
def t_ATR(t):
    t.value = t.value 
    return t

@lex.TOKEN(r'True|False')
def t_BOO(t):
    t.value = t.value 
    return t

@lex.TOKEN(r'"[^"]*"')
def t_STR(t):
    t.value = t.value 
    return t
'''
@lex.TOKEN(r'')
def t_CAR(t):
    t.value = t.value 
    return t
'''
@lex.TOKEN(palavrasReservadas)
def t_PRS(t):
    t.value = t.value 
    return t
'''
@lex.TOKEN(r'')
def t_PTO(t):
    t.value = t.value 
    return t
'''
@lex.TOKEN(r';.*')
def t_COM(t):
    t.value = t.value 
    return t
'''
@lex.TOKEN(r'')
def t_NIN(t):
    t.value = t.value 
    return t
'''
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
const
endConst
if 9 > 8
    ObjectPAL ;kolcsjklnclsdjkncjkdsnc782347823784623"
    ObjectPAL
'''
linhas = data.split('\n')

for linha in linhas:
    lexer.input(linha)
    flag = True
    while(flag):
        tok = lexer.token()
        if tok: 
            print(tok)
        else:
            flag = False

''' VERSÃO WHILE TRUE
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.lexpos)
'''