import re

# Lista de patrones y su tipo
token_spec = [
    ('DEF', r'\bdef\b'),
    ('FUN', r'\bfun\b'), 
    ('VARINT', r'\bint\b'), ('VARBOOL', r'\bbool\b'), ('VARFLOAT', r'\bfloat\b'), 
    ('IF', r'\bif\b'), ('THEN', r'\bthen\b'), ('ELSE', r'\belse\b'),
    ('MAP', r'\bmap\b'), ('FILTER', r'\bfilter\b'), ('REDUCE', r'\breduce\b'),
    ('TRUE', r'\btrue\b'), ('FALSE', r'\bfalse\b'),
    ('FLOAT', r'\d+\.\d+'), ('INT', r'\d+'), 
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('EQ', r'=='), ('NEQ', r'!='), ('MORETHAN', r'>'), ('LESSTHAN', r'<'), ('AND', r'&&'), ('OR', r'\|\|'), 
    ('ARROW', r'=>'), ('ASSIGN', r'='),
    ('PLUS', r'\+'), ('MINUS', r'-'), ('MUL', r'\*'), ('DIV', r'\/'),
    ('LPAREN', r'\('), ('RPAREN', r'\)'),
    ('LBRACK', r'\['), ('RBRACK', r'\]'),
    ('COMMA', r','), ('ENDLINE', r'\r?\n'), ('SKIP', r'[ \t]+'), ('MISMATCH', r'.')
]

def lexer(code):
    tokens = []
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Error: símbolo inesperado {value}')
        else:
            tokens.append((kind, value))
    return tokens
