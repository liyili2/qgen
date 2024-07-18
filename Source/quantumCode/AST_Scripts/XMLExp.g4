grammar XMLExp;

root: '<' Root '>' program '</' Root '>';

nextexp: '<' Next '>' program '</' Next '>';

program: exp (exp)* ;

exp: letexp | appexp | blockexp | cuexp | ifexp | matchexp | skipexp | xexp | srexp | qftexp | lshiftexp | rshiftexp | revexp | rqftexp;

blockexp : '<' BLOCK '>' '</' BLOCK '>';

idexp : '<' VEXP OP '=' '\'' ID '\'' '>' Identifier '</' VEXP '>' ;

exppair : '<' Pair 'case' '=' '\'' element '\'' '>' program '</' Pair '>' ;

matchexp : '<' Match 'id' '=' '\'' Identifier '\'' '>' exppair (exppair)* '</' Match '>' ;

letexp : '<' Let 'id' '=' '\'' Identifier '\'' '>' (idexp)* program '</' Let '>' ;

ifexp : '<' Ifa '>' vexp nextexp nextexp '</' Ifa '>';

appexp : '<' APP 'id' '=' '\'' Identifier '\'' '>' (vexp)* '</' APP '>';

//ida : '<' ID 'type' '=' '\'' atype '\'' '>' Identifier '</' ID '>' ;
        
vexp: idexp | '<' VEXP OP '=' '\'' NUM '\'' '>' numexp '</' VEXP '>'
    | '<' VEXP OP '=' '\'' op '\'' '>' vexp vexp '</' VEXP '>';

element : numexp | Identifier;

numexp: Number | Minus Number;
        
 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase

skipexp: '<' PEXP 'gate' '=' '\'' 'SKIP' '\'' 'id' '=' '\'' Identifier '\'' '>' vexp '</' PEXP '>' ;

xexp: '<' PEXP 'gate' '=' '\'' 'X' '\'' 'id' '=' '\'' Identifier '\'' '>' vexp '</' PEXP '>' ;

cuexp: '<' PEXP 'gate' '=' '\'' 'CU' '\'' 'id' '=' '\'' Identifier '\'' '>' vexp program '</' PEXP '>' ;

//rzexp: '<' PEXP 'gate' '=' '\'' 'RZ' '\'' 'id' '=' '\'' Identifier '\'' '>' vexp vexp '</' PEXP '>' ;

srexp: '<' PEXP 'gate' '=' '\'' 'SR' '\'' 'id' '=' '\'' Identifier '\'' '>' vexp '</' PEXP '>' ;

lshiftexp: '<' PEXP 'gate' '=' '\'' 'Lshift' '\'' 'id' '=' '\'' Identifier '\'' '>' '</' PEXP '>' ;

rshiftexp: '<' PEXP 'gate' '=' '\'' 'Rshift' '\'' 'id' '=' '\'' Identifier '\'' '>' '</' PEXP '>' ;

revexp: '<' PEXP 'gate' '=' '\'' 'Rev' '\'' 'id' '=' '\'' Identifier '\'' '>' '</' PEXP '>' ;

qftexp: '<' PEXP 'gate' '=' '\'' 'QFT' '\'' 'id' '=' '\'' Identifier '\'' '>' vexp '</' PEXP '>' ;

rqftexp: '<' PEXP 'gate' '=' '\'' 'RQFT' '\'' 'id' '=' '\'' Identifier '\'' '>' '</' PEXP '>' ;

op: Plus | Minus | Times | Div | Mod | Exp | GNum;

//atype: Qubits | Nat | Bits;

//boolexp: TrueLiteral | FalseLiteral;

BLOCK: 'block';

Root : 'root';

Next : 'next';

Let : 'let';

Ifa : 'if';

Match : 'match';

Pair : 'pair';

Qubits : 'qubits';

Nat : 'nat';

Bits : 'bits';

 TrueLiteral : '#t' ;
 FalseLiteral : '#f' ;
 Dot : '.' ;

 RQFT : 'RQFT' ;

 OP : 'op';

 Plus : '+';

 Minus : '-';

 Times : '*';

 Div : '/';

 Mod : '%';

 Exp : '^';

 GNum : '$';

 APP : 'app';

 PEXP : 'pexp';

 VEXP : 'vexp';

 ID : 'id';

 NUM: 'num';

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
