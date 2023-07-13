
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ARRAY AT BEGIN BITWISE_AND BITWISE_NOT BITWISE_OR BITWISE_XOR BREAK CASE CLASS COLON COMMA COMPLEX CONSTANT DEDENT DEF DEFINED DIVIDE DO DOT DOUBLYAT EACH ELSE ELSEIF END_LOWER END_UPPER ENSURE EQUAL EQUALS EXPONENT FALSE FILE FLOAT FOR GLOBAL GREATER_THAN GREATER_THAN_EQUAL HASH HASHAS HASHTAG ID IF IN INDENT INT LBRACKET LCURLYBRACKET LESS_THAN LESS_THAN_EQUAL LINE LOOP LPARENTHESIS MINUS MODULE MODULO MULTIPLY NEWLINE NEXT NIL NOT NOT_EQUAL OP_AND OP_NOT OP_OR OR PLUS PRINT PUTS RATIONAL RBRACKET RCURLYBRACKET REDO RESCUE RETRY RETURN RPARENTHESIS Rational SELF SEMICOLON SET SHIFT_LEFT SHIFT_RIGHT STR SUPER SYMBOL THEN TRUE UNDEF UNLESS UNTIL WHEN WHILE YIELDstatement : expressionexpression : ID EQUALS expressionexpression : AT ID EQUALS expressionexpression : GLOBAL ID EQUALS expressionexpression : ID EQUALS Rational LPARENTHESIS INT COMMA INT RPARENTHESIS\n    expression : expression PLUS expression\n    | expression MINUS expression\n    | expression MULTIPLY expression\n    | expression DIVIDE expression\n    \n    statement : set_vacio\n    | set_elementos\n    \n    set_vacio : ID EQUALS SET LCURLYBRACKET RCURLYBRACKET\n    \n    set_elementos : ID EQUALS SET LCURLYBRACKET varios_set_elementos RCURLYBRACKET\n    \n    varios_set_elementos : INT\n    | STR\n    | FLOAT\n    | INT COMMA varios_set_elementos\n    | FLOAT COMMA varios_set_elementos\n    | STR COMMA varios_set_elementos \n    \n    statement : array\n    \n    array : ID EQUALS LBRACKET RBRACKET\n    array : ID EQUALS LBRACKET string_lista RBRACKET\n    string_lista : STR\n    | STR COMMA string_lista\n    array : ID EQUALS LBRACKET int_lista RBRACKET\n    int_lista : INT\n    | INT COMMA int_lista\n    \n    statement : hash_vacio\n    | hash_elementos\n    \n    hash_vacio : ID EQUALS LCURLYBRACKET RCURLYBRACKET\n    \n    hash_elementos : ID EQUALS LCURLYBRACKET varios_pares_hash RCURLYBRACKET\n    \n    varios_pares_hash : ID COLON expression\n    | STR HASHAS expression\n    | ID COLON expression COMMA varios_pares_hash\n    | STR HASHAS expression COMMA varios_pares_hash\n    expression : INTexpression : FLOATexpression : STRexpression : TRUE\n                  | FALSEexpression : COLON IDexpression : ID\n    statement : PUTS STR\n    | PRINT STR\n    \n    statement : PUTS INT\n    | PRINT INT\n    \n    statement : PUTS FLOAT\n    | PRINT FLOAT\n    \n    statement : PUTS ID\n    | PRINT ID\n    statement : DEF ID LPARENTHESIS parameters RPARENTHESIS LCURLYBRACKET statements RCURLYBRACKETparameters : ID\n                  | parameters COMMA IDstatements : statement\n                  | statements COMMA statement'
    
