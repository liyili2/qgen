grammar Exp;

exp: Identifier | letexp | callexp | ifexp | skipexp | xgexp | cuexp 
   | rzexp | rrzexp | srexp | srrexp | lshiftexp | rshiftexp | revexp | qftexp | rqftexp | exp Seq exp ;
        
vexp: Identifier | numexp | boolexp | addexp | subexp | multexp | divexp | modexp | expexp;

bexp: lessexp | equalexp | greaterexp | andexp | orexp;        
        
posiexp : '(' vexp ','  vexp  ')' ;

skipexp: SKIPEXP posiexp;

xgexp: Xgate posiexp;
       
cuexp: CU posiexp exp;
       
rzexp: RZ vexp exp;
       
rrzexp: RRZ vexp exp;

srexp: SR vexp exp;
       
srrexp: SRR vexp exp;

lshiftexp: Lshift vexp;

rshiftexp: Rshift vexp;

revexp: Rev vexp;

qftexp: QFT vexp vexp;
       
rqftexp: RQFT vexp vexp;
                                            
numexp: Number | '-' Number | Number Dot Number | '-' Number Dot Number;       
  
addexp:  exp '+' exp;
 
subexp: exp '-' exp;

multexp: exp '*'  exp;
 
divexp: exp '/' exp;
        
modexp: exp '%' exp;

expexp: exp '^' exp;


letexp: Let  ( '(' Identifier ':' typea ')' )+ exp IN exp;

matchexp: Match exp With ( '|' exp '=>' exp )+;

boolexp: TrueLiteral | FalseLiteral;

callexp: App exp exp;

ifexp: If bexp Then exp Else exp;

lessexp: exp Less exp;

equalexp: exp Equal exp;

greaterexp: exp Greater exp;


andexp: exp '&&'  exp;

orexp: exp '||' exp;


typea: booleantype | funct | numtype | pairtype;

booleantype: 'bool';

numtype: 'num';
        
pairtype: '(' typea ',' typea ')';


funct: '(' typea '->' typea ')';
        
 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase

 App: 'app';
 Then: 'then';
 Else: 'else';
 Let : 'let' ;
 IN : 'in' ;
 Match : 'match' ;
 With : 'with' ;
 //Fun : 'Fun' ;
 If : 'if' ; 
 Car : 'car' ; 
 Cdr : 'cdr' ; 
 Less : '<' ;
 Equal : '=' ;
 Greater : '>' ;
 TrueLiteral : '#t' ;
 FalseLiteral : '#f' ;
// Ref : 'ref' ;
// Deref : 'deref' ;
// Assign : 'set!' ;

 SKIPEXP : 'SKIP';
 Xgate : 'X' ;
 CU : 'CU';
 RZ : 'RZ';
 RRZ : 'RRZ';
 SR : 'SR';
 SRR : 'SRR';
 Lshift : 'Lshift';
 Rshift : 'Rshift';
 Rev : 'Rev';
 QFT : 'QFT';
 RQFT : 'RQFT';
 Seq : ';';
 
 //Free : 'free' ;
 //Fork : 'fork' ;
 //Lock : 'lock' ;
 //UnLock : 'unlock' ;
 //Process : 'process' ;
 //Send : 'send' ;
 //Stop : 'stop' ;

 Dot : '.' ;

 Number : DIGIT+ ;



 Identifier :   Letter LetterOrDigit*;

 Letter :   [a-zA-Z$_]
    |   ~[\u0000-\u00FF\uD800-\uDBFF] 
        {Character.isJavaIdentifierStart(_input.LA(-1))}?
    |   [\uD800-\uDBFF] [\uDC00-\uDFFF] 
        {Character.isJavaIdentifierStart(Character.toCodePoint((char)_input.LA(-2), (char)_input.LA(-1)))}? ;

 LetterOrDigit: [a-zA-Z0-9$_]
    |   ~[\u0000-\u00FF\uD800-\uDBFF] 
        {Character.isJavaIdentifierPart(_input.LA(-1))}?
    |    [\uD800-\uDBFF] [\uDC00-\uDFFF] 
        {Character.isJavaIdentifierPart(Character.toCodePoint((char)_input.LA(-2), (char)_input.LA(-1)))}?;

 fragment DIGIT: ('0'..'9');

 fragment ESCQUOTE : '\\"';
 StrLiteral :   '"' ( ESCQUOTE | ~('\n'|'\r') )*? '"';

 AT : '@';
 ELLIPSIS : '...';
 WS  :  [ \t\r\n\u000C]+ -> skip;
 Comment :   '/*' .*? '*/' -> skip;
 Line_Comment :   '//' ~[\r\n]* -> skip;
