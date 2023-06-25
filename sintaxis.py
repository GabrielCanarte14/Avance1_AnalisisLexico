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