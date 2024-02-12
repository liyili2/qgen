grammar XMLExp;

program: exp (exp)* ;

exp: skipexp | xexp | cuexp | rzexp | srexp | lshiftexp | rshiftexp | revexp | qftexp | rqftexp;

idexp : '<' ID '>' Identifier '</' ID '>';
        
vexp: idexp | '<' VEXP '>' numexp '</' VEXP '>'
    | '<' VEXP '>' boolexp '</' VEXP '>' | '<' VEXP OP '=' '\'' op '\'' '>' vexp vexp '</' VEXP '>';

numexp: Number | Minus Number;
        
 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase

skipexp: '<' PEXP 'gate' '=' 'SKIP' flag '>' idexp vexp '</' PEXP '>' ;

xexp: '<' PEXP 'gate' '=' 'X' flag '>' idexp vexp '</' PEXP '>' ;

cuexp: '<' PEXP 'gate' '=' 'CU' flag '>' idexp vexp program '</' PEXP '>' ;

rzexp: '<' PEXP 'gate' '=' 'RZ' flag '>' vexp idexp vexp '</' PEXP '>' ;

srexp: '<' PEXP 'gate' '=' 'SR' flag '>' vexp idexp '</' PEXP '>' ;

lshiftexp: '<' PEXP 'gate' '=' 'Lshift' flag '>' idexp '</' PEXP '>' ;

rshiftexp: '<' PEXP 'gate' '=' 'Rshift' flag '>' idexp '</' PEXP '>' ;

revexp: '<' PEXP 'gate' '=' 'Rev' flag '>' idexp '</' PEXP '>' ;

qftexp: '<' PEXP 'gate' '=' 'QFT' flag '>' idexp vexp '</' PEXP '>' ;

rqftexp: '<' PEXP 'gate' '=' 'RQFT' flag '>' idexp vexp '</' PEXP '>' ;

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
