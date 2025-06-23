import re

TOKEN_SPEC = [
    ('INT_TYPE',   r'\bint\b'),
    ('BOOL_TYPE',  r'\bbool\b'),
    ('VOID',       r'\bvoid\b'),
    ('STRUCT',     r'\bstruct\b'),
    ('IF',         r'\bif\b'),
    ('ELSE',       r'\belse\b'),
    ('WHILE',      r'\bwhile\b'),
    ('RETURN',     r'\breturn\b'),
    ('TRUE',       r'\btrue\b'),
    ('FALSE',      r'\bfalse\b'),
    ('ID',         r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER',     r'\d+'),
    ('EQ',         r'=='),
    ('NEQ',        r'!='),
    ('LEQ',        r'<='),
    ('GEQ',        r'>='),
    ('LT',         r'<'),
    ('GT',         r'>'),
    ('AND',        r'&&'),
    ('OR',         r'\|\|'),
    ('ASSIGN',     r'='),
    ('PLUS',       r'\+'),
    ('MINUS',      r'-'),
    ('MUL',        r'\*'),
    ('DIV',        r'/'),
    ('MOD',        r'%'),
    ('LPAREN',     r'\('),
    ('RPAREN',     r'\)'),
    ('LBRACK',     r'\['),
    ('RBRACK',     r'\]'),
    ('LBRACE',     r'\{'),
    ('RBRACE',     r'\}'),
    ('COMMA',      r','),
    ('SEMI',       r';'),
    ('SKIP',       r'[ \t]+'),
    ('NEWLINE',    r'\r?\n'),
    ('MISMATCH',   r'.'),
]

def lexer(code):
    tokens = []
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Carácter inesperado: {value}")
        else:
            tokens.append((kind, value))
    return tokens
