# Generated from MiniFun_Parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,
        1,3,1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,63,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,89,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,98,8,4,1,4,5,4,
        101,8,4,10,4,12,4,104,9,4,1,5,1,5,1,5,1,5,3,5,110,8,5,1,6,1,6,1,
        6,1,6,5,6,116,8,6,10,6,12,6,119,9,6,1,6,1,6,1,7,1,7,1,7,0,1,8,8,
        0,2,4,6,8,10,12,14,0,1,1,0,20,26,134,0,17,1,0,0,0,2,23,1,0,0,0,4,
        33,1,0,0,0,6,41,1,0,0,0,8,88,1,0,0,0,10,109,1,0,0,0,12,111,1,0,0,
        0,14,122,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,
        1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,
        24,5,1,0,0,24,25,5,2,0,0,25,27,5,3,0,0,26,28,3,4,2,0,27,26,1,0,0,
        0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,4,0,0,30,31,5,5,0,0,31,32,
        3,8,4,0,32,3,1,0,0,0,33,38,5,2,0,0,34,35,5,6,0,0,35,37,5,2,0,0,36,
        34,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,
        0,40,38,1,0,0,0,41,46,3,8,4,0,42,43,5,6,0,0,43,45,3,8,4,0,44,42,
        1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,7,1,0,0,0,48,
        46,1,0,0,0,49,50,6,4,-1,0,50,89,3,10,5,0,51,89,5,2,0,0,52,53,5,7,
        0,0,53,54,3,8,4,0,54,55,5,8,0,0,55,56,3,8,4,0,56,57,5,9,0,0,57,58,
        3,8,4,6,58,89,1,0,0,0,59,60,5,10,0,0,60,62,5,3,0,0,61,63,3,4,2,0,
        62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,4,0,0,65,66,5,
        11,0,0,66,89,3,8,4,5,67,68,5,12,0,0,68,69,5,3,0,0,69,70,3,8,4,0,
        70,71,5,6,0,0,71,72,3,8,4,0,72,73,5,4,0,0,73,89,1,0,0,0,74,75,5,
        13,0,0,75,76,5,3,0,0,76,77,3,8,4,0,77,78,5,6,0,0,78,79,3,8,4,0,79,
        80,5,4,0,0,80,89,1,0,0,0,81,82,5,14,0,0,82,83,5,3,0,0,83,84,3,8,
        4,0,84,85,5,6,0,0,85,86,3,8,4,0,86,87,5,4,0,0,87,89,1,0,0,0,88,49,
        1,0,0,0,88,51,1,0,0,0,88,52,1,0,0,0,88,59,1,0,0,0,88,67,1,0,0,0,
        88,74,1,0,0,0,88,81,1,0,0,0,89,102,1,0,0,0,90,91,10,7,0,0,91,92,
        3,14,7,0,92,93,3,8,4,8,93,101,1,0,0,0,94,95,10,4,0,0,95,97,5,3,0,
        0,96,98,3,6,3,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,101,
        5,4,0,0,100,90,1,0,0,0,100,94,1,0,0,0,101,104,1,0,0,0,102,100,1,
        0,0,0,102,103,1,0,0,0,103,9,1,0,0,0,104,102,1,0,0,0,105,110,5,15,
        0,0,106,110,5,16,0,0,107,110,5,17,0,0,108,110,3,12,6,0,109,105,1,
        0,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,1,0,0,0,110,11,1,0,
        0,0,111,112,5,18,0,0,112,117,3,8,4,0,113,114,5,6,0,0,114,116,3,8,
        4,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,120,1,0,0,0,119,117,1,0,0,0,120,121,5,19,0,0,121,13,1,0,
        0,0,122,123,7,0,0,0,123,15,1,0,0,0,11,19,27,38,46,62,88,97,100,102,
        109,117
    ]

class MiniFun_Parser ( Parser ):

    grammarFileName = "MiniFun_Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "DEF", "ID", "LPAREN", "RPAREN", "ASSIGN", 
                      "COMMA", "IF", "THEN", "ELSE", "FUN", "ARROW", "MAP", 
                      "FILTER", "REDUCE", "INT", "TRUE", "FALSE", "LBRACK", 
                      "RBRACK", "PLUS", "MINUS", "MUL", "EQ", "NEQ", "AND", 
                      "OR" ]

    RULE_program = 0
    RULE_function_def = 1
    RULE_params = 2
    RULE_args = 3
    RULE_expression = 4
    RULE_literal = 5
    RULE_list = 6
    RULE_operator = 7

    ruleNames =  [ "program", "function_def", "params", "args", "expression", 
                   "literal", "list", "operator" ]

    EOF = Token.EOF
    DEF=1
    ID=2
    LPAREN=3
    RPAREN=4
    ASSIGN=5
    COMMA=6
    IF=7
    THEN=8
    ELSE=9
    FUN=10
    ARROW=11
    MAP=12
    FILTER=13
    REDUCE=14
    INT=15
    TRUE=16
    FALSE=17
    LBRACK=18
    RBRACK=19
    PLUS=20
    MINUS=21
    MUL=22
    EQ=23
    NEQ=24
    AND=25
    OR=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniFun_Parser.EOF, 0)

        def function_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniFun_Parser.Function_defContext)
            else:
                return self.getTypedRuleContext(MiniFun_Parser.Function_defContext,i)


        def getRuleIndex(self):
            return MiniFun_Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MiniFun_Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.function_def()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 21
            self.match(MiniFun_Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(MiniFun_Parser.DEF, 0)

        def ID(self):
            return self.getToken(MiniFun_Parser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniFun_Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniFun_Parser.RPAREN, 0)

        def ASSIGN(self):
            return self.getToken(MiniFun_Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniFun_Parser.ExpressionContext,0)


        def params(self):
            return self.getTypedRuleContext(MiniFun_Parser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniFun_Parser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)




    def function_def(self):

        localctx = MiniFun_Parser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(MiniFun_Parser.DEF)
            self.state = 24
            self.match(MiniFun_Parser.ID)
            self.state = 25
            self.match(MiniFun_Parser.LPAREN)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 26
                self.params()


            self.state = 29
            self.match(MiniFun_Parser.RPAREN)
            self.state = 30
            self.match(MiniFun_Parser.ASSIGN)
            self.state = 31
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniFun_Parser.ID)
            else:
                return self.getToken(MiniFun_Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniFun_Parser.COMMA)
            else:
                return self.getToken(MiniFun_Parser.COMMA, i)

        def getRuleIndex(self):
            return MiniFun_Parser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = MiniFun_Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MiniFun_Parser.ID)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 34
                self.match(MiniFun_Parser.COMMA)
                self.state = 35
                self.match(MiniFun_Parser.ID)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniFun_Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniFun_Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniFun_Parser.COMMA)
            else:
                return self.getToken(MiniFun_Parser.COMMA, i)

        def getRuleIndex(self):
            return MiniFun_Parser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = MiniFun_Parser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.expression(0)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 42
                self.match(MiniFun_Parser.COMMA)
                self.state = 43
                self.expression(0)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniFun_Parser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniFun_Parser.ID, 0)

        def IF(self):
            return self.getToken(MiniFun_Parser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniFun_Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniFun_Parser.ExpressionContext,i)


        def THEN(self):
            return self.getToken(MiniFun_Parser.THEN, 0)

        def ELSE(self):
            return self.getToken(MiniFun_Parser.ELSE, 0)

        def FUN(self):
            return self.getToken(MiniFun_Parser.FUN, 0)

        def LPAREN(self):
            return self.getToken(MiniFun_Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniFun_Parser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(MiniFun_Parser.ARROW, 0)

        def params(self):
            return self.getTypedRuleContext(MiniFun_Parser.ParamsContext,0)


        def MAP(self):
            return self.getToken(MiniFun_Parser.MAP, 0)

        def COMMA(self):
            return self.getToken(MiniFun_Parser.COMMA, 0)

        def FILTER(self):
            return self.getToken(MiniFun_Parser.FILTER, 0)

        def REDUCE(self):
            return self.getToken(MiniFun_Parser.REDUCE, 0)

        def operator(self):
            return self.getTypedRuleContext(MiniFun_Parser.OperatorContext,0)


        def args(self):
            return self.getTypedRuleContext(MiniFun_Parser.ArgsContext,0)


        def getRuleIndex(self):
            return MiniFun_Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniFun_Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18]:
                self.state = 50
                self.literal()
                pass
            elif token in [2]:
                self.state = 51
                self.match(MiniFun_Parser.ID)
                pass
            elif token in [7]:
                self.state = 52
                self.match(MiniFun_Parser.IF)
                self.state = 53
                self.expression(0)
                self.state = 54
                self.match(MiniFun_Parser.THEN)
                self.state = 55
                self.expression(0)
                self.state = 56
                self.match(MiniFun_Parser.ELSE)
                self.state = 57
                self.expression(6)
                pass
            elif token in [10]:
                self.state = 59
                self.match(MiniFun_Parser.FUN)
                self.state = 60
                self.match(MiniFun_Parser.LPAREN)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 61
                    self.params()


                self.state = 64
                self.match(MiniFun_Parser.RPAREN)
                self.state = 65
                self.match(MiniFun_Parser.ARROW)
                self.state = 66
                self.expression(5)
                pass
            elif token in [12]:
                self.state = 67
                self.match(MiniFun_Parser.MAP)
                self.state = 68
                self.match(MiniFun_Parser.LPAREN)
                self.state = 69
                self.expression(0)
                self.state = 70
                self.match(MiniFun_Parser.COMMA)
                self.state = 71
                self.expression(0)
                self.state = 72
                self.match(MiniFun_Parser.RPAREN)
                pass
            elif token in [13]:
                self.state = 74
                self.match(MiniFun_Parser.FILTER)
                self.state = 75
                self.match(MiniFun_Parser.LPAREN)
                self.state = 76
                self.expression(0)
                self.state = 77
                self.match(MiniFun_Parser.COMMA)
                self.state = 78
                self.expression(0)
                self.state = 79
                self.match(MiniFun_Parser.RPAREN)
                pass
            elif token in [14]:
                self.state = 81
                self.match(MiniFun_Parser.REDUCE)
                self.state = 82
                self.match(MiniFun_Parser.LPAREN)
                self.state = 83
                self.expression(0)
                self.state = 84
                self.match(MiniFun_Parser.COMMA)
                self.state = 85
                self.expression(0)
                self.state = 86
                self.match(MiniFun_Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 100
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MiniFun_Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 90
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 91
                        self.operator()
                        self.state = 92
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = MiniFun_Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 94
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 95
                        self.match(MiniFun_Parser.LPAREN)
                        self.state = 97
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 521348) != 0):
                            self.state = 96
                            self.args()


                        self.state = 99
                        self.match(MiniFun_Parser.RPAREN)
                        pass

             
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniFun_Parser.INT, 0)

        def TRUE(self):
            return self.getToken(MiniFun_Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniFun_Parser.FALSE, 0)

        def list_(self):
            return self.getTypedRuleContext(MiniFun_Parser.ListContext,0)


        def getRuleIndex(self):
            return MiniFun_Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = MiniFun_Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(MiniFun_Parser.INT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(MiniFun_Parser.TRUE)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.match(MiniFun_Parser.FALSE)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniFun_Parser.LBRACK, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniFun_Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniFun_Parser.ExpressionContext,i)


        def RBRACK(self):
            return self.getToken(MiniFun_Parser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniFun_Parser.COMMA)
            else:
                return self.getToken(MiniFun_Parser.COMMA, i)

        def getRuleIndex(self):
            return MiniFun_Parser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = MiniFun_Parser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(MiniFun_Parser.LBRACK)
            self.state = 112
            self.expression(0)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 113
                self.match(MiniFun_Parser.COMMA)
                self.state = 114
                self.expression(0)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(MiniFun_Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MiniFun_Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniFun_Parser.MINUS, 0)

        def MUL(self):
            return self.getToken(MiniFun_Parser.MUL, 0)

        def EQ(self):
            return self.getToken(MiniFun_Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniFun_Parser.NEQ, 0)

        def AND(self):
            return self.getToken(MiniFun_Parser.AND, 0)

        def OR(self):
            return self.getToken(MiniFun_Parser.OR, 0)

        def getRuleIndex(self):
            return MiniFun_Parser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = MiniFun_Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133169152) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




