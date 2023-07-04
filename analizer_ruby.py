from main import tokens
import ply.lex as lex
import ply.yacc as yacc

symbol_table = {}  # Tabla de símbolos para almacenar variables y sus valores
hashes_table = {}
function_table = {}  # Tabla de funciones para almacenar funciones y sus declaraciones

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
        if result is not None:
            print(result)

def update_errors(error_message):
    errors_list.append(error_message)
