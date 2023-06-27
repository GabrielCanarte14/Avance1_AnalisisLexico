
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ARRAY AT BEGIN BITWISE_AND BITWISE_NOT BITWISE_OR BITWISE_XOR BREAK CASE CLASS COLON COMMA COMPLEX CONSTANT DEDENT DEF DEFINED DIVIDE DO DOT EACH ELSE ELSEIF END_LOWER END_UPPER ENSURE EQUAL EQUALS EXPONENT FALSE FILE FLOAT FOR GLOBAL GREATER_THAN GREATER_THAN_EQUAL HASH HASHAS ID IF IN INDENT INT LBRACKET LCURLYBRACKET LESS_THAN LESS_THAN_EQUAL LINE LOOP LPARENTHESIS MINUS MODULE MODULO MULTIPLY NEXT NIL NOT NOT_EQUAL OP_AND OP_NOT OP_OR OR PLUS PUTS RATIONAL RBRACKET RCURLYBRACKET REDO RESCUE RETRY RETURN RPARENTHESIS SELF SEMICOLON SHIFT_LEFT SHIFT_RIGHT STR SUPER SYMBOL THEN TRUE UNDEF UNLESS UNTIL WHEN WHILE YIELD\n    statement : set_vacio\n    | set_numero\n    | set_str\n    \n    statement : array_vacio\n    | array_numero\n    | array_str\n    \n    array_vacio : ID EQUALS LBRACKET RBRACKET\n    \n    array_numero : ID EQUALS LBRACKET varios_numeros RBRACKET\n    \n    array_str : ID EQUALS LBRACKET varios_str RBRACKET\n    \n    set_vacio : ID EQUALS LCURLYBRACKET RCURLYBRACKET\n    \n    set_numero : ID EQUALS LCURLYBRACKET varios_numeros RCURLYBRACKET\n    \n    set_str : ID EQUALS LCURLYBRACKET varios_str RCURLYBRACKET\n    \n    statement : hash_vacio\n    | hash_elementos\n    \n    hash_vacio : ID EQUALS LCURLYBRACKET RCURLYBRACKET\n    \n    hash_elementos : ID EQUALS LCURLYBRACKET varios_pares_hash RCURLYBRACKET\n    \n    varios_pares_hash : ID COLON valor\n    | STR HASHAS valor\n    | ID COLON valor COMMA varios_pares_hash\n    | STR HASHAS valor COMMA varios_pares_hash\n    \n    statement : IF comparaciones statement END_LOWER\n    \n    statement : LOOP DO statement BREAK IF comparacion\n    \n    statement : CASE valor when_clauses ELSE statement_list END_LOWER\n    | CASE valor when_clauses ELSE PUTS valor END_LOWER\n    \n    when_clauses : when_clause\n    | when_clauses when_clause\n    \n   when_clause : WHEN valor THEN statement_list\n   | WHEN valor PUTS valor\n    \n    statement : DEF ID LPARENTHESIS RPARENTHESIS statement END_LOWER\n    \n    statement : DEF ID LPARENTHESIS argumentos RPARENTHESIS statement END_LOWER\n    \n    statement : DEF ID LPARENTHESIS argumentos RPARENTHESIS statement RETURN valor END_LOWER\n    \n    varios_str : STR\n    | STR COMMA STR\n    \n    statement : ID EQUALS valor\n    \n    valor : numero\n    | STR\n    | ID\n    \n    argumentos : ID\n    | ID COMMA argumentos\n    \n    statement_list : statement_list statement\n    | statement\n    \n    comparador : EQUAL\n    | NOT_EQUAL\n    | GREATER_THAN\n    | LESS_THAN\n    | GREATER_THAN_EQUAL\n    | LESS_THAN_EQUAL\n    \n    comparacion_num : numero comparador numero\n    \n    comparacion_variables : ID EQUAL ID\n    | ID NOT_EQUAL ID\n    \n    comparacion : comparacion_num\n    | comparacion_variables\n    \n    comparaciones : comparacion\n    | comparacion conector comparacion\n    conector : OP_AND\n  | OP_OR\n  \n    numero : INT\n    | FLOAT\n    \n    varios_numeros : numero\n    | numero COMMA varios_numeros\n    '
    
