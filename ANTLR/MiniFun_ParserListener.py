# Generated from MiniFun_Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniFun_Parser import MiniFun_Parser
else:
    from MiniFun_Parser import MiniFun_Parser

# This class defines a complete listener for a parse tree produced by MiniFun_Parser.
class MiniFun_ParserListener(ParseTreeListener):

    # Enter a parse tree produced by MiniFun_Parser#program.
    def enterProgram(self, ctx:MiniFun_Parser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#program.
    def exitProgram(self, ctx:MiniFun_Parser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniFun_Parser#function_def.
    def enterFunction_def(self, ctx:MiniFun_Parser.Function_defContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#function_def.
    def exitFunction_def(self, ctx:MiniFun_Parser.Function_defContext):
        pass


    # Enter a parse tree produced by MiniFun_Parser#params.
    def enterParams(self, ctx:MiniFun_Parser.ParamsContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#params.
    def exitParams(self, ctx:MiniFun_Parser.ParamsContext):
        pass


    # Enter a parse tree produced by MiniFun_Parser#args.
    def enterArgs(self, ctx:MiniFun_Parser.ArgsContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#args.
    def exitArgs(self, ctx:MiniFun_Parser.ArgsContext):
        pass


    # Enter a parse tree produced by MiniFun_Parser#expression.
    def enterExpression(self, ctx:MiniFun_Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#expression.
    def exitExpression(self, ctx:MiniFun_Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniFun_Parser#literal.
    def enterLiteral(self, ctx:MiniFun_Parser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#literal.
    def exitLiteral(self, ctx:MiniFun_Parser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniFun_Parser#list.
    def enterList(self, ctx:MiniFun_Parser.ListContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#list.
    def exitList(self, ctx:MiniFun_Parser.ListContext):
        pass


    # Enter a parse tree produced by MiniFun_Parser#operator.
    def enterOperator(self, ctx:MiniFun_Parser.OperatorContext):
        pass

    # Exit a parse tree produced by MiniFun_Parser#operator.
    def exitOperator(self, ctx:MiniFun_Parser.OperatorContext):
        pass



del MiniFun_Parser