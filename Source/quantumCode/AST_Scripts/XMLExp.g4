grammar XMLExp;

program: exp (exp)* ;

exp: skipexp | xexp | cuexp | rzexp | srexp | lshiftexp | rshiftexp | revexp | qftexp | rqftexp;

idexp : '<' ID '>' Identifier '</' ID '>';
        
vexp: idexp | '<' VEXP '>' numexp '</' VEXP '>'
    | '<' VEXP '>' boolexp '</' VEXP '>' | '<' VEXP OP '=' '\'' op '\'' '>' vexp vexp '</' VEXP '>';

numexp: Number | '-' Number | Number Dot Number | '-' Number Dot Number;       
        
 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase

skipexp: '<' PEXP Gate '=' skip flag '>' idexp vexp '</' PEXP '>' ;

xexp: '<' PEXP Gate '=' X flag '>' idexp vexp '</' PEXP '>' ;

cuexp: '<' PEXP Gate '=' CU flag '>' idexp vexp program '</' PEXP '>' ;

rzexp: '<' PEXP Gate '=' RZ flag '>' vexp idexp vexp '</' PEXP '>' ;

srexp: '<' PEXP Gate '=' SR flag '>' vexp vexp '</' PEXP '>' ;

lshiftexp: '<' PEXP Gate '=' Lshift flag '>' vexp '</' PEXP '>' ;

rshiftexp: '<' PEXP Gate '=' Rshift flag '>' vexp '</' PEXP '>' ;

revexp: '<' PEXP Gate '=' Rev flag '>' vexp '</' PEXP '>' ;

qftexp: '<' PEXP Gate '=' QFT flag '>' vexp '</' PEXP '>' ;

rqftexp: '<' PEXP Gate '=' RQFT flag '>' vexp '</' PEXP '>' ;

op: Plus | Minus | Times | Div | Mod | Exp;

flag: Type '=' '\'' typeexp '\'';

typeexp: Nor | QFT '(' Number ')';

boolexp: TrueLiteral | FalseLiteral;

 TrueLiteral : '#t' ;
 FalseLiteral : '#f' ;
 Dot : '.' ;
 Nor : 'Nor' ;
 QFT : 'QFT' ;

 RQFT : 'RQFT' ;

 OP : 'op';

 Plus : '+';

 Minus : '-';

 Times : '*';

 Div : '/';

 Mod : '%';

 Exp : '^';

 skip : 'SKIP';

 X : 'X';

 RZ : 'RZ';

 SR : 'SR';

 CU : 'CU';

 Lshift : 'Lshift';

 Rshift : 'Rshift';

 Rev : 'Rev';

 Gate : 'gate';

 Type : 'type';

 PEXP : 'pexp';

 VEXP : 'vexp';

 ID : 'id';

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
