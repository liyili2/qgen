grammar SpecExp;

program: aexp '->' aexp ;

aexp: '|' vexp '>' ('|' vexp '>')* ;
        
vexp: Identifier | numexp | vexp Plus vexp | vexp Minus vexp | vexp Mult  vexp | vexp Div vexp | vexp Mod vexp | vexp Less vexp | vexp Equal vexp | vexp Greater vexp;
                                            
numexp: Number | '-' Number ;       
  
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
