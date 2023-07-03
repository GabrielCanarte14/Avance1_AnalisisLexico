from main import tokens
import ply.yacc as yacc

#Estructuras de datos

#Set

def p_sets(p):
    '''
    statement : set_vacio
    | set_numero
    '''

def p_set_vacio(p):
    '''
    set_vacio : ID EQUALS LCURLYBRACKET RCURLYBRACKET
    '''
def p_set(p):
    '''
    set_numero : ID EQUALS LCURLYBRACKET varios_elementos RCURLYBRACKET
    '''

def p_varios_elementos(p):
    '''
    varios_elementos : STR
    | numero
    | STR COMMA varios_elementos
    | numero COMMA varios_elementos
    '''

#Array

def p_array(p):
    '''
    statement : array_vacio
    | array_numero
    | array_str
    '''

def p_array_vacio(p):
    '''
    array_vacio : ID EQUALS LBRACKET RBRACKET
    '''

def p_array_numeros(p):
    '''
    array_numero : ID EQUALS LBRACKET varios_numeros RBRACKET
    '''

def p_array_str(p):
    '''
    array_str : ID EQUALS LBRACKET varios_str RBRACKET
    '''




#Hash

def p_hash(p):
    '''
    statement : hash_vacio
    | hash_elementos
    '''

def p_hash_vacio(p):
    '''
    hash_vacio : ID EQUALS LCURLYBRACKET RCURLYBRACKET
    '''

def p_hash_elementos(p):
    '''
    hash_elementos : ID EQUALS LCURLYBRACKET varios_pares_hash RCURLYBRACKET
    '''

def p_varios_pares_hash(p):
    '''
    varios_pares_hash : ID COLON valor
    | STR HASHAS valor
    | ID COLON valor COMMA varios_pares_hash
    | STR HASHAS valor COMMA varios_pares_hash
    '''


#Estrcuturas de Control

#IF
def p_sentencia_if(p):
    '''
    statement : IF comparaciones statement END_LOWER
    '''


#Loop
def p_sentencia_loop(p):
    '''
    statement : LOOP DO statement BREAK IF comparacion
    '''

#Case-when
def p_case_when(p):
    '''
    statement : CASE valor when_clauses ELSE statement_list END_LOWER
    | CASE valor when_clauses ELSE PUTS valor END_LOWER
    '''

def p_when_clauses(p):
    '''
    when_clauses : when_clause
    | when_clauses when_clause
    '''

def p_when_clause(p):
    '''
   when_clause : WHEN valor THEN statement_list
   | WHEN valor PUTS valor
    '''



#Declaraciones

def p_declaracion_basica(p):
    '''
    statement : DEF ID LPARENTHESIS RPARENTHESIS statement END_LOWER
    '''

def p_declaracion_parametros(p):
   '''
    statement : DEF ID LPARENTHESIS argumentos RPARENTHESIS statement END_LOWER
    '''

def p_declaracion_parametros_return(p):
    '''
    statement : DEF ID LPARENTHESIS argumentos RPARENTHESIS statement RETURN valor END_LOWER
    '''

def p_print(p):
    '''
    statement : PUTS valor
    '''


#Gabriel Cañarte

def p_varios_str(p):
    '''
    varios_str : STR
    | STR COMMA STR
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




def p_argumentos(p):
    '''
    argumentos : ID
    | ID COMMA argumentos
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
    | boolean
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


def p_asignacion_arimetica(p):
    '''
    statement : ID EQUALS expresion
    '''


def p_operador_aritmetico(p):
    '''
    operador_aritmetico : PLUS
    | MINUS
    | MULTIPLY
    | DIVIDE
    | MODULO
    | EXPONENT
    '''

def p_expresion(p):
    '''
    expresion : numero operador_aritmetico numero
    | ID operador_aritmetico numero
    | ID operador_aritmetico ID
    | numero operador_aritmetico ID
    '''

def p_booleans(p):
    '''
    boolean : TRUE
    | FALSE
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