from main import tokens
import ply.yacc as yacc

def p_array_vacio(p):
    '''
    array : ID EQUALS LBRACKET RBRACKET
    '''

def p_array_numeros(p):
    '''
    array : ID EQUALS LBRACKET varios_numeros RBRACKET
    '''

def p_array_str(p):
    '''
    array : ID EQUALS LBRACKET varios_str RBRACKET
    '''

def p_sentencia_asignacion(p):
    '''
    statement : ID EQUALS valor
    '''

def p_valor(p):
    '''
    valor : numero
    | STR
    | ID
    '''

def p_sentencia_if(p):
    '''
    statement : IF comparaciones bloque END_LOWER
    '''

def p_bloque(p):
    '''
    bloque : INDENT statement DEDENT
    '''

def p_statement_list(p):
    '''
    statement_list : statement_list statement
    | statement
    '''

def p_comparador(p):
    '''
    comparador : EQUAL
    | NOT_EQUAL
    | GREATER_THAN
    | LESS_THAN
    | GREATER_THAN_EQUAL
    | LESS_THAN_EQUAL
    '''

def p_comparacion_num(p):
    '''
    comparacion_num : numero comparador numero
    '''

def p_comparacion_variables(p):
    '''
    comparacion_variables : ID EQUAL ID
    | ID NOT_EQUAL ID
    '''

def p_comparacion(p):
    '''
    comparacion : comparacion_num
    | comparacion_variables
    '''

def p_comparaciones(p):
    '''
    comparaciones : comparacion
    | comparacion conector comparacion
    '''


def p_conector(p):
  '''conector : OP_AND
  | OP_OR
  '''

def p_numero(p):
    '''
    numero : INT
    | FLOAT
    '''

def p_varios_numeros(p):
    '''
    varios_numeros : numero
    | numero COMMA varios_numeros
    '''

def p_varios_str(p):
    '''
    varios_str : STR
    | STR COMMA STR
    '''



def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type)
         #sintactico.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
sintactico = yacc.yacc()

while True:
   try:
       s = input('ruby > ')
   except EOFError:
       break
   if not s: continue
   result = sintactico.parse(s)
   if result!=None: print(result)