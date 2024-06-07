Input of the program:

    x: qubit array of length n+1 (CoqNVal),
    n: natural number (int)

Output of the program:

    x: x[0], x[0] xor x[1], ... , x[0] xor x[1] xor ... xor x[n-1], 
    n: unchanged

Where x[0], x[0] xor x[1], ... , x[0] xor x[1] xor ... xor x[n-1] means a list of qubit x from 0-th position to n-1 th position.
