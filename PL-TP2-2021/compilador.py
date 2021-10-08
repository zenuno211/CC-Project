import sys
import ply.yacc as yacc
import ply.lex as lex

from comp_lex import tokens



#Tabela de identificadores
#id - tipo - endereço - tamanho


def p_Programa(p):
    "Programa : Declaracoes Operacoes"
    p[0] = p[1] + "\nstart\n" + p[2] + "stop"
    if p.parser.success:
        print("Compilação bem sucedida")
        outFile.write(p[0])
    else:
        outFile.write("err \"Erro de compilação\"\n")
        handle_error(p)

def p_Declaracoes_Declaracao(p):
    "Declaracoes : Declaracao Declaracoes"
    p[0] = p[1] + p[2]

def p_Declaracoes_Vazio(p):
    "Declaracoes : "
    p[0] = ""


def p_Declaracao(p):
    "Declaracao : INT DeclaracaoInt ';'"
    p[0] = p[2]

def p_Declaracao_error(p):
    "Declaracao : INT DeclaracaoInt"
    p[0] = ""
    p.parser.success = False
    p.parser.errors.append(" ';' em falta em declaração")

def p_DeclaracaoInt_Exp(p):
    "DeclaracaoInt : ID '=' Exp"
    p[0] = p[3]
    p.parser.tab_ids[p[1]] = ('int',p.parser.contador_vars, None, None)
    p.parser.contador_vars += 1

def p_DeclaracaoInt_ID(p):
    "DeclaracaoInt : ID"
    p[0] = "pushi 0\n"
    p.parser.tab_ids[p[1]] = ('int',p.parser.contador_vars, None, None)
    p.parser.contador_vars += 1

def p_DeclaracaoInt_READ(p):
    "DeclaracaoInt : ID '=' READ '(' ')'"
    p[0] = "read\natoi\n"
    p.parser.tab_ids[p[1]] = ('int',p.parser.contador_vars, None, None)
    p.parser.contador_vars += 1

def p_DeclaracaoInt_ArrayVazio(p):
    "DeclaracaoInt : ID '[' NUMBER ']'"
    p[0] = "pushn " + p[3] + '\n'
    p.parser.tab_ids[p[1]] = ('int_array',p.parser.contador_vars, int(p[3]), None)
    p.parser.contador_vars += int(p[3])

def p_DeclaracaoInt_ArrayLista(p):
    "DeclaracaoInt : ID '[' NUMBER ']' '=' Lista"
    if(p.parser.contador_aux_arrays == int(p[3])):
        p[0] = p[6]
        p.parser.tab_ids[p[1]] = ('int_array',p.parser.contador_vars, int(p[3]), None)
        p.parser.contador_vars += int(p[3])
        p.contador_aux_arrays = 0
    else:
        parser.success = False
        p.parser.errors.append("Declaração do array " + p[1] + " com número errado de elementos")
        p[0] = ""


def p_DeclaracaoInt_Array_2Dim_Vazio(p):
    "DeclaracaoInt : ID '[' NUMBER ']' '[' NUMBER ']'"
    size = int(p[3]) * int(p[6])
    p[0] = "pushn " + str(size) + '\n'
    p.parser.tab_ids[p[1]] = ('int_biarray',p.parser.contador_vars, int(p[3]), int(p[6]))
    p.parser.contador_vars += size


def p_Lista(p):
    "Lista : '{' NUMBER RLista '}'"
    p.parser.contador_aux_arrays  += 1
    p[0] = "pushi " + p[2] + "\n" + p[3]

def p_RLista(p):
    "RLista : ',' NUMBER RLista"
    p.parser.contador_aux_arrays += 1
    p[0] = "pushi " + p[2] + "\n" + p[3]

def p_RLista_Vazio(p):
    "RLista : "
    p[0] = ""


def p_Operacoes_Op(p):
    "Operacoes : Operacao Operacoes"
    p[0] = p[1] + p[2]

def p_Operacoes_vazio(p):
    "Operacoes : "
    p[0] = ""

def p_Operacao_Atribuicao(p):
    "Operacao : Atribuicao"
    p[0] = p[1]

def p_Operacao_Ciclo(p):
    "Operacao : Ciclo"
    p[0] = p[1]

def p_Operacao_Condicional(p):
    "Operacao : Condicional"
    p[0] = p[1]

def p_Operacao_Output(p):
    "Operacao : Output"
    p[0] = p[1]
 
def p_Atribuicao(p):
    "Atribuicao : AtribuicaoInt ';'"
    p[0] = p[1]

def p_Atribuicao_error(p):
    "Atribuicao : AtribuicaoInt "
    p[0] = ""
    p.parser.success = False
    p.parser.errors.append(" ';' em falta em declaração")

