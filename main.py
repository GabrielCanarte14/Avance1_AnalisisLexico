import ply.lex as lex

#Crear los tokens para la siguiente sintaxis

#SELECT * FROM Tabla
#SELECT campo1, campo2 from Tabla1 where campo==1
#SELECT campo1 as cedula from Datos where provincia<>"7"
#print(consulta)
#DELETE FROM datos WHERE id>1000
#print("SELECT * FROM Tabla")

#Diccionario de palabras reservadas
reserved = {'alias':'alias',
            'and':'and',
            'begin':'BEGIN',
            'break':'break',
            'case':'case',
            'class':'class',
            'def':'def',
            'defined':'defined',
            'do':'do',
            'else':'else',
            'elsif':'elsif',
            'end':'END',
            'true':'TRUE',
            'false':'FALSE'
           }

#Sequencia de tokens, puede ser lista o tupla
tokens = (
  'ID',
  'EQUALS',
  'STR',
  'INT',
  'AT',
  'GLOBAL',
  'CONSTANT',
  'FLOAT',
  'TRUE',
  'FALSE',
  'COMMA',
  'LBRACKET',
  'RBRACKET',
  'SYMBOL',
  'HASHAS'
) + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
t_EQUALS = r'='
t_STR = r'"[^"]*"'
t_INT = r'-?\d+'
t_AT = r'@'
t_GLOBAL = r'\$'
t_FLOAT = r'-?\d*\.\d+([eE]-?\d)?'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_COMMA = r','
t_SYMBOL = r'=:'
t_HASHAS = r'=>'

#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_ID(t):
  r'[a-z][a-zA-Z_]\w+'
  t.type = reserved.get(t.value.lower(), 'ID')
  return t

def t_CONSTANT(t):
  r'[A-Z][a-zA-Z_]\w+'
  t.type = reserved.get(t.value.lower(), 'CONSTANT')
  return t

def t_COMMENTS(t):
  r'\#.*'
  pass

# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)



#Contruir analizador
lexer = lex.lex()

#Testeando
data = '''
hola => [hola,gola]
    '''

#Datos de entrada
lexer.input(data)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)