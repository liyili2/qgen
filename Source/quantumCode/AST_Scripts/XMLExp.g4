grammar XMLExp;

program: xexp (xexp)* ;

xexp: '<' Identifier '>' nextlevel '</' Identifier '>' ;
        
vexp: Identifier | numexp | boolexp | vexp '+' vexp | vexp '-' vexp | vexp '*'  vexp | vexp '/' vexp | vexp '%' vexp | vexp '^' vexp;

nextlevel: program | vexp | typeexp ;

numexp: Number | '-' Number | Number Dot Number | '-' Number Dot Number;       
        
 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase

typeexp: Nor | QFT '(' Number ')';

boolexp: TrueLiteral | FalseLiteral;

 TrueLiteral : '#t' ;
 FalseLiteral : '#f' ;
 Dot : '.' ;
 Nor : 'Nor' ;
 QFT : 'QFT' ;

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