def p_AtribuicaoInt_Exp(p):
    "AtribuicaoInt : ID '=' Exp"
    if(p[1] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[1]][0] == 'int'):
            address = p.parser.tab_ids[p[1]][1]
            p[0] = p[3] + "storeg " + str(address) + "\n"
        else:
            p.parser.errors.append("Variável " + p[1] + " não é do tipo esperado (int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[3] + " não declarada")
        p.parser.success = False
        p[0] = ""

def p_AtribuicaoInt_READ(p):
    "AtribuicaoInt : READ '(' ID ')'"
    if(p[3] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[3]][0] == 'int'):
            address = p.parser.tab_ids[p[3]][1]
            p[0] = "read \natoi \n" + "storeg " + str(address) + "\n"
        else:
            p.parser.errors.append("Variável " + p[3] + " não é do tipo esperado (int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[3] + " não declarada")
        p.parser.success = False
        p[0] = ""

def p_AtribuicaoInt_Array(p):
    "AtribuicaoInt : ID '[' Exp ']' '=' Exp"
    if(p[1] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[1]][0] == 'int_array'):
            address = p.parser.tab_ids[p[1]][1]
            p[0] = "pushgp\npushi " + str(address) + "\npadd\n"+ p[3] +  p[6] + "storen\n"
        else:
            p.parser.errors.append("Variável " + p[1] + " não é do tipo esperado (array de int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[1] + " não declarada")
        p.parser.success = False
        p[0] = ""


def p_AtribuicaoInt_Array_READ(p):
    "AtribuicaoInt : READ '(' ID '[' Exp ']' ')'"
    if(p[3] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[3]][0] == 'int_array'):
            address = p.parser.tab_ids[p[3]][1]
            p[0] = "pushgp\npushi " + str(address) + "\npadd\n"+ p[5] +  "read \natoi \n" + "storen\n"
        else:
            p.parser.errors.append("Variável " + p[3] + " não é do tipo esperado (array de int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[3] + " não declarada")
        p.parser.success = False
        p[0] = ""

def p_AtribuicaoInt_Array_2Dim(p):
    "AtribuicaoInt : ID '[' Exp ']' '[' Exp ']' '=' Exp"
    if(p[1] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[1]][0] == 'int_biarray'):
            address = p.parser.tab_ids[p[1]][1]
            offset = p[3] + "pushi " + str(p.parser.tab_ids[p[1]][3]) + "\nmul\n" + p[6] + "add\n"
            p[0] = "pushgp\npushi " + str(address) + "\npadd\n"+ offset +  p[9] + "storen\n"
        else:
            p.parser.errors.append("Variável " + p[1] + " não é do tipo esperado (array bidimensional de int)")
            p.parser.success = False
            p[0] = ""
        
    else:
        p.parser.errors.append("Variável " + p[1] + " não declarada")
        p.parser.success = False
        p[0] = ""

