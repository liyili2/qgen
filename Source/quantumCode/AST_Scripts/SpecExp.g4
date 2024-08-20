grammar SpecExp;

program: qexps '->' qexps
      | 'A' '(' vexp ',' vexp ')' program
      | 'E' Identifier '@' bexp '.' program ;

qexp: Nor '(' vexp ',' vexp ')'  | Phi '(' vexp ',' vexp ')' ;

qexps : qexp ( qexp )*;
        
vexp: Identifier | numexp
 | vexp Plus vexp
 | vexp Minus vexp
 | vexp Mult vexp
 | vexp Div vexp
 | vexp Mod vexp;

bexp: vexp Equal vexp
    | vexp Less vexp
    | vexp Greater vexp
    | Not bexp
    | bexp And bexp
    | bexp Or bexp;
                                            
numexp: Number | '-' Number ;       

Nor : 'Nor';

Phi : 'Phi';

Not : 'not';

And : '&&';

Or : '||';

Plus:  '+';
 
Minus: '-' ;

Mult: '*';
 
Div: '/';
        
Mod: '%';

Less: '<';

Equal: '=';

Greater: '>';
        
 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase

 Number : DIGIT+ ;

 Identifier :   Letter LetterOrDigit*;

 Letter :   [a-zA-Z$_];

 LetterOrDigit: [a-zA-Z0-9$_];

 fragment DIGIT: ('0'..'9');

 fragment ESCQUOTE : '\\"';
 StrLiteral :   '"' ( ESCQUOTE | ~('\n'|'\r') )*? '"';

 AT : '@';
 ELLIPSIS : '...';
 WS  :  [ \t\r\n\u000C]+ -> skip;
 Comment :   '/*' .*? '*/' -> skip;
 Line_Comment :   '//' ~[\r\n]* -> skip;
