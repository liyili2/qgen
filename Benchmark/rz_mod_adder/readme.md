Input of the program:

    x: qubit array of length na (CoqNVal),
    na: Natural number representing the length of x (int) 
    c: qubits array of length one, used as carry register. c must be initialized to zero (CoqNVal),
    a: addend to be added to x (int), 
    m : modulo divisor (int)

Output of the program:
    
    x: (old(x) + a) % m,
    c: unchanged,
    na: unchanged,
    a: unchanged,
    m : unchanged 
