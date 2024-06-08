Input of the program:

    x: Qubit array of length na (CoqNVal)
    na: Natural number representing the length of x (int)
    m: Natural to subtract from x (int)

Output of the program:

    x: (old(x) − m) % 2^na, where % is natural number modulo, e.g., 7−9 mod 2^4 =14 
    na: Unchanged
    m: Unchanged
    
    
//  Fixpoint f (x:var) (n:nat) (size:nat) (M: nat -> bool) :=
//  match n with 
//  | 0 => SKIP (x,0)
//  | S m => f x m size M ; if M m then SRR (size - n) x else SKIP (x,m)
//  end.
//sub, subtracting natural number n to qubit array x
// main: QFT x 0; f x n size M; RQFT x
//SRR i x means SR (-i) x, 
//spec: x -> (x+m) % (2^na),  the subtrahend is natural number modulo, meaning that no negative number will be produce. 1 - 10 in a four bit situation will be -9+16 = 7
