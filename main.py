import ply.lex as lex

# Diccionario de palabras reservadas
reserved = {
    'alias': 'ALIAS',
    'and': 'AND',
    'begin': 'BEGIN',
    'break': 'BREAK',
    'case': 'CASE',
    'class': 'CLASS',
    'def': 'DEF',
    'defined': 'DEFINED',
    'do': 'DO',
    'else': 'ELSE',
    'elsif': 'ELSEIF',
    'end': 'END_LOWER',
    'END': 'END_UPPER',
    'ensure': 'ENSURE',
    'true': 'TRUE',
    'false': 'FALSE',
    'for': 'FOR',
    'if': 'IF',
    'in': 'IN',
    'module': 'MODULE',
    'next': 'NEXT',
    'nil': 'NIL',
    'not': 'NOT',
    'or': 'OR',
    'redo': 'REDO',
    'rescue': 'RESCUE',
    'retry': 'RETRY',
    'return': 'RETURN',
    'self': 'SELF',
    'super': 'SUPER',
    'then': 'THEN',
    'undef': 'UNDEF',
    'unless': 'UNLESS',
    'until': 'UNTIL',
    'when': 'WHEN',
    'while': 'WHILE',
    'yield': 'YIELD'
}

# Sequencia de tokens, puede ser lista o tupla
tokens = (
    'EQUALS',
    'STR',
    'INT',
    'CONSTANT',
    'FLOAT',
    'SYMBOL',
    'HASHAS',
    # Caracteres Especiales
    'AT',
    'COMMA',
    'LBRACKET',
    'RBRACKET',
    'LPARENTHESIS',
    'RPARENTHESIS',
    'LCURLYBRACKET',
    'RCURLYBRACKET',
    'DOT',
    'GLOBAL',
    'COLON',
    'SEMICOLON',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'EXPONENT',
    'EQUAL',
    'NOT_EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_THAN_EQUAL',
    'LESS_THAN_EQUAL',
    'OP_AND',
    'OP_OR',
    'OP_NOT',
    'BITWISE_AND',
    'BITWISE_OR',
    'BITWISE_XOR',
    'BITWISE_NOT',
    'SHIFT_LEFT',
    'SHIFT_RIGHT',
    'ID',
) + tuple(reserved.values())

# Exp Regulares para tokens de símbolos
t_EQUALS = r'='
t_STR = r'"[^"]*"'
t_INT = r'-?\d+'
t_FLOAT = r'-?\d*\.\d+([eE]-?\d)?'
t_SYMBOL = r'=:'
t_HASHAS = r'=>'

t_AT = r'@'
t_GLOBAL = r'\$'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_COMMA = r','
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_LCURLYBRACKET = r'\{'
t_RCURLYBRACKET = r'\}'
t_COLON = r':'
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_EXPONENT = r'\*\*'
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_THAN_EQUAL = r'>='
t_LESS_THAN_EQUAL = r'<='
t_OP_AND = r'&&'
t_OP_OR = r'\|\|'
t_OP_NOT = r'!'
t_BITWISE_AND = r'&'
t_BITWISE_OR = r'\|'
t_BITWISE_XOR = r'\^'
t_BITWISE_NOT = r'~'
t_SHIFT_LEFT = r'<<'
t_SHIFT_RIGHT = r'>>'


# Para contabilizar nro de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Función para reconocer constantes
def t_CONSTANT(t):
    r'[A-Z][a-zA-Z_]\w*'
    t.type = reserved.get(t.value.lower(), 'CONSTANT')
    return t


# Función para reconocer identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t



# Expresión regular para comentarios
def t_COMMENTS(t):
    r'\#.*'
    pass


# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


# Presentación de errores léxicos
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Construir analizador
lexer = lex.lex()

# Testeando
data = '''
hola => [hola,gola]
/
x = 123.5 + (5 * 22)
hola
else
return
if
y23
"hola"
'''

# Datos de entrada
lexer.input(data)

# Tokenizador
while True:
    tok = lexer.token()
    if not tok:
        break  # Rompe
    print(tok)
