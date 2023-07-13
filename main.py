import ply.lex as lex

# Crear los tokens para la siguiente sintaxis

# Diccionario de palabras reservadas
reserved = {'alias': 'ALIAS',
            'set' : 'SET',
            'rational' : 'Rational',
            'puts':'PUTS',
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
            'yield': 'YIELD',
            '_FILE_':'FILE',
            '_LINE_': 'LINE',
            'each': 'EACH',
            'loop': 'LOOP',
            }

# Sequencia de tokens, puede ser lista o tupla
tokens = (
        'ID',
        'EQUALS',
        'STR',
        'INT',
        'CONSTANT',
        'FLOAT',
        'COMPLEX',
        'RATIONAL', 
        'SYMBOL',
        'HASHAS',
        'ARRAY',
        'HASH',
        #  Caracteres Especiales
        'AT',
        'DOUBLYAT',
        'COMMA',
        'HASHTAG',
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
        'INDENT',
        'DEDENT'
         ) + tuple(reserved.values())

# Exp Regulares para tokens de símbolos
t_EQUALS = r'='
t_STR = r'("[^"]*")|(\'[^"]*\')'
t_INT = r'-?\d+'
t_FLOAT = r'-?\d*\.\d+([eE]-?\d)?'
t_SYMBOL = r'=:'
t_HASHAS = r'=>'

t_COMPLEX = r'(-?\d+)*\s[+|-]\s(\d+)*[i]'
t_RATIONAL = r'-?\d+\/[1-9]\d*'
t_ARRAY = r'\w+\s?=\s?\[("[^"]*",)*("[^"]*")+\]'
t_HASH = r'\w+\s?=\s?{(\s?:\w+\s?=>\s?"[^"]*",)*(\s?:\w+\s?=>\s?"[^"]*")+}'

t_AT = r'@'
t_DOUBLYAT = r'@@'
t_GLOBAL = r'\$'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_DOT = r'\.'
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
t_HASHTAG = r'\#'




# Para contabilizar nro de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


def t_CONSTANT(t):
    r'[A-Z][a-zA-Z_]\w+'
    t.type = reserved.get(t.value.lower(), 'CONSTANT')
    return t



# Expresión regular para comentarios
def t_COMMENTS(t):
    r'\#.*'
    pass

# Expresion regular para bloque de comentarios
def t_COMMENT_BLOCK(t):
    r'=begin\n(.*)\n?=end'
    pass



def t_INDENT(t):
    r'\n[ ]+'
    # Cálculo del nivel de indentación basado en la cantidad de espacios
    # y generación del token INDENT
    return t

# Regla para dedentación
def t_DEDENT(t):
    r'\n'
    # Cálculo del nivel de dedentación basado en la posición actual del token
    # y generación del token DEDENT
    return t

# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


# Presentación de errores léxicos
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Contruir analizador
lexer = lex.lex()

# Testeando
data = '''
:
hola => [hola,gola]
/
x = 123.5 + (5 * 22)
hola
else
return
if
y23
"hola"
=begin
ndjencje
=end

#Algoritmo Freddy Gómez
def factorial(n)
  if num <= 1
    return 1
  else
    return num * factorial(num - 1)
  end
end

number = 5
result = factorial(number)
puts "El factorial de #{number} es: #{result}"



#Algoritmo Gabriel Cañarte 
def obtener_divisores(numero)
  divisores = []
  (1..numero).each do |i|
    if numero % i == 0
      divisores << i
    end
  end
  return divisores
end

numero = 12
resultado = encontrar_divisores(numero)
puts "Los divisores de #{numero} son: #{resultado.join(", ")}"

#Algoritmo Danilo Torres
def binary_search(arr, target)
  low = 0
  high = arr.length - 1

  while low <= high do
    mid = (low + high) / 2
    if arr[mid] == target
      return mid
    elsif arr[mid] < target
      low = mid + 1
    else
      high = mid - 1
    end
  end

  return -1
end
array = [1, 3, 5, 7, 9]
target = 7
index = binary_search(array, target)
puts "El elemento #{target} se encuentra en el índice #{index}."

    '''

# Datos de entrada
lexer.input(data)

# Tokenizador
while True:
    tok = lexer.token()
    if not tok:
        break  # Rompe
    print(tok)
