from main import tokens
import ply.lex as lex
import ply.yacc as yacc

symbol_table = {}  # Tabla de símbolos para almacenar variables y sus valores
hashes_table = {}
arrays_table = {}
function_table = {}  # Tabla de funciones para almacenar funciones y sus declaraciones
sets_table = {}

def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]


def p_expression_assignment(p):
    'expression : ID EQUALS expression'
    variable_name = p[1]
    expression_value = p[3]

    symbol_table[variable_name] = expression_value
    p[0] = expression_value


def p_expression_binary_operation(p):
    '''
    expression : expression PLUS expression
    | expression MINUS expression
    | expression MULTIPLY expression
    | expression DIVIDE expression
    '''
    operator = p[2]
    operand1 = p[1]
    operand2 = p[3]

    if operator == '+':
        p[0] = operand1 + operand2
    elif operator == '-':
        p[0] = operand1 - operand2
    elif operator == '*':
        p[0] = operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            p[0] = operand1 / operand2
        else:
            print("Error semántico: División entre cero")
            error_message = f"Error semántico: División entre cero \n"
            update_errors(error_message)

def p_set(p):
    '''
    statement : set_vacio
    | set_elementos
    '''

def p_set_vacio(p):
    '''
    set_vacio : ID EQUALS SET LCURLYBRACKET RCURLYBRACKET
    '''
    set_name = p[1]
    sets_table[set_name] = {}
    if set_name in hashes_table:
        print(f"Error semántico: El set '{set_name}' ya ha sido creado anteriormente")
    else:
        sets_table[set_name] = set()

def p_set_elementos(p):
    '''
    set_elementos : ID EQUALS SET LCURLYBRACKET varios_set_elementos RCURLYBRACKET
    '''
    set_name = p[1]
    if set_name in sets_table:
        print(f"Error semántico: El set '{set_name}' ya ha sido creado anteriormente")
    else:
        set_elements = p[5]
        sets_table[set_name] = set_elements

def p_varios_set_elementos(p):
    '''
    varios_set_elementos : INT
    | STR
    | FLOAT
    | INT COMMA varios_set_elementos
    | FLOAT COMMA varios_set_elementos
    | STR COMMA varios_set_elementos 
    '''
    if len(p) == 2:
        p[0] = set((p[1], ))
    else:
        elemento = p[1]
        p[0] = set(elemento)

def p_array(p):
    '''
    statement : array_vacio
    '''
    p[0] = p[1]

def p_array_vacio(p):
    '''
    array_vacio : ID EQUALS LBRACKET RBRACKET
    '''
    array_name = p[1]
    arrays_table[array_name] = []
    if array_name in arrays_table:
        print(f"Error semántico: El array '{array_name}' ya ha sido creado anteriormente")
        error_message = f"Error semántico: El array '{array_name}' ya ha sido creado anteriormente \n"
        update_errors(error_message)
    else:
        arrays_table[array_name] = []



def p_array_str(p):
    '''
    array_str : ID EQUALS LBRACKET varios_str RBRACKET
    '''
def p_varios_str(p):
    '''
    varios_str : STR
    | STR COMMA STR
    '''
    

def p_hash(p):
    '''
    statement : hash_vacio
    | hash_elementos
    '''
    p[0] = p[1]

def p_hash_vacio(p):
    '''
    hash_vacio : ID EQUALS LCURLYBRACKET RCURLYBRACKET
    '''
    hash_name = p[1]
    hashes_table[hash_name] = {}
    if hash_name in hashes_table:
        print(f"Error semántico: El hash '{hash_name}' ya ha sido creado anteriormente")
        error_message = f"Error semántico: El hash '{hash_name}' ya ha sido creado anteriormente \n"
        update_errors(error_message)
    else:
        hashes_table[hash_name] = {}

def p_hash_elementos(p):
    '''
    hash_elementos : ID EQUALS LCURLYBRACKET varios_pares_hash RCURLYBRACKET
    '''

    hash_name = p[1]
    if hash_name in hashes_table:
        print(f"Error semántico: El hash '{hash_name}' ya ha sido creado anteriormente")
        error_message = f"Error semántico: El hash '{hash_name}' ya ha sido creado anteriormente \n"
        update_errors(error_message)
    else:
        hash_elements = p[4]
        hashes_table[hash_name] = hash_elements

def p_varios_pares_hash(p):
    '''
    varios_pares_hash : ID COLON expression
    | STR HASHAS expression
    | ID COLON expression COMMA varios_pares_hash
    | STR HASHAS expression COMMA varios_pares_hash
    '''

    if len(p) == 4:
        key = p[1]
        value = p[3]
        p[0] = {key: value}
    else:
        key = p[1]
        value = p[3]
        rest_of_hash = p[5]
        rest_of_hash[key] = value
        p[0] = rest_of_hash

def p_expression_int(p):
    'expression : INT'
    p[0] = int(p[1])


def p_expression_float(p):
    'expression : FLOAT'
    p[0] = float(p[1])


def p_expression_string(p):
    'expression : STR'
    p[0] = p[1]


def p_expression_id(p):
    'expression : ID'
    variable_name = p[1]
    if variable_name in symbol_table:
        p[0] = symbol_table[variable_name]
    else:
        print(f"Error semántico: Variable '{variable_name}' no definida")
        error_message =f"Error semántico: Variable '{variable_name}' no definida \n"
        update_errors(error_message)

def p_print_str(p):
    '''
    statement : PUTS STR
    '''
    valor = p[2]
    valor = valor.strip('"')
    print(valor)

def p_print_int(p):
    '''
    statement : PUTS INT
    '''
    print(p[2])

def p_print_float(p):
    '''
    statement : PUTS FLOAT
    '''
    print(p[2])



def p_error(p):
    if p:
        error_message = f"Error de sintaxis en token: {p.type}\n"
        update_errors(error_message)
    else:
        error_message = "Syntax error at EOF\n"
        update_errors(error_message)

# Build the parser
analizador = yacc.yacc()

# Variable para almacenar los errores
errors_list = []

def analyze_code(code):
    lines = code.splitlines()
    for line in lines:
        if not line.strip():
            continue
        result = analizador.parse(line)
        print(symbol_table)
        print(hashes_table)
        print(sets_table)
        if result is not None:
            print(result)

def update_errors(error_message):
    errors_list.append(error_message)
