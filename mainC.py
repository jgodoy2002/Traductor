from MiniC_Lexer import lexer
from MiniC_Parser import MiniCParser

def separador():
    print("=" * 60)

def imprimir_ast(ast):
    print("Árbol de Sintaxis Abstracta (AST):")
    for nodo in ast:
        print(f"  {nodo}")

def test_minic(codigo):
    separador()
    print("Código MiniC de entrada:")
    print(codigo)

    try:
        tokens = lexer(codigo)
        print("\nTokens:")
        for t in tokens:
            print(f"  {t}")
        
        parser = MiniCParser(tokens)
        ast = parser.parse()
        
        print()
        imprimir_ast(ast)
    except Exception as e:
        print(f"\n Error durante el análisis: {e}")

if __name__ == "__main__":
    ejemplo = """
    int cuadrado(int x) {
        int y = 2;
        return x * x;
    }

    int suma(int a, int b) {
        return a + b;
    }
    """

    test_minic(ejemplo)