_lr_action_items = {'PUTS':([0,90,104,],[8,8,8,]),'PRINT':([0,90,104,],[10,10,10,]),'DEF':([0,90,104,],[14,14,14,]),'ID':([0,8,10,14,15,16,19,20,21,22,23,32,45,47,48,49,50,72,74,80,90,96,97,104,],[13,27,31,33,34,35,36,38,38,38,38,38,53,62,38,38,38,38,38,91,13,53,53,13,]),'AT':([0,20,21,22,23,32,48,49,50,72,74,90,104,],[15,15,15,15,15,15,15,15,15,15,15,15,15,]),'GLOBAL':([0,20,21,22,23,32,48,49,50,72,74,90,104,],[16,16,16,16,16,16,16,16,16,16,16,16,16,]),'INT':([0,8,10,20,21,22,23,32,46,48,49,50,51,52,72,74,78,81,83,84,85,90,104,],[11,25,29,11,11,11,11,11,61,11,11,11,66,69,11,11,61,92,69,69,69,11,11,]),'FLOAT':([0,8,10,20,21,22,23,32,48,49,50,52,72,74,83,84,85,90,104,],[12,26,30,12,12,12,12,12,12,12,12,71,12,12,71,71,71,12,12,]),'STR':([0,8,10,20,21,22,23,32,45,46,48,49,50,52,72,74,77,83,84,85,90,96,97,104,],[9,24,28,9,9,9,9,9,56,60,9,9,9,70,9,9,60,70,70,70,9,56,56,9,]),'TRUE':([0,20,21,22,23,32,48,49,50,72,74,90,104,],[17,17,17,17,17,17,17,17,17,17,17,17,17,]),'FALSE':([0,20,21,22,23,32,48,49,50,72,74,90,104,],[18,18,18,18,18,18,18,18,18,18,18,18,18,]),'COLON':([0,20,21,22,23,32,48,49,50,53,72,74,90,104,],[19,19,19,19,19,19,19,19,19,72,19,19,19,19,]),'$end':([1,2,3,4,5,6,7,9,11,12,13,17,18,24,25,26,27,28,29,30,31,36,37,38,39,40,41,42,54,57,64,65,67,73,75,76,82,100,103,],[0,-1,-10,-11,-20,-28,-29,-38,-36,-37,-42,-39,-40,-43,-45,-47,-49,-44,-46,-48,-50,-41,-6,-42,-7,-8,-9,-2,-30,-21,-3,-4,-12,-31,-22,-25,-13,-5,-51,]),'RCURLYBRACKET':([2,3,4,5,6,7,9,11,12,13,17,18,24,25,26,27,28,29,30,31,36,37,38,39,40,41,42,45,52,54,55,57,64,65,67,68,69,70,71,73,75,76,82,86,87,93,94,95,98,99,100,101,102,103,105,],[-1,-10,-11,-20,-28,-29,-38,-36,-37,-42,-39,-40,-43,-45,-47,-49,-44,-46,-48,-50,-41,-6,-42,-7,-8,-9,-2,54,67,-30,73,-21,-3,-4,-12,82,-14,-15,-16,-31,-22,-25,-13,-32,-33,-17,-19,-18,103,-54,-5,-34,-35,-51,-55,]),'COMMA':([2,3,4,5,6,7,9,11,12,13,17,18,24,25,26,27,28,29,30,31,36,37,38,39,40,41,42,54,57,60,61,62,63,64,65,66,67,69,70,71,73,75,76,82,86,87,91,98,99,100,103,105,],[-1,-10,-11,-20,-28,-29,-38,-36,-37,-42,-39,-40,-43,-45,-47,-49,-44,-46,-48,-50,-41,-6,-42,-7,-8,-9,-2,-30,-21,77,78,-52,80,-3,-4,81,-12,83,84,85,-31,-22,-25,-13,96,97,-53,104,-54,-5,-51,-55,]),'PLUS':([2,9,11,12,13,17,18,36,37,38,39,40,41,42,64,65,86,87,100,],[20,-38,-36,-37,-42,-39,-40,-41,20,-42,20,20,20,20,20,20,20,20,-5,]),'MINUS':([2,9,11,12,13,17,18,36,37,38,39,40,41,42,64,65,86,87,100,],[21,-38,-36,-37,-42,-39,-40,-41,21,-42,21,21,21,21,21,21,21,21,-5,]),'MULTIPLY':([2,9,11,12,13,17,18,36,37,38,39,40,41,42,64,65,86,87,100,],[22,-38,-36,-37,-42,-39,-40,-41,22,-42,22,22,22,22,22,22,22,22,-5,]),'DIVIDE':([2,9,11,12,13,17,18,36,37,38,39,40,41,42,64,65,86,87,100,],[23,-38,-36,-37,-42,-39,-40,-41,23,-42,23,23,23,23,23,23,23,23,-5,]),'EQUALS':([13,34,35,38,],[32,48,49,50,]),'Rational':([32,50,],[43,43,]),'SET':([32,],[44,]),'LBRACKET':([32,],[46,]),'LCURLYBRACKET':([32,44,79,],[45,52,90,]),'LPARENTHESIS':([33,43,],[47,51,]),'RBRACKET':([46,58,59,60,61,88,89,],[57,75,76,-23,-26,-24,-27,]),'HASHAS':([56,],[74,]),'RPARENTHESIS':([62,63,91,92,],[-52,79,-53,100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,90,104,],[1,99,105,]),'expression':([0,20,21,22,23,32,48,49,50,72,74,90,104,],[2,37,39,40,41,42,64,65,42,86,87,2,2,]),'set_vacio':([0,90,104,],[3,3,3,]),'set_elementos':([0,90,104,],[4,4,4,]),'array':([0,90,104,],[5,5,5,]),'hash_vacio':([0,90,104,],[6,6,6,]),'hash_elementos':([0,90,104,],[7,7,7,]),'varios_pares_hash':([45,96,97,],[55,101,102,]),'string_lista':([46,77,],[58,88,]),'int_lista':([46,78,],[59,89,]),'parameters':([47,],[63,]),'varios_set_elementos':([52,83,84,85,],[68,93,94,95,]),'statements':([90,],[98,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expression','analizer_ruby.py',12),
  ('expression -> ID EQUALS expression','expression',3,'p_expression_assignment','analizer_ruby.py',19),
  ('expression -> AT ID EQUALS expression','expression',4,'p_expression_assignment_instance','analizer_ruby.py',36),
  ('expression -> GLOBAL ID EQUALS expression','expression',4,'p_expression_assignment_global','analizer_ruby.py',45),
  ('expression -> ID EQUALS Rational LPARENTHESIS INT COMMA INT RPARENTHESIS','expression',8,'p_expression_assignment_rational','analizer_ruby.py',54),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binary_operation','analizer_ruby.py',64),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binary_operation','analizer_ruby.py',65),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binary_operation','analizer_ruby.py',66),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binary_operation','analizer_ruby.py',67),
  ('statement -> set_vacio','statement',1,'p_set','analizer_ruby.py',89),
  ('statement -> set_elementos','statement',1,'p_set','analizer_ruby.py',90),
  ('set_vacio -> ID EQUALS SET LCURLYBRACKET RCURLYBRACKET','set_vacio',5,'p_set_vacio','analizer_ruby.py',95),
  ('set_elementos -> ID EQUALS SET LCURLYBRACKET varios_set_elementos RCURLYBRACKET','set_elementos',6,'p_set_elementos','analizer_ruby.py',105),
  ('varios_set_elementos -> INT','varios_set_elementos',1,'p_varios_set_elementos','analizer_ruby.py',116),
  ('varios_set_elementos -> STR','varios_set_elementos',1,'p_varios_set_elementos','analizer_ruby.py',117),
  ('varios_set_elementos -> FLOAT','varios_set_elementos',1,'p_varios_set_elementos','analizer_ruby.py',118),
  ('varios_set_elementos -> INT COMMA varios_set_elementos','varios_set_elementos',3,'p_varios_set_elementos','analizer_ruby.py',119),
  ('varios_set_elementos -> FLOAT COMMA varios_set_elementos','varios_set_elementos',3,'p_varios_set_elementos','analizer_ruby.py',120),
  ('varios_set_elementos -> STR COMMA varios_set_elementos','varios_set_elementos',3,'p_varios_set_elementos','analizer_ruby.py',121),
  ('statement -> array','statement',1,'p_array','analizer_ruby.py',131),
  ('array -> ID EQUALS LBRACKET RBRACKET','array',4,'p_array_vacio','analizer_ruby.py',137),
  ('array -> ID EQUALS LBRACKET string_lista RBRACKET','array',5,'p_string_array','analizer_ruby.py',147),
  ('string_lista -> STR','string_lista',1,'p_string_lista','analizer_ruby.py',158),
  ('string_lista -> STR COMMA string_lista','string_lista',3,'p_string_lista','analizer_ruby.py',159),
  ('array -> ID EQUALS LBRACKET int_lista RBRACKET','array',5,'p_int_array','analizer_ruby.py',169),
  ('int_lista -> INT','int_lista',1,'p_int_lista','analizer_ruby.py',180),
  ('int_lista -> INT COMMA int_lista','int_lista',3,'p_int_lista','analizer_ruby.py',181),
  ('statement -> hash_vacio','statement',1,'p_hash','analizer_ruby.py',192),
  ('statement -> hash_elementos','statement',1,'p_hash','analizer_ruby.py',193),
  ('hash_vacio -> ID EQUALS LCURLYBRACKET RCURLYBRACKET','hash_vacio',4,'p_hash_vacio','analizer_ruby.py',199),
  ('hash_elementos -> ID EQUALS LCURLYBRACKET varios_pares_hash RCURLYBRACKET','hash_elementos',5,'p_hash_elementos','analizer_ruby.py',212),
  ('varios_pares_hash -> ID COLON expression','varios_pares_hash',3,'p_varios_pares_hash','analizer_ruby.py',226),
  ('varios_pares_hash -> STR HASHAS expression','varios_pares_hash',3,'p_varios_pares_hash','analizer_ruby.py',227),
  ('varios_pares_hash -> ID COLON expression COMMA varios_pares_hash','varios_pares_hash',5,'p_varios_pares_hash','analizer_ruby.py',228),
  ('varios_pares_hash -> STR HASHAS expression COMMA varios_pares_hash','varios_pares_hash',5,'p_varios_pares_hash','analizer_ruby.py',229),
  ('expression -> INT','expression',1,'p_expression_int','analizer_ruby.py',244),
  ('expression -> FLOAT','expression',1,'p_expression_float','analizer_ruby.py',249),
  ('expression -> STR','expression',1,'p_expression_string','analizer_ruby.py',253),
  ('expression -> TRUE','expression',1,'p_expression_boolean','analizer_ruby.py',257),
  ('expression -> FALSE','expression',1,'p_expression_boolean','analizer_ruby.py',258),
  ('expression -> COLON ID','expression',2,'p_expression_symbol','analizer_ruby.py',264),
  ('expression -> ID','expression',1,'p_expression_id','analizer_ruby.py',271),
  ('statement -> PUTS STR','statement',2,'p_print_str','analizer_ruby.py',282),
  ('statement -> PRINT STR','statement',2,'p_print_str','analizer_ruby.py',283),
  ('statement -> PUTS INT','statement',2,'p_print_int','analizer_ruby.py',291),
  ('statement -> PRINT INT','statement',2,'p_print_int','analizer_ruby.py',292),
  ('statement -> PUTS FLOAT','statement',2,'p_print_float','analizer_ruby.py',298),
  ('statement -> PRINT FLOAT','statement',2,'p_print_float','analizer_ruby.py',299),
  ('statement -> PUTS ID','statement',2,'p_print_id','analizer_ruby.py',305),
  ('statement -> PRINT ID','statement',2,'p_print_id','analizer_ruby.py',306),
  ('statement -> DEF ID LPARENTHESIS parameters RPARENTHESIS LCURLYBRACKET statements RCURLYBRACKET','statement',8,'p_function_declaration','analizer_ruby.py',319),
  ('parameters -> ID','parameters',1,'p_parameters','analizer_ruby.py',330),
  ('parameters -> parameters COMMA ID','parameters',3,'p_parameters','analizer_ruby.py',331),
  ('statements -> statement','statements',1,'p_statements','analizer_ruby.py',339),
  ('statements -> statements COMMA statement','statements',3,'p_statements','analizer_ruby.py',340),
]
