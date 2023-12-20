grammar Exp;

 program returns [Exp ast]:        
        e=exp { $ast = $e.ast; } 
        ;
        
        
vexp returns [VExp ast]:
        va=varexp { $ast = $va.ast; }
        | num=numexp { $ast = $num.ast; }
        | bl=boolexp { $ast = $bl.ast; }
        | add=addexp { $ast = $add.ast; }
        | sub=subexp { $ast = $sub.ast; }
        | mul=multexp { $ast = $mul.ast; }
        | div=divexp { $ast = $div.ast; }
        | mod=modexp { $ast = $mod.ast; }
        | expa=expexp { $ast = $expa.ast; }
        ;

bexp returns [BExp ast]:
         less=lessexp { $ast = $less.ast; }
        | eq=equalexp { $ast = $eq.ast; }
        | gt=greaterexp { $ast = $gt.ast; }
        | anda=andexp { $ast = $anda.ast; }
        | ora=orexp { $ast = $ora.ast; }
        ;        
        
        
posi returns [PosiExp ast]:
        posii=posiexp {$ast = $posii.ast;};
        
exp returns [Exp ast]: 
          let=letexp { $ast = $let.ast; }
        | lam=lambdaexp { $ast = $lam.ast; }
        | call=callexp { $ast = $call.ast; }
        | i=ifexp { $ast = $i.ast; }
 //       | lrec=letrecexp { $ast = $lrec.ast; }
        | skipa=skipexp {$ast = $skipa.ast;}
        | xgate=xgexp {$ast = $xgate.ast;}
        | cu=cuexp {$ast = cu.ast;}
        | rz=rzexp {$ast = rz.ast;}
        | rrz=rrzexp {$ast = rrz.ast;}
        | sr=srexp {$ast = sr.ast;}
        | srr=srrexp {$ast = srr.ast;}
        | lshift=lshiftexp {$ast = lshift.ast;}
        | rshift=rshiftexp {$ast = rshift.ast;}
        | rev=revexp {$ast = rev.ast;}
        | qft=qftexp {$ast = qft.ast;}
        | rqft=rqftexp {$ast = rqft.ast;}
        | seq=seqexp {$ast = seq.ast;} 
 
      //  | ref=refexp { $ast = $ref.ast; }
     //   | deref=derefexp { $ast = $deref.ast; }
    //    | assign=assignexp { $ast = $assign.ast; }
  //      | free=freeexp { $ast = $free.ast; }
        ;



 skipexp returns [SkipExp ast] :
        SKIPEXP e1=posiexp { $ast = new SkipExp(e1); }
        ;
        


 posiexp returns [PosiExp ast] :
        '(' e1=vexp
        ',' 
            e2=vexp 
        ')' { $ast = new PosiExp($e1.ast,$e2.ast); }
        ;
 xgexp returns [XExp ast]:
       Xgate e = posiexp {$ast = new XExp($e.ast)} ;
       
       
       

 cuexp returns [CUExp ast]:
       CU e1=posiexp e2=exp {$ast = new CUExp($e1.ast, $e2.ast)} ;
       
       

 rzexp returns [RZExp ast]:
       RZ e1=vexp e2=exp {$ast = new RZExp($e1.ast, $e2.ast)} ;
       

 rrzexp returns [RRZExp ast]:
       RRZ e1=vexp e2=exp {$ast = new RRZExp($e1.ast, $e2.ast)} ;
       

 srexp returns [SRExp ast]:
       SR e1=vexp e2=exp {$ast = new SRExp($e1.ast, $e2.ast)} ;
       
 srrexp returns [SRRExp ast]:
       SRR e1=vexp e2=exp {$ast = new SRRExp($e1.ast, $e2.ast)} ;

 lshiftexp returns [LshExp ast]:
       Lshift e1=vexp {$ast = new LshExp($e1.ast)} ;


 rshiftexp returns [RshExp ast]:
       Rshift e1=vexp {$ast = new RshExp($e1.ast)} ;

 revexp returns [RevExp ast]:
       Rev e1=vexp {$ast = new RevExp($e1.ast)} ;

 qftexp returns [QFTExp ast]:
       QFT e1=vexp e2=vexp {$ast = new QFTExp($e1.ast, $e2.ast)} ;
       

 rqftexp returns [QFTExp ast]:
       RQFT e1=vexp e2=vexp {$ast = new RQFTExp($e1.ast, $e2.ast)} ;

 seqexp returns [SeqExp ast]:
      Seq e1=exp e2=exp {$ast = new SeqExp($e1.ast, $e2.ast)} ;
                                            
 numexp returns [NumExp ast]:
        n0=Number { $ast = new NumExp(Integer.parseInt($n0.text)); } 
        | '-' n0=Number { $ast = new NumExp(-Integer.parseInt($n0.text)); }
        | n0=Number Dot n1=Number { $ast = new NumExp(Double.parseDouble($n0.text+"."+$n1.text)); }
        | '-' n0=Number Dot n1=Number { $ast = new NumExp(Double.parseDouble("-" + $n0.text+"."+$n1.text)); }
        ;       
  
 addexp returns [AddExp ast]
        locals [ArrayList<Exp> list]
        @init { $list = new ArrayList<Exp>(); } :
        '(' '+'
            e=exp { $list.add($e.ast); } 
            e=exp { $list.add($e.ast); }
        ')' { $ast = new AddExp($list); }
        ;
 
 subexp returns [SubExp ast]  
        locals [ArrayList<Exp> list]
        @init { $list = new ArrayList<Exp>(); } :
        '(' '-'
            e=exp { $list.add($e.ast); } 
            ( e=exp { $list.add($e.ast); } )?
        ')' { $ast = new SubExp($list); }
        ;

 multexp returns [MultExp ast] 
        locals [ArrayList<Exp> list]
        @init { $list = new ArrayList<Exp>(); } :
        '(' '*'
            e=exp { $list.add($e.ast); } 
            e=exp { $list.add($e.ast); }
        ')' { $ast = new MultExp($list); }
        ;
 
 divexp returns [DivExp ast] 
        locals [ArrayList<Exp> list]
        @init { $list = new ArrayList<Exp>(); } :
        '(' '/'
            e=exp { $list.add($e.ast); } 
            e=exp { $list.add($e.ast); } 
        ')' { $ast = new DivExp($list); }
        ;
        
 modexp returns [ModExp ast] 
        locals [ArrayList<Exp> list]
        @init { $list = new ArrayList<Exp>(); } :
        '(' '%'
            e=exp { $list.add($e.ast); } 
            e=exp { $list.add($e.ast); } 
        ')' { $ast = new ModExp($list); }
        ;

 expexp returns [ExpExp ast] 
        locals [ArrayList<Exp> list]
        @init { $list = new ArrayList<Exp>(); } :
        '(' '^'
            e=exp { $list.add($e.ast); } 
            e=exp { $list.add($e.ast); } 
        ')' { $ast = new ExpExp($list); }
        ;
        
 varexp returns [VarExp ast]: 
        ida=Identifier { $ast = new VarExp($ida.text); }
        ;

 letexp  returns [LetExp ast] 
        locals [ArrayList<String> names, ArrayList<Type> types, ArrayList<Exp> value_exps]
        @init { $names = new ArrayList<String>(); $types=new ArrayList<Type>(); $value_exps = new ArrayList<Exp>(); } :
        Let 
            '(' ( '(' ida=Identifier ':' t=typea e=exp ')' { $names.add($ida.text);$types.add($t.ast); $value_exps.add($e.ast); } )  ')'
            body=exp 
        { $ast = new LetExp($names, $types, $value_exps, $body.ast); }
