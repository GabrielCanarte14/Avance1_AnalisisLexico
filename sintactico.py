from main import tokens
import ply.yacc as yacc

# Reglas de gramática y acciones semánticas
symbol_table = {}  # Tabla de símbolos para almacenar variables y sus valores

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

def p_expression_int(p):
    'expression : INT'
    p[0] = p[1]

def p_expression_float(p):
    'expression : FLOAT'
    p[0] = p[1]

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


def p_expression_logicals(p):
    '''
    expression : expression EQUAL expression
               | expression GREATER_THAN expression
               | expression LESS_THAN expression
               | expression GREATER_THAN_EQUAL expression
               | expression LESS_THAN_EQUAL expression
    '''
    operator = p[2]
    operand1 = p[1]
    operand2 = p[3]

    if operator == '==':
        p[0] = operand1 == operand2
    elif operator == '>':
        p[0] = operand1 > operand2
    elif operator == '<':
        p[0] = operand1 < operand2
    elif operator == '>=':
        p[0] = operand1 >= operand2
    elif operator == '<=':
        p[0] = operand1 <= operand2
def p_expression_logical(p):
    '''
    expression : expression OP_AND expression
    | expression OP_OR expression
    '''
    operator = p[2]
    operand1 = p[1]
    operand2 = p[3]

    if operator == '&&':
        p[0] = operand1 and operand2
    elif operator == '||':
        p[0] = operand1 or operand2

    if p[0] is None:
        print("Error semántico: Operación lógica inválida")


def p_error(p):
    print("Error de sintaxis")

sintactico = yacc.yacc()

while True:
   try:
       s = input('ruby > ')
   except EOFError:
       break
   if not s: continue
   result = sintactico.parse(s)
   print(symbol_table)
   if result!=None: print(result)
