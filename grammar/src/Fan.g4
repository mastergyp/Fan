grammar Fan;

// PARSER RULES
prog: statements EOF;

statements: statement*;

statement: terminated;

terminated:
    (expr) TERMINATED;

//LEXER RULES
expr:
    ID ASSIGN expr
    |LPAREN expr RPAREN
    | expr (POWER) expr
    | MINUS expr
    | expr (MUL|DIV) expr
    | expr (MINUS|PLUS) expr
    | INT
    | ID;

// BLOCKS AND ENCLOUSURES
LPAREN : '(';
RPAREN : ')';


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
INT: DIGIT+;

ID: [A-Za-z];

// COMMENTS RULES
BLOCK_COMMENT:  DIV MUL .*? MUL DIV -> channel(HIDDEN);
LINE_COMMENT:   DIV DIV ~[\r\n]* -> channel(HIDDEN);


// NEWLINES and WHITESPACE
NEWLINE: '\r' ? '\n' -> skip;
WS: (' '| '\t')+ -> skip;


//FRAGMENTS

fragment LETTER: A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z;

fragment A: 'A' | 'a'; fragment B: 'B' | 'b'; fragment C: 'C' | 'c'; fragment D: 'D' | 'd'; fragment E: 'E' | 'e';
fragment F: 'F' | 'f'; fragment G: 'G' | 'g'; fragment H: 'H' | 'h'; fragment I: 'I' | 'i'; fragment J: 'J' | 'j';
fragment K: 'K' | 'k'; fragment L: 'L' | 'l'; fragment M: 'M' | 'm'; fragment N: 'N' | 'n'; fragment O: 'O' | 'o';
fragment P: 'P' | 'p'; fragment Q: 'Q' | 'q'; fragment R: 'R' | 'r'; fragment S: 'S' | 's'; fragment T: 'T' | 't';
fragment U: 'U' | 'u'; fragment V: 'V' | 'v'; fragment W: 'W' | 'w'; fragment X: 'X' | 'x'; fragment Y: 'Y' | 'y';
fragment Z: 'Z' | 'z';

fragment UPPERLETTER: [A-Za-z];

fragment DIGIT: [0-9];