_lr_action_items = {'IF':([0,2,3,4,5,6,7,8,9,15,16,17,18,21,22,23,25,26,27,48,51,52,53,54,55,56,57,61,64,70,75,77,78,82,84,85,86,90,91,92,93,94,96,99,105,106,114,],[10,-1,-2,-3,-4,-5,-6,-13,-14,10,-53,-51,-52,-57,-58,10,-35,-36,-37,-34,-21,-54,-48,-49,-50,74,10,10,-10,-7,10,-41,10,10,-11,-12,-16,-8,-9,-22,-23,-40,10,-29,-24,-30,-31,]),'LOOP':([0,2,3,4,5,6,7,8,9,15,16,17,18,21,22,23,25,26,27,48,51,52,53,54,55,57,61,64,70,75,77,78,82,84,85,86,90,91,92,93,94,96,99,105,106,114,],[11,-1,-2,-3,-4,-5,-6,-13,-14,11,-53,-51,-52,-57,-58,11,-35,-36,-37,-34,-21,-54,-48,-49,-50,11,11,-10,-7,11,-41,11,11,-11,-12,-16,-8,-9,-22,-23,-40,11,-29,-24,-30,-31,]),'CASE':([0,2,3,4,5,6,7,8,9,15,16,17,18,21,22,23,25,26,27,48,51,52,53,54,55,57,61,64,70,75,77,78,82,84,85,86,90,91,92,93,94,96,99,105,106,114,],[12,-1,-2,-3,-4,-5,-6,-13,-14,12,-53,-51,-52,-57,-58,12,-35,-36,-37,-34,-21,-54,-48,-49,-50,12,12,-10,-7,12,-41,12,12,-11,-12,-16,-8,-9,-22,-23,-40,12,-29,-24,-30,-31,]),'DEF':([0,2,3,4,5,6,7,8,9,15,16,17,18,21,22,23,25,26,27,48,51,52,53,54,55,57,61,64,70,75,77,78,82,84,85,86,90,91,92,93,94,96,99,105,106,114,],[13,-1,-2,-3,-4,-5,-6,-13,-14,13,-53,-51,-52,-57,-58,13,-35,-36,-37,-34,-21,-54,-48,-49,-50,13,13,-10,-7,13,-41,13,13,-11,-12,-16,-8,-9,-22,-23,-40,13,-29,-24,-30,-31,]),'ID':([0,2,3,4,5,6,7,8,9,10,12,13,15,16,17,18,21,22,23,25,26,27,29,31,32,33,41,42,46,47,48,49,51,52,53,54,55,57,61,64,70,74,75,76,77,78,79,80,82,83,84,85,86,89,90,91,92,93,94,96,99,105,106,107,108,109,114,],[14,-1,-2,-3,-4,-5,-6,-13,-14,20,27,28,14,-53,-51,-52,-57,-58,14,-35,-36,-37,27,20,-55,-56,54,55,27,60,-34,63,-21,-54,-48,-49,-50,14,14,-10,-7,20,14,27,-41,14,27,60,14,27,-11,-12,-16,27,-8,-9,-22,-23,-40,14,-29,-24,-30,27,63,63,-31,]),'$end':([1,2,3,4,5,6,7,8,9,17,18,21,22,25,26,27,48,51,53,54,55,64,70,84,85,86,90,91,92,93,99,105,106,114,],[0,-1,-2,-3,-4,-5,-6,-13,-14,-51,-52,-57,-58,-35,-36,-37,-34,-21,-48,-49,-50,-10,-7,-11,-12,-16,-8,-9,-22,-23,-29,-24,-30,-31,]),'END_LOWER':([2,3,4,5,6,7,8,9,17,18,21,22,25,26,27,30,48,51,53,54,55,64,70,75,77,81,84,85,86,90,91,92,93,94,95,99,100,105,106,110,114,],[-1,-2,-3,-4,-5,-6,-13,-14,-51,-52,-57,-58,-35,-36,-37,51,-34,-21,-48,-49,-50,-10,-7,93,-41,99,-11,-12,-16,-8,-9,-22,-23,-40,105,-29,106,-24,-30,114,-31,]),'BREAK':([2,3,4,5,6,7,8,9,17,18,21,22,25,26,27,43,48,51,53,54,55,64,70,84,85,86,90,91,92,93,99,105,106,114,],[-1,-2,-3,-4,-5,-6,-13,-14,-51,-52,-57,-58,-35,-36,-37,56,-34,-21,-48,-49,-50,-10,-7,-11,-12,-16,-8,-9,-22,-23,-29,-24,-30,-31,]),'ELSE':([2,3,4,5,6,7,8,9,17,18,21,22,25,26,27,44,45,48,51,53,54,55,58,64,70,77,84,85,86,90,91,92,93,94,96,97,99,105,106,114,],[-1,-2,-3,-4,-5,-6,-13,-14,-51,-52,-57,-58,-35,-36,-37,57,-25,-34,-21,-48,-49,-50,-26,-10,-7,-41,-11,-12,-16,-8,-9,-22,-23,-40,-27,-28,-29,-24,-30,-31,]),'WHEN':([2,3,4,5,6,7,8,9,17,18,21,22,24,25,26,27,44,45,48,51,53,54,55,58,64,70,77,84,85,86,90,91,92,93,94,96,97,99,105,106,114,],[-1,-2,-3,-4,-5,-6,-13,-14,-51,-52,-57,-58,46,-35,-36,-37,46,-25,-34,-21,-48,-49,-50,-26,-10,-7,-41,-11,-12,-16,-8,-9,-22,-23,-40,-27,-28,-29,-24,-30,-31,]),'RETURN':([2,3,4,5,6,7,8,9,17,18,21,22,25,26,27,48,51,53,54,55,64,70,84,85,86,90,91,92,93,99,100,105,106,114,],[-1,-2,-3,-4,-5,-6,-13,-14,-51,-52,-57,-58,-35,-36,-37,-34,-21,-48,-49,-50,-10,-7,-11,-12,-16,-8,-9,-22,-23,-29,107,-24,-30,-31,]),'INT':([10,12,29,31,32,33,34,35,36,37,38,39,40,46,49,50,74,76,79,83,87,89,107,],[21,21,21,21,-55,-56,21,-42,-43,-44,-45,-46,-47,21,21,21,21,21,21,21,21,21,21,]),'FLOAT':([10,12,29,31,32,33,34,35,36,37,38,39,40,46,49,50,74,76,79,83,87,89,107,],[22,22,22,22,-55,-56,22,-42,-43,-44,-45,-46,-47,22,22,22,22,22,22,22,22,22,22,]),'DO':([11,],[23,]),'STR':([12,29,46,49,50,76,79,83,88,89,107,108,109,],[26,26,26,69,73,26,26,26,103,26,26,112,112,]),'EQUALS':([14,],[29,]),'OP_AND':([16,17,18,21,22,53,54,55,],[32,-51,-52,-57,-58,-48,-49,-50,]),'OP_OR':([16,17,18,21,22,53,54,55,],[33,-51,-52,-57,-58,-48,-49,-50,]),'EQUAL':([19,20,21,22,],[35,41,-57,-58,]),'NOT_EQUAL':([19,20,21,22,],[36,42,-57,-58,]),'GREATER_THAN':([19,21,22,],[37,-57,-58,]),'LESS_THAN':([19,21,22,],[38,-57,-58,]),'GREATER_THAN_EQUAL':([19,21,22,],[39,-57,-58,]),'LESS_THAN_EQUAL':([19,21,22,],[40,-57,-58,]),'THEN':([21,22,25,26,27,59,],[-57,-58,-35,-36,-37,78,]),'PUTS':([21,22,25,26,27,57,59,],[-57,-58,-35,-36,-37,76,79,]),'COMMA':([21,22,25,26,27,60,68,69,73,101,104,],[-57,-58,-35,-36,-37,80,87,88,88,108,109,]),'RCURLYBRACKET':([21,22,25,26,27,49,65,66,67,68,69,101,102,103,104,111,113,],[-57,-58,-35,-36,-37,64,84,85,86,-59,-32,-17,-60,-33,-18,-19,-20,]),'RBRACKET':([21,22,50,68,71,72,73,102,103,],[-57,-58,70,-59,90,91,-32,-60,-33,]),'LPARENTHESIS':([28,],[47,]),'LCURLYBRACKET':([29,],[49,]),'LBRACKET':([29,],[50,]),'RPARENTHESIS':([47,60,62,98,],[61,-38,82,-39,]),'COLON':([63,],[83,]),'HASHAS':([69,112,],[89,89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,15,23,57,61,75,78,82,96,],[1,30,43,77,81,94,77,100,94,]),'set_vacio':([0,15,23,57,61,75,78,82,96,],[2,2,2,2,2,2,2,2,2,]),'set_numero':([0,15,23,57,61,75,78,82,96,],[3,3,3,3,3,3,3,3,3,]),'set_str':([0,15,23,57,61,75,78,82,96,],[4,4,4,4,4,4,4,4,4,]),'array_vacio':([0,15,23,57,61,75,78,82,96,],[5,5,5,5,5,5,5,5,5,]),'array_numero':([0,15,23,57,61,75,78,82,96,],[6,6,6,6,6,6,6,6,6,]),'array_str':([0,15,23,57,61,75,78,82,96,],[7,7,7,7,7,7,7,7,7,]),'hash_vacio':([0,15,23,57,61,75,78,82,96,],[8,8,8,8,8,8,8,8,8,]),'hash_elementos':([0,15,23,57,61,75,78,82,96,],[9,9,9,9,9,9,9,9,9,]),'comparaciones':([10,],[15,]),'comparacion':([10,31,74,],[16,52,92,]),'comparacion_num':([10,31,74,],[17,17,17,]),'comparacion_variables':([10,31,74,],[18,18,18,]),'numero':([10,12,29,31,34,46,49,50,74,76,79,83,87,89,107,],[19,25,25,19,53,25,68,68,19,25,25,25,68,25,25,]),'valor':([12,29,46,76,79,83,89,107,],[24,48,59,95,97,101,104,110,]),'conector':([16,],[31,]),'comparador':([19,],[34,]),'when_clauses':([24,],[44,]),'when_clause':([24,44,],[45,58,]),'argumentos':([47,80,],[62,98,]),'varios_numeros':([49,50,87,],[65,71,102,]),'varios_str':([49,50,],[66,72,]),'varios_pares_hash':([49,108,109,],[67,111,113,]),'statement_list':([57,78,],[75,96,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> set_vacio','statement',1,'p_sets','sintaxis.py',6),
  ('statement -> set_numero','statement',1,'p_sets','sintaxis.py',7),
  ('statement -> set_str','statement',1,'p_sets','sintaxis.py',8),
  ('statement -> array_vacio','statement',1,'p_array','sintaxis.py',16),
  ('statement -> array_numero','statement',1,'p_array','sintaxis.py',17),
  ('statement -> array_str','statement',1,'p_array','sintaxis.py',18),
  ('array_vacio -> ID EQUALS LBRACKET RBRACKET','array_vacio',4,'p_array_vacio','sintaxis.py',23),
  ('array_numero -> ID EQUALS LBRACKET varios_numeros RBRACKET','array_numero',5,'p_array_numeros','sintaxis.py',28),
  ('array_str -> ID EQUALS LBRACKET varios_str RBRACKET','array_str',5,'p_array_str','sintaxis.py',33),
  ('set_vacio -> ID EQUALS LCURLYBRACKET RCURLYBRACKET','set_vacio',4,'p_set_vacio','sintaxis.py',40),
  ('set_numero -> ID EQUALS LCURLYBRACKET varios_numeros RCURLYBRACKET','set_numero',5,'p_set_numeros','sintaxis.py',44),
  ('set_str -> ID EQUALS LCURLYBRACKET varios_str RCURLYBRACKET','set_str',5,'p_set_str','sintaxis.py',49),
  ('statement -> hash_vacio','statement',1,'p_hash','sintaxis.py',57),
  ('statement -> hash_elementos','statement',1,'p_hash','sintaxis.py',58),
  ('hash_vacio -> ID EQUALS LCURLYBRACKET RCURLYBRACKET','hash_vacio',4,'p_hash_vacio','sintaxis.py',63),
  ('hash_elementos -> ID EQUALS LCURLYBRACKET varios_pares_hash RCURLYBRACKET','hash_elementos',5,'p_hash_elementos','sintaxis.py',68),
  ('varios_pares_hash -> ID COLON valor','varios_pares_hash',3,'p_varios_pares_hash','sintaxis.py',73),
  ('varios_pares_hash -> STR HASHAS valor','varios_pares_hash',3,'p_varios_pares_hash','sintaxis.py',74),
  ('varios_pares_hash -> ID COLON valor COMMA varios_pares_hash','varios_pares_hash',5,'p_varios_pares_hash','sintaxis.py',75),
  ('varios_pares_hash -> STR HASHAS valor COMMA varios_pares_hash','varios_pares_hash',5,'p_varios_pares_hash','sintaxis.py',76),
  ('statement -> IF comparaciones statement END_LOWER','statement',4,'p_sentencia_if','sintaxis.py',85),
  ('statement -> LOOP DO statement BREAK IF comparacion','statement',6,'p_sentencia_loop','sintaxis.py',92),
  ('statement -> CASE valor when_clauses ELSE statement_list END_LOWER','statement',6,'p_case_when','sintaxis.py',98),
  ('statement -> CASE valor when_clauses ELSE PUTS valor END_LOWER','statement',7,'p_case_when','sintaxis.py',99),
  ('when_clauses -> when_clause','when_clauses',1,'p_when_clauses','sintaxis.py',104),
  ('when_clauses -> when_clauses when_clause','when_clauses',2,'p_when_clauses','sintaxis.py',105),
  ('when_clause -> WHEN valor THEN statement_list','when_clause',4,'p_when_clause','sintaxis.py',110),
  ('when_clause -> WHEN valor PUTS valor','when_clause',4,'p_when_clause','sintaxis.py',111),
  ('statement -> DEF ID LPARENTHESIS RPARENTHESIS statement END_LOWER','statement',6,'p_declaracion_basica','sintaxis.py',120),
  ('statement -> DEF ID LPARENTHESIS argumentos RPARENTHESIS statement END_LOWER','statement',7,'p_declaracion_parametros','sintaxis.py',125),
  ('statement -> DEF ID LPARENTHESIS argumentos RPARENTHESIS statement RETURN valor END_LOWER','statement',9,'p_declaracion_parametros_return','sintaxis.py',130),
  ('varios_str -> STR','varios_str',1,'p_varios_str','sintaxis.py',140),
  ('varios_str -> STR COMMA STR','varios_str',3,'p_varios_str','sintaxis.py',141),
  ('statement -> ID EQUALS valor','statement',3,'p_sentencia_asignacion','sintaxis.py',151),
  ('valor -> numero','valor',1,'p_valor','sintaxis.py',156),
  ('valor -> STR','valor',1,'p_valor','sintaxis.py',157),
  ('valor -> ID','valor',1,'p_valor','sintaxis.py',158),
  ('argumentos -> ID','argumentos',1,'p_argumentos','sintaxis.py',166),
  ('argumentos -> ID COMMA argumentos','argumentos',3,'p_argumentos','sintaxis.py',167),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','sintaxis.py',172),
  ('statement_list -> statement','statement_list',1,'p_statement_list','sintaxis.py',173),
  ('comparador -> EQUAL','comparador',1,'p_comparador','sintaxis.py',178),
  ('comparador -> NOT_EQUAL','comparador',1,'p_comparador','sintaxis.py',179),
  ('comparador -> GREATER_THAN','comparador',1,'p_comparador','sintaxis.py',180),
  ('comparador -> LESS_THAN','comparador',1,'p_comparador','sintaxis.py',181),
  ('comparador -> GREATER_THAN_EQUAL','comparador',1,'p_comparador','sintaxis.py',182),
  ('comparador -> LESS_THAN_EQUAL','comparador',1,'p_comparador','sintaxis.py',183),
  ('comparacion_num -> numero comparador numero','comparacion_num',3,'p_comparacion_num','sintaxis.py',188),
  ('comparacion_variables -> ID EQUAL ID','comparacion_variables',3,'p_comparacion_variables','sintaxis.py',193),
  ('comparacion_variables -> ID NOT_EQUAL ID','comparacion_variables',3,'p_comparacion_variables','sintaxis.py',194),
  ('comparacion -> comparacion_num','comparacion',1,'p_comparacion','sintaxis.py',199),
  ('comparacion -> comparacion_variables','comparacion',1,'p_comparacion','sintaxis.py',200),
  ('comparaciones -> comparacion','comparaciones',1,'p_comparaciones','sintaxis.py',205),
  ('comparaciones -> comparacion conector comparacion','comparaciones',3,'p_comparaciones','sintaxis.py',206),
  ('conector -> OP_AND','conector',1,'p_conector','sintaxis.py',211),
  ('conector -> OP_OR','conector',1,'p_conector','sintaxis.py',212),
  ('numero -> INT','numero',1,'p_numero','sintaxis.py',217),
  ('numero -> FLOAT','numero',1,'p_numero','sintaxis.py',218),
  ('varios_numeros -> numero','varios_numeros',1,'p_varios_numeros','sintaxis.py',223),
  ('varios_numeros -> numero COMMA varios_numeros','varios_numeros',3,'p_varios_numeros','sintaxis.py',224),
]