;
        

 //strexp returns [StrExp ast] :
 //       s=StrLiteral { $ast = new StrExp($s.text); } 
  //      ;

 boolexp returns [BoolExp ast] :
        TrueLiteral { $ast = new BoolExp(true); } 
        | FalseLiteral { $ast = new BoolExp(false); } 
        ;



  lambdaexp returns [LambdaExp ast] 
        locals [ArrayList<String> formals, ArrayList<Type> types  ]
        @init { $formals = new ArrayList<String>(); $types = new ArrayList<Type>(); } :
        Fun 
        '(' (ida=Identifier ':' ty=typea { $formals.add($ida.text); $types.add($ty.ast); } )* ')'
            body=exp
        {$ast = new LambdaExp($formals, $types, $body.ast); }
        ;

 callexp returns [CallExp ast] 
        locals [ArrayList<Exp> arguments = new ArrayList<Exp>();  ] :
        '(' f=exp 
            ( e=exp { $arguments.add($e.ast); } )
        ')' { $ast = new CallExp($f.ast,$arguments); }
        ;

 ifexp returns [IfExp ast] :
        '(' If 
            e1=bexp 
            e2=exp 
            e3=exp 
        ')' { $ast = new IfExp($e1.ast,$e2.ast,$e3.ast); }
        ;

 lessexp returns [LessExp ast] :
        '(' Less 
            e1=exp 
            e2=exp 
        ')' { $ast = new LessExp($e1.ast,$e2.ast); }
        ;

 equalexp returns [EqualExp ast] :
        '(' Equal 
            e1=exp 
            e2=exp 
        ')' { $ast = new EqualExp($e1.ast,$e2.ast); }
        ;

 greaterexp returns [GreaterExp ast] :
        '(' Greater 
            e1=exp 
            e2=exp 
        ')' { $ast = new GreaterExp($e1.ast,$e2.ast); }
        ;

 andexp returns [AndExp ast] :
        '(' '&&' 
            e1=exp 
            e2=exp 
        ')' { $ast = new LessExp($e1.ast,$e2.ast); }
        ;

 orexp returns [OrExp ast] :
        '(' '||' 
            e1=exp 
            e2=exp 
        ')' { $ast = new EqualExp($e1.ast,$e2.ast); }
        ;


typea returns [Type ast]: 
        b=booleantype { $ast = $b.ast; }
        |f=funct  { $ast = $f.ast; }
        |n=numtype { $ast = $n.ast; }
        |p=pairtype { $ast = $p.ast; }
        ;

booleantype returns [BoolT ast] :
        'bool' { $ast = new BoolT(); }
        ;

numtype returns [NumT ast] :
        'num' { $ast = new NumT(); }
        ;
        
pairtype returns [PairT ast] :
        '(' fst = typea ',' snd= typea ')' { $ast = new PairT($fst.ast, $snd.ast); }
        ;

 funct returns [FuncT ast] 
        locals [ArrayList<Type> formals]
        @init { $formals = new ArrayList<Type>(); } :
        '('  
             (e=typea { $formals.add($e.ast);} )* '->' ret=typea 
        ')' { $ast = new FuncT($formals, $ret.ast); }
        ;
        
 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase

 Let : 'let' ;
 Letrec : 'letrec' ;
 Fun : 'Fun' ;
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
