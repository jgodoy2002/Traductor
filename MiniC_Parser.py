class MiniCParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def eat(self, kind):
        token = self.current()
        if token[0] == kind:
            self.pos += 1
            return token[1]
        else:
            raise SyntaxError(f"Se esperaba {kind} pero se encontró {token}")

    def parse(self):
        functions = []
        while self.current()[0] != 'EOF':
            functions.append(self.parse_function())
        return functions

    def parse_function(self):
        ret_type = self.eat('INT_TYPE')
        name = self.eat('ID')
        self.eat('LPAREN')
        params = self.parse_params()
        self.eat('RPAREN')
        self.eat('LBRACE')
        body = []
        while self.current()[0] != 'RBRACE':
            body.append(self.parse_statement())
        self.eat('RBRACE')
        return ('function', ret_type, name, params, body)

    def parse_params(self):
        params = []
        if self.current()[0] in ('INT_TYPE', 'BOOL_TYPE'):
            while True:
                ptype = self.eat(self.current()[0])
                pname = self.eat('ID')
                params.append((ptype, pname))
                if self.current()[0] != 'COMMA':
                    break
                self.eat('COMMA')
        return params

    def parse_statement(self):
        if self.current()[0] == 'INT_TYPE':
            return self.parse_var_decl()
        elif self.current()[0] == 'RETURN':
            return self.parse_return()
        else:
            raise SyntaxError(f"Sentencia inesperada: {self.current()}")

    def parse_var_decl(self):
        vtype = self.eat('INT_TYPE')
        name = self.eat('ID')
        self.eat('ASSIGN')
        value = self.eat('NUMBER')
        self.eat('SEMI')
        return ('var_decl', vtype, name, int(value))

    def parse_return(self):
        self.eat('RETURN')
        value = self.eat('NUMBER')
        self.eat('SEMI')
        return ('return', int(value))
