
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "COMP DIF ELSE ID IF INT MAIORIGUAL MENORIGUAL NUMBER PRINT PRINTLN READ STRING WHILEPrograma : Declaracoes OperacoesDeclaracoes : Declaracao DeclaracoesDeclaracoes : Declaracao : INT DeclaracaoInt ';'Declaracao : INT DeclaracaoIntDeclaracaoInt : ID '=' ExpDeclaracaoInt : IDDeclaracaoInt : ID '=' READ '(' ')'DeclaracaoInt : ID '[' NUMBER ']'DeclaracaoInt : ID '[' NUMBER ']' '=' ListaDeclaracaoInt : ID '[' NUMBER ']' '[' NUMBER ']'Lista : '{' NUMBER RLista '}'RLista : ',' NUMBER RListaRLista : Operacoes : Operacao OperacoesOperacoes : Operacao : AtribuicaoOperacao : CicloOperacao : CondicionalOperacao : OutputAtribuicao : AtribuicaoInt ';'Atribuicao : AtribuicaoInt AtribuicaoInt : ID '=' ExpAtribuicaoInt : READ '(' ID ')'AtribuicaoInt : ID '[' Exp ']' '=' ExpAtribuicaoInt : READ '(' ID '[' Exp ']' ')'AtribuicaoInt : ID '[' Exp ']' '[' Exp ']' '=' ExpAtribuicaoInt : READ '(' ID '[' Exp ']' '[' Exp ']' ')'Ciclo : WHILE '(' Comparacao ')' '{' Operacoes '}'Condicional : IF '(' Comparacao ')' '{' Operacoes '}'Condicional : IF '(' Comparacao ')' '{' Operacoes '}' ELSE '{' Operacoes '}'Comparacao : Exp Comparador ExpComparador : COMPComparador : '<'Comparador : '>'Comparador : MENORIGUALComparador : MAIORIGUALComparador : DIFOutput : PRINT '(' Exp ')' ';'Output : PRINT '(' STRING ')' ';'Output : PRINTLN '(' Exp ')' ';'Output : PRINTLN '(' STRING ')' ';'Exp : Exp '+' TermoExp : Exp '-' TermoExp : TermoTermo : Termo '*' FatorTermo : Termo '/' FatorTermo : Termo '%' FatorTermo : FatorFator : IDFator : ID '[' Exp ']'Fator : ID '[' Exp ']' '[' Exp ']'Fator : NUMBERFator : '(' Exp ')'"
    
