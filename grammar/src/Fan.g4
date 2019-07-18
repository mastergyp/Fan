grammar Fan;

// PARSER RULES
prog: statements EOF;

statements: statement*;

statement: terminated;

terminated:
    (expr) TERMINATED;

//LEXER RULES
expr:
    STRING                            # String
    |IF expr THEN expr (ELSE expr)?   # If
    |ID ASSIGN expr                   # Assign
    |expr (NOT)? IN ID                # InField
    |expr (NOT)? IN array             # InList
    |LPAREN expr RPAREN               # Paren
    |<assoc=right> expr (POWER) expr  # Power
    |expr (MUL|DIV) expr              # MulAndDiv
    |expr (MINUS|PLUS) expr           # PlusAndMinus
    |expr (EQ|NEQ|GT|LT|GTE|LTE) expr # Boolean
    |expr (AND|OR) expr               # BooleanExpr
    |FUNC LPAREN (expr (',' expr)*)? RPAREN  # FunctionCall
    |NUMBER                           # Number
    |ID                               # Id
    |PRINT expr                       # Print
    |RETURN expr                      # Return
    ;


array: '[' ID (',' ID)* ']'
      |'[' ']';

STRING: '"' '"'
       | '"' WORD_FOR_STRING (WORD_FOR_STRING)* '"'
;

// BLOCKS AND ENCLOUSURES
LPAREN : '(';
RPAREN : ')';

IF: 'if';
THEN: 'then';
ELSE: 'else';
PRINT: 'print';
IN: 'in';
RETURN: 'return';


// BOOLEAN
EQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';

AND: 'and';
OR: 'or';
NOT: 'not';

TRUE: 'True';
FALSE: 'False';

// Function call
FUNC:
    '重复数量'
    ;




// KEY SYMBOLS
TERMINATED: ';';


// OPERATORS
DIV:    '/';
MUL:    '*';
PLUS:   '+';
MINUS:  '-';
POWER:  '^';

ASSIGN: '=';

// TYPES
NUMBER: [-] ? ('.' DIGIT+ | DIGIT+ ('.' DIGIT*)? );



ID: WORD+;

// COMMENTS RULES
BLOCK_COMMENT:  DIV MUL .*? MUL DIV -> channel(HIDDEN);
LINE_COMMENT:   DIV DIV ~[\r\n]* -> channel(HIDDEN);


// NEWLINES and WHITESPACE
NEWLINE: '\r' ? '\n' -> skip;
WS: (' '| '\t')+ -> skip;


//FRAGMENTS
fragment DIGIT: [0-9];
fragment WORD: ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9'|'\u4E00'..'\u9FA5' | '\uF900'..'\uFA2D');
fragment WORD_FOR_STRING: WORD  | ' ' | '\'' | '_';

