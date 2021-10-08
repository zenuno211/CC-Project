import sys
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER', 'STRING', 'ID', 'COMP','MENORIGUAL','MAIORIGUAL','INT','WHILE','IF','ELSE','READ','PRINT', 'PRINTLN','DIF'
)

# Literals
literals = ['+', '-', '*', '/', '(', ')', '?', '!','{','}','<','>',';','=', '[', ']','%',',']
 
t_NUMBER = r'\d+'

t_STRING = r'\".*?\"'

t_INT = r'\bint\b'

t_WHILE = r'\bwhile\b'

t_IF = r'\bif\b'

t_ELSE = r'\belse\b'

t_READ = r'\bread\b'

t_PRINT = r'\bprint\b'

t_PRINTLN = r'\bprintln\b'

t_ID = r'\w+'

t_COMP = r'=='

t_DIF = r'!='

t_MENORIGUAL = r'<='
    
t_MAIORIGUAL = r'>='

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'
 
# Error handling rule
def t_error(t):
    print("Caracter inesperado '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

file = open('codetest.txt')

for line in file:
    lexer.input(line)
    tok = lexer.token()
    while tok:
        #print(tok)
        tok = lexer.token()