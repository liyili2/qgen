Input of the program:

    xa: qubit array of length na (CoqNVal),
    ya: qubit array of length na (CoqNVal),
    result: qubit array of length na, initialized to zero (CoqNVal),
    ca: carry qubit register of length one. ca is required to be initialized as zero (CoqNVal),
    na: length of xa, ya, and result (int)

Output of the program:

    xa: unchanged, 
    ya: unchanged,
    result: (xa * ya) % 2^na, 
    ca: unchanged, 
    na: unchanged

xa and ya and re have the same length of na
If the values of xa (ya) is greater than 2^na, than it will be reduced to xa % 2^na (ya % 2^na).
