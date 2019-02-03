#!/usr/bin/python
'''
Simple program to generate shotgun fragments from a given sequence.
Input: sequence, min length and max length of the fragments 
       and the required coverage
Output: the set of fragments
This is the program we developed in class Jan 24, 2019
'''
import random
# ---------------------------------------------------------
# The function to generate the fragments
# ---------------------------------------------------------
def genfrags(seq, minlen, maxlen, requiredCoverage) :
    n = len(seq)
    coverage = [0 for i in range(n)]
    # -----------------------------------------------------
    # A local function to check if the required coverage is met
    # -----------------------------------------------------
    def covered() :
        for i in range(n) :
            if coverage[i] < requiredCoverage :
                return False
        return True
    # -----------------------------------------------------
    # An empty list to hold the fragments
    # -----------------------------------------------------
    frags = []
    # -----------------------------------------------------
    # A loop to generate random fragments until the coverage is met
    # -----------------------------------------------------
    while not covered() :
        randlen = random.randint(minlen, maxlen)
        start = random.randint(0, n - randlen)
        end = start + randlen
        frag = seq[start : end]
        frags.append(frag)
        # Update the coverage
        for i in range(start, end) :
            coverage[i] += 1
    # -----------------------------------------------------
    # Print the coverage for interest and return the fragments
    # -----------------------------------------------------
    print coverage
    print ('------------------------------------')
    print ('The average is', (float(sum(coverage))/n))
    print ('------------------------------------')
    return frags
# ---------------------------------------------------------
# Try it out on a short sequence of length 80
# ---------------------------------------------------------
seq1 = ['ACTG' for i in range(20)]
list1 = list(seq1) # since we cannot shuffle a string
random.shuffle(list1)
seq1 = ''.join(list1) # going back to the string after shuffling
print seq1
fragments = genfrags(seq1, 15, 20, 3)
print fragments
# ---------------------------------------------------------
# The End
# ---------------------------------------------------------
