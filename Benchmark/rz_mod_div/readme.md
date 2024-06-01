input of the program:

x: qubits(na), ex: qubits(ex) (require to be zero), na: nat, m:nat, i:nat (requires to be related to m, such that 2^{n-1} <= 2^i < 2^n)

ouptu of the program:

x: old(x) % m, ex: old(x) / m (nat number division), na: same, m : same, i:same


<pexp gate = 'QFT' > <id> x </id> <vexp> 0 </vexp> </pexp> 
< app > <id> f </id> <vexp op = 'plus' > <id> i </id> <vexp> 1 </vexp> <id> x </id> <id> ex </id> <id> na </id> <id> m </id> </app> 
<pexp gate = 'RQFT' > <id> x </id> </pexp>
