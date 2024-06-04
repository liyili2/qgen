Input of the program:

xa: qubit array of length na to be added to ya (CoqNVal),
ya: qubit array of length na (CoqNVal), 
ca: qubit array of length 1, initialized as 0 (CoqNVal),
na: Natural number representing the length of xa and ya (int)

Output of the program:

xa: unchanged, 
ya: (xa + ya) % 2^na (modified in place),
ca: unchanged, 
na: unchanged

xa and ya have the same length