def p_AtribuicaoInt_Array_2Dim_READ(p):
    "AtribuicaoInt : READ '(' ID '[' Exp ']' '[' Exp ']' ')'"
    if(p[3] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[3]][0] == 'int_biarray'):
            address = p.parser.tab_ids[p[3]][1]
            offset = p[5] + "pushi " + str(p.parser.tab_ids[p[3]][3]) + "\nmul\n" + p[8] + "add\n"
            p[0] = "pushgp\npushi " + str(address) + "\npadd\n"+ offset + "read \natoi \n" + "storen\n"
        else:
            p.parser.errors.append("Variável " + p[3] + " não é do tipo esperado (array bidimensional de int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[3] + " não declarada")
        p.parser.success = False
        p[0] = ""

def p_Ciclo(p):
    "Ciclo : WHILE '(' Comparacao ')' '{' Operacoes '}'"
    labelInic = "while" + str(p.parser.contador_ciclos) + ""
    labelEnd= "while" + str(p.parser.contador_ciclos) + "end"
    p[0] = "\n" + labelInic + ":\n" + p[3] + "jz " + labelEnd + "\n\n" + p[6] + "jump " + labelInic + "\n\n" + labelEnd + ":\n"
    p.parser.contador_ciclos += 1

def p_Condicional(p):
    "Condicional : IF '(' Comparacao ')' '{' Operacoes '}'"
    labelEnd= "if" + str(p.parser.contador_condicional) + "end"
    p[0] = p[3] + "jz " + labelEnd + "\n\n" + p[6] +  labelEnd + ":\n"
    p.parser.contador_condicional += 1

def p_Condicional_Else(p):
    "Condicional : IF '(' Comparacao ')' '{' Operacoes '}' ELSE '{' Operacoes '}'"
    labelEnd= "if" + str(p.parser.contador_condicional) + "end"
    elseEnd= "else" + str(p.parser.contador_condicional) + "end"
    p[0] = p[3] + "jz " + elseEnd + "\n\n" + p[6] + "jump " + labelEnd + "\n\n" + elseEnd  + ":\n"+ p[10] + "\n" + labelEnd + ":\n"
    p.parser.contador_condicional += 1

def p_Comparacao(p):
    "Comparacao : Exp Comparador Exp"
    p[0] = p[1] + p[3] + p[2]

def p_Comparador_equal(p):
    "Comparador : COMP"
    p[0] = 'equal\n'

def p_Comparador_inf(p):
    "Comparador : '<'"
    p[0] = 'inf\n'    

def p_Comparador_sup(p):
    "Comparador : '>'"
    p[0] = 'sup\n'

def p_Comparador_infeq(p):
    "Comparador : MENORIGUAL"
    p[0] = 'infeq\n'

def p_Comparador_supeq(p):
    "Comparador : MAIORIGUAL"
    p[0] = 'supeq\n'

def p_Comparador_dif(p):
    "Comparador : DIF"
    p[0] = 'equal\nnot\n'

def p_Output_PRINT_Exp(p):
    "Output : PRINT '(' Exp ')' ';'"
    p[0] = p[3] + "writei\n"

def p_Output_PRINT_STRING(p):
    "Output : PRINT '(' STRING ')' ';'"
    p[0] = "pushs " + p[3] + "\nwrites\n"

def p_Output_PRINTLN_Exp(p):
    "Output : PRINTLN '(' Exp ')' ';'"
    p[0] = p[3] + "writei\npushs \"\\n\"\nwrites\n"

def p_Output_PRINTLN_STRING(p):
    "Output : PRINTLN '(' STRING ')' ';'"
    p[0] = "pushs " + p[3] + "\nwrites\npushs \"\\n\"\nwrites\n"

def p_Exp_add(p):
    "Exp : Exp '+' Termo"
    p[0] = p[1] + p[3] + "add\n"

def p_Exp_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = p[1] + p[3] + "sub\n"

def p_Exp_term(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : Termo '*' Fator"
    p[0] = p[1] +  p[3] + "mul\n"

def p_Termo_div(p):
    "Termo : Termo '/' Fator"
    p[0] = p[1] + p[3] + "div\n"

def p_Termo_mod(p):
    "Termo : Termo '%' Fator"
    p[0] = p[1] + p[3] + "mod\n"

def p_Termo_fator(p):
    "Termo : Fator"
    p[0] = p[1]

def p_Factor_id(p):
    "Fator : ID"
    if(p[1] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[1]][0] == 'int'):
            endereco = p.parser.tab_ids[p[1]][1]
            p[0] = "pushg " + str(endereco) + "\n"
        else:
            p.parser.errors.append("Variável " + p[1] + " não é do tipo esperado ( int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[1] + " não declarada")
        p.parser.success = False
        p[0] = ""


def p_Fator_arrayvalue(p):
    "Fator : ID '[' Exp ']'"
    if(p[1] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[1]][0] == 'int_array'):
            address = p.parser.tab_ids[p[1]][1]
            p[0] = "pushgp\npushi " + str(address) + "\npadd\n" + p[3] + "loadn\n"
        else:
            p.parser.errors.append("Variável " + p[1] + " não é do tipo esperado (array de int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[1] + " não declarada")
        parser.success = False
        p[0] = ""

def p_Fator_array_2Dim_value(p):
    "Fator : ID '[' Exp ']' '[' Exp ']'"
    if(p[1] in p.parser.tab_ids):
        if(p.parser.tab_ids[p[1]][0] == 'int_biarray'):
            address = p.parser.tab_ids[p[1]][1]
            offset = p[3] + "pushi " + str(p.parser.tab_ids[p[1]][3]) + "\nmul\n" + p[6] + "add\n"
            p[0] = "pushgp\npushi " + str(address) + "\npadd\n" + offset + "loadn\n"
        else:
            p.parser.errors.append("Variável " + p[1] + " não é do tipo esperado (array bidimensional de int)")
            p.parser.success = False
            p[0] = ""
    else:
        p.parser.errors.append("Variável " + p[1] + " não declarada")
        p.parser.success = False
        p[0] = ""

def p_Fator_number(p):
    "Fator : NUMBER"
    p[0] = "pushi " + p[1] + "\n"

def p_Fator_group(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]

def p_error(p):
    print('Syntax error:', p)
    outFile.write("err \"Erro de compilação\"\n")
    parser.success = False

def handle_error(p):
    for error in p.parser.errors:
        print(error)

#inicio do Parser e Calculadora
parser = yacc.yacc()

parser.success = True
parser.tab_ids = {}
parser.contador_ciclos = 0
parser.contador_condicional = 0
parser.contador_vars = 0
parser.contador_aux_arrays = 0
parser.errors = []

inFile = open(sys.argv[1],'r')
outFile = open(sys.argv[2],'w')

content = ""
for line in inFile:
    content += line

parser.parse(content)