parser grammar MiniFun_Parser;

program         : function_def+ EOF ;

function_def    : DEF ID LPAREN params? RPAREN ASSIGN expression ;

params          : ID ( COMMA ID )* ;

args            : expression ( COMMA expression )* ;

expression      : literal
                | ID
                | expression operator expression
                | IF expression THEN expression ELSE expression
                | FUN LPAREN params? RPAREN ARROW expression
                | expression LPAREN args? RPAREN
                | MAP LPAREN expression COMMA expression RPAREN
                | FILTER LPAREN expression COMMA expression RPAREN
                | REDUCE LPAREN expression COMMA expression RPAREN ;

literal         : INT | TRUE | FALSE | list ;

list            : LBRACK expression ( COMMA expression )* RBRACK ;

operator        : PLUS | MINUS | MUL | EQ | NEQ | AND | OR ;
