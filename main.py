from MiniFun_Parser import Parser
from MiniFun_Lexer import lexer  

def test_code(code):
    print(f"\n=== Código: {code}")
    tokens = lexer(code)
    parser = Parser(tokens)
    try:
        ast = parser.parse()
        print("AST:", ast)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Caso 1: Definición de función simple
    code1 = "def suma(x, y) = x + y"
    
    # Caso 2: Expresión if
    code2 = "def max(a, b) = if a > b then a else b"
    
    # Caso 3: Función anónima y llamada
    code3 = "def apply(f, x) = f(x)"

    # Caso 4: Función anonima sencila
    code4 = "fun(x, y) => x + y"

    test_code(code1)
    test_code(code2)
    test_code(code3)
    test_code(code4)