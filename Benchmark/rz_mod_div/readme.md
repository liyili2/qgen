TODO: is _i_ related to m or n?

Input of the program:

    x: Qubit array of length na (CoqNVal),
    ex: Qubit array of length na, initialized as zeroes (CoqNVal)
    na: Natural number representing the length of x and ex (int)
    m: Modulo divisor, natural number (int)
    i: Natural number related to m, such that 2^{n−1} ≤ 2^i <2^n (int)

Output of the program:

    x: old(x) % m (CoqNVal)
    ex: old(x)/m  natural number division (int)
    na: Unchanged
    m: Unchanged
    i: Unchanged

<pexp gate = 'QFT' > <id> x </id> <vexp> 0 </vexp> </pexp> 
< app > <id> f </id> <vexp op = 'plus' > <id> i </id> <vexp> 1 </vexp> <id> x </id> <id> ex </id> <id> na </id> <id> m </id> </app> 
<pexp gate = 'RQFT' > <id> x </id> </pexp>
