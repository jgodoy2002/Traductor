from MiniC_Lexer import lexer
from MiniC_Parser import MiniCParser
from C_Analizador import AnalizadorSemanticoC


def separador():
    print("=" * 60)

def imprimir_ast(ast):
    print("Árbol de Sintaxis Abstracta (AST):")
    for nodo in ast:
        print(f"  {nodo}")

def imprimir_errores_semanticos(errores):
    print("\nErrores Semánticos:")
    if errores:
        for err in errores:
            print(f"  - {err}")
    else:
        print("  :) No se encontraron errores semánticos.")

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

        # === Análisis Semántico ===
        analizador = AnalizadorSemanticoC()
        analizador.analizar(ast)
        imprimir_errores_semanticos(analizador.tabla.errors)

    except Exception as e:
        print(f"\nError durante el análisis: {e}")

if __name__ == "__main__":
    ejemplo = """
    int cuadrado(int x) {
        int y = 2;
        return x * x;
    }

    int suma(int a, int b) {
        return a + b;
    }

    int falla() {
        return z;
    }
    """

    test_minic(ejemplo)