_lr_action_items = {'WHILE':([0,2,3,6,7,8,9,10,11,18,19,20,22,30,36,37,38,39,45,48,72,75,76,77,79,80,81,82,83,85,86,87,88,89,93,97,100,103,105,107,110,111,119,120,121,123,126,128,],[-3,12,-3,12,-17,-18,-19,-20,-22,-2,-5,-7,-21,-4,-45,-49,-50,-53,-23,-6,-24,-9,-54,12,-43,-44,-46,-47,-48,12,-39,-40,-41,-42,-8,-51,-25,-10,-29,-30,-26,-11,-52,12,-27,-12,-28,-31,]),'IF':([0,2,3,6,7,8,9,10,11,18,19,20,22,30,36,37,38,39,45,48,72,75,76,77,79,80,81,82,83,85,86,87,88,89,93,97,100,103,105,107,110,111,119,120,121,123,126,128,],[-3,13,-3,13,-17,-18,-19,-20,-22,-2,-5,-7,-21,-4,-45,-49,-50,-53,-23,-6,-24,-9,-54,13,-43,-44,-46,-47,-48,13,-39,-40,-41,-42,-8,-51,-25,-10,-29,-30,-26,-11,-52,13,-27,-12,-28,-31,]),'PRINT':([0,2,3,6,7,8,9,10,11,18,19,20,22,30,36,37,38,39,45,48,72,75,76,77,79,80,81,82,83,85,86,87,88,89,93,97,100,103,105,107,110,111,119,120,121,123,126,128,],[-3,14,-3,14,-17,-18,-19,-20,-22,-2,-5,-7,-21,-4,-45,-49,-50,-53,-23,-6,-24,-9,-54,14,-43,-44,-46,-47,-48,14,-39,-40,-41,-42,-8,-51,-25,-10,-29,-30,-26,-11,-52,14,-27,-12,-28,-31,]),'PRINTLN':([0,2,3,6,7,8,9,10,11,18,19,20,22,30,36,37,38,39,45,48,72,75,76,77,79,80,81,82,83,85,86,87,88,89,93,97,100,103,105,107,110,111,119,120,121,123,126,128,],[-3,15,-3,15,-17,-18,-19,-20,-22,-2,-5,-7,-21,-4,-45,-49,-50,-53,-23,-6,-24,-9,-54,15,-43,-44,-46,-47,-48,15,-39,-40,-41,-42,-8,-51,-25,-10,-29,-30,-26,-11,-52,15,-27,-12,-28,-31,]),'ID':([0,2,3,4,6,7,8,9,10,11,18,19,20,22,23,24,25,26,27,28,29,30,31,33,36,37,38,39,45,48,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,75,76,77,79,80,81,82,83,85,86,87,88,89,90,91,93,97,100,103,105,106,107,109,110,111,115,119,120,121,123,126,128,],[-3,16,-3,20,16,-17,-18,-19,-20,-22,-2,-5,-7,-21,38,38,38,38,38,38,47,-4,38,38,-45,-49,-50,-53,-23,-6,38,38,38,-33,-34,-35,-36,-37,-38,38,38,38,38,-24,38,-9,-54,16,-43,-44,-46,-47,-48,16,-39,-40,-41,-42,38,38,-8,-51,-25,-10,-29,38,-30,38,-26,-11,38,-52,16,-27,-12,-28,-31,]),'READ':([0,2,3,6,7,8,9,10,11,18,19,20,22,30,31,36,37,38,39,45,48,72,75,76,77,79,80,81,82,83,85,86,87,88,89,93,97,100,103,105,107,110,111,119,120,121,123,126,128,],[-3,17,-3,17,-17,-18,-19,-20,-22,-2,-5,-7,-21,-4,49,-45,-49,-50,-53,-23,-6,-24,-9,-54,17,-43,-44,-46,-47,-48,17,-39,-40,-41,-42,-8,-51,-25,-10,-29,-30,-26,-11,-52,17,-27,-12,-28,-31,]),'$end':([0,1,2,3,5,6,7,8,9,10,11,18,19,20,21,22,30,36,37,38,39,45,48,72,75,76,79,80,81,82,83,86,87,88,89,93,97,100,103,105,107,110,111,119,121,123,126,128,],[-3,0,-16,-3,-1,-16,-17,-18,-19,-20,-22,-2,-5,-7,-15,-21,-4,-45,-49,-50,-53,-23,-6,-24,-9,-54,-43,-44,-46,-47,-48,-39,-40,-41,-42,-8,-51,-25,-10,-29,-30,-26,-11,-52,-27,-12,-28,-31,]),'INT':([0,3,19,20,30,36,37,38,39,48,75,76,79,80,81,82,83,93,97,103,111,119,123,],[4,4,-5,-7,-4,-45,-49,-50,-53,-6,-9,-54,-43,-44,-46,-47,-48,-8,-51,-10,-11,-52,-12,]),'}':([6,7,8,9,10,11,21,22,36,37,38,39,45,72,76,77,79,80,81,82,83,85,86,87,88,89,96,97,98,100,105,107,110,112,117,119,120,121,124,125,126,127,128,],[-16,-17,-18,-19,-20,-22,-15,-21,-45,-49,-50,-53,-23,-24,-54,-16,-43,-44,-46,-47,-48,-16,-39,-40,-41,-42,105,-51,107,-25,-29,-30,-26,-14,123,-52,-16,-27,-14,128,-28,-13,-31,]),';':([11,19,20,36,37,38,39,45,48,67,68,69,70,72,75,76,79,80,81,82,83,93,97,100,103,110,111,119,121,123,126,],[22,30,-7,-45,-49,-50,-53,-23,-6,86,87,88,89,-24,-9,-54,-43,-44,-46,-47,-48,-8,-51,-25,-10,-26,-11,-52,-27,-12,-28,]),'(':([12,13,14,15,17,23,24,25,26,27,28,31,33,49,53,54,55,56,57,58,59,60,61,62,63,64,65,73,90,91,106,109,115,],[23,24,25,26,29,33,33,33,33,33,33,33,33,74,33,33,33,-33,-34,-35,-36,-37,-38,33,33,33,33,33,33,33,33,33,33,]),'=':([16,20,71,75,108,],[27,31,91,95,115,]),'[':([16,20,38,47,71,75,97,101,],[28,32,65,73,90,94,106,109,]),'NUMBER':([23,24,25,26,27,28,31,32,33,53,54,55,56,57,58,59,60,61,62,63,64,65,73,90,91,94,104,106,109,115,118,],[39,39,39,39,39,39,39,50,39,39,39,39,-33,-34,-35,-36,-37,-38,39,39,39,39,39,39,39,102,112,39,39,39,124,]),'STRING':([25,26,],[42,44,]),')':([34,36,37,38,39,40,41,42,43,44,47,51,74,76,78,79,80,81,82,83,97,101,119,122,],[52,-45,-49,-50,-53,66,67,68,69,70,72,76,93,-54,-32,-43,-44,-46,-47,-48,-51,110,-52,126,]),'+':([35,36,37,38,39,41,43,45,46,48,51,76,78,79,80,81,82,83,84,92,97,99,100,113,116,119,121,],[54,-45,-49,-50,-53,54,54,54,54,54,54,-54,54,-43,-44,-46,-47,-48,54,54,-51,54,54,54,54,-52,54,]),'-':([35,36,37,38,39,41,43,45,46,48,51,76,78,79,80,81,82,83,84,92,97,99,100,113,116,119,121,],[55,-45,-49,-50,-53,55,55,55,55,55,55,-54,55,-43,-44,-46,-47,-48,55,55,-51,55,55,55,55,-52,55,]),'COMP':([35,36,37,38,39,76,79,80,81,82,83,97,119,],[56,-45,-49,-50,-53,-54,-43,-44,-46,-47,-48,-51,-52,]),'<':([35,36,37,38,39,76,79,80,81,82,83,97,119,],[57,-45,-49,-50,-53,-54,-43,-44,-46,-47,-48,-51,-52,]),'>':([35,36,37,38,39,76,79,80,81,82,83,97,119,],[58,-45,-49,-50,-53,-54,-43,-44,-46,-47,-48,-51,-52,]),'MENORIGUAL':([35,36,37,38,39,76,79,80,81,82,83,97,119,],[59,-45,-49,-50,-53,-54,-43,-44,-46,-47,-48,-51,-52,]),'MAIORIGUAL':([35,36,37,38,39,76,79,80,81,82,83,97,119,],[60,-45,-49,-50,-53,-54,-43,-44,-46,-47,-48,-51,-52,]),'DIF':([35,36,37,38,39,76,79,80,81,82,83,97,119,],[61,-45,-49,-50,-53,-54,-43,-44,-46,-47,-48,-51,-52,]),']':([36,37,38,39,46,50,76,79,80,81,82,83,84,92,97,99,102,113,116,119,],[-45,-49,-50,-53,71,75,-54,-43,-44,-46,-47,-48,97,101,-51,108,111,119,122,-52,]),'*':([36,37,38,39,76,79,80,81,82,83,97,119,],[62,-49,-50,-53,-54,62,62,-46,-47,-48,-51,-52,]),'/':([36,37,38,39,76,79,80,81,82,83,97,119,],[63,-49,-50,-53,-54,63,63,-46,-47,-48,-51,-52,]),'%':([36,37,38,39,76,79,80,81,82,83,97,119,],[64,-49,-50,-53,-54,64,64,-46,-47,-48,-51,-52,]),'{':([52,66,95,114,],[77,85,104,120,]),'ELSE':([107,],[114,]),',':([112,124,],[118,118,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Declaracoes':([0,3,],[2,18,]),'Declaracao':([0,3,],[3,3,]),'Operacoes':([2,6,77,85,120,],[5,21,96,98,125,]),'Operacao':([2,6,77,85,120,],[6,6,6,6,6,]),'Atribuicao':([2,6,77,85,120,],[7,7,7,7,7,]),'Ciclo':([2,6,77,85,120,],[8,8,8,8,8,]),'Condicional':([2,6,77,85,120,],[9,9,9,9,9,]),'Output':([2,6,77,85,120,],[10,10,10,10,10,]),'AtribuicaoInt':([2,6,77,85,120,],[11,11,11,11,11,]),'DeclaracaoInt':([4,],[19,]),'Comparacao':([23,24,],[34,40,]),'Exp':([23,24,25,26,27,28,31,33,53,65,73,90,91,106,109,115,],[35,35,41,43,45,46,48,51,78,84,92,99,100,113,116,121,]),'Termo':([23,24,25,26,27,28,31,33,53,54,55,65,73,90,91,106,109,115,],[36,36,36,36,36,36,36,36,36,79,80,36,36,36,36,36,36,36,]),'Fator':([23,24,25,26,27,28,31,33,53,54,55,62,63,64,65,73,90,91,106,109,115,],[37,37,37,37,37,37,37,37,37,37,37,81,82,83,37,37,37,37,37,37,37,]),'Comparador':([35,],[53,]),'Lista':([95,],[103,]),'RLista':([112,124,],[117,127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Declaracoes Operacoes','Programa',2,'p_Programa','compilador.py',14),
  ('Declaracoes -> Declaracao Declaracoes','Declaracoes',2,'p_Declaracoes_Declaracao','compilador.py',24),
  ('Declaracoes -> <empty>','Declaracoes',0,'p_Declaracoes_Vazio','compilador.py',28),
  ('Declaracao -> INT DeclaracaoInt ;','Declaracao',3,'p_Declaracao','compilador.py',33),
  ('Declaracao -> INT DeclaracaoInt','Declaracao',2,'p_Declaracao_error','compilador.py',37),
  ('DeclaracaoInt -> ID = Exp','DeclaracaoInt',3,'p_DeclaracaoInt_Exp','compilador.py',43),
  ('DeclaracaoInt -> ID','DeclaracaoInt',1,'p_DeclaracaoInt_ID','compilador.py',49),
  ('DeclaracaoInt -> ID = READ ( )','DeclaracaoInt',5,'p_DeclaracaoInt_READ','compilador.py',55),
  ('DeclaracaoInt -> ID [ NUMBER ]','DeclaracaoInt',4,'p_DeclaracaoInt_ArrayVazio','compilador.py',61),
  ('DeclaracaoInt -> ID [ NUMBER ] = Lista','DeclaracaoInt',6,'p_DeclaracaoInt_ArrayLista','compilador.py',67),
  ('DeclaracaoInt -> ID [ NUMBER ] [ NUMBER ]','DeclaracaoInt',7,'p_DeclaracaoInt_Array_2Dim_Vazio','compilador.py',80),
  ('Lista -> { NUMBER RLista }','Lista',4,'p_Lista','compilador.py',88),
  ('RLista -> , NUMBER RLista','RLista',3,'p_RLista','compilador.py',93),
  ('RLista -> <empty>','RLista',0,'p_RLista_Vazio','compilador.py',98),
  ('Operacoes -> Operacao Operacoes','Operacoes',2,'p_Operacoes_Op','compilador.py',103),
  ('Operacoes -> <empty>','Operacoes',0,'p_Operacoes_vazio','compilador.py',107),
  ('Operacao -> Atribuicao','Operacao',1,'p_Operacao_Atribuicao','compilador.py',111),
  ('Operacao -> Ciclo','Operacao',1,'p_Operacao_Ciclo','compilador.py',115),
  ('Operacao -> Condicional','Operacao',1,'p_Operacao_Condicional','compilador.py',119),
  ('Operacao -> Output','Operacao',1,'p_Operacao_Output','compilador.py',123),
  ('Atribuicao -> AtribuicaoInt ;','Atribuicao',2,'p_Atribuicao','compilador.py',127),
  ('Atribuicao -> AtribuicaoInt','Atribuicao',1,'p_Atribuicao_error','compilador.py',131),
  ('AtribuicaoInt -> ID = Exp','AtribuicaoInt',3,'p_AtribuicaoInt_Exp','compilador.py',137),
  ('AtribuicaoInt -> READ ( ID )','AtribuicaoInt',4,'p_AtribuicaoInt_READ','compilador.py',152),
  ('AtribuicaoInt -> ID [ Exp ] = Exp','AtribuicaoInt',6,'p_AtribuicaoInt_Array','compilador.py',167),
  ('AtribuicaoInt -> READ ( ID [ Exp ] )','AtribuicaoInt',7,'p_AtribuicaoInt_Array_READ','compilador.py',183),
  ('AtribuicaoInt -> ID [ Exp ] [ Exp ] = Exp','AtribuicaoInt',9,'p_AtribuicaoInt_Array_2Dim','compilador.py',198),
  ('AtribuicaoInt -> READ ( ID [ Exp ] [ Exp ] )','AtribuicaoInt',10,'p_AtribuicaoInt_Array_2Dim_READ','compilador.py',215),
  ('Ciclo -> WHILE ( Comparacao ) { Operacoes }','Ciclo',7,'p_Ciclo','compilador.py',231),
  ('Condicional -> IF ( Comparacao ) { Operacoes }','Condicional',7,'p_Condicional','compilador.py',238),
  ('Condicional -> IF ( Comparacao ) { Operacoes } ELSE { Operacoes }','Condicional',11,'p_Condicional_Else','compilador.py',244),
  ('Comparacao -> Exp Comparador Exp','Comparacao',3,'p_Comparacao','compilador.py',251),
  ('Comparador -> COMP','Comparador',1,'p_Comparador_equal','compilador.py',255),
  ('Comparador -> <','Comparador',1,'p_Comparador_inf','compilador.py',259),
  ('Comparador -> >','Comparador',1,'p_Comparador_sup','compilador.py',263),
  ('Comparador -> MENORIGUAL','Comparador',1,'p_Comparador_infeq','compilador.py',267),
  ('Comparador -> MAIORIGUAL','Comparador',1,'p_Comparador_supeq','compilador.py',271),
  ('Comparador -> DIF','Comparador',1,'p_Comparador_dif','compilador.py',275),
  ('Output -> PRINT ( Exp ) ;','Output',5,'p_Output_PRINT_Exp','compilador.py',279),
  ('Output -> PRINT ( STRING ) ;','Output',5,'p_Output_PRINT_STRING','compilador.py',283),
  ('Output -> PRINTLN ( Exp ) ;','Output',5,'p_Output_PRINTLN_Exp','compilador.py',287),
  ('Output -> PRINTLN ( STRING ) ;','Output',5,'p_Output_PRINTLN_STRING','compilador.py',291),
  ('Exp -> Exp + Termo','Exp',3,'p_Exp_add','compilador.py',295),
  ('Exp -> Exp - Termo','Exp',3,'p_Exp_sub','compilador.py',299),
  ('Exp -> Termo','Exp',1,'p_Exp_term','compilador.py',303),
  ('Termo -> Termo * Fator','Termo',3,'p_Termo_mul','compilador.py',307),
  ('Termo -> Termo / Fator','Termo',3,'p_Termo_div','compilador.py',311),
  ('Termo -> Termo % Fator','Termo',3,'p_Termo_mod','compilador.py',315),
  ('Termo -> Fator','Termo',1,'p_Termo_fator','compilador.py',319),
  ('Fator -> ID','Fator',1,'p_Factor_id','compilador.py',323),
  ('Fator -> ID [ Exp ]','Fator',4,'p_Fator_arrayvalue','compilador.py',339),
  ('Fator -> ID [ Exp ] [ Exp ]','Fator',7,'p_Fator_array_2Dim_value','compilador.py',354),
  ('Fator -> NUMBER','Fator',1,'p_Fator_number','compilador.py',370),
  ('Fator -> ( Exp )','Fator',3,'p_Fator_group','compilador.py',374),
]
