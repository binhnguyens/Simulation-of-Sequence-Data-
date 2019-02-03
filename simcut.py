#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:04:32 2019

@author: binhnguyen
"""
import random
#Importing genfrags - a function created that is similar to the sim1end

print ('--------------------------------------')
print ('Lab 3 Part 2')
print ('--------------------------------------')

#Arbitrary numbers to choose 
seq = ['ACTG' for i in range(20)]
list1 = list(seq) # since we cannot shuffle a string
random.shuffle(list1)
seq = ''.join(list1) # going back to the string after shuffling

#seq = 'ATGCTGA'

requiredCoverage =3 
minlen = 15
maxlen =20


#Part A
tocut = [seq]*requiredCoverage
coverage = [0 for i in range(len(seq))]

print tocut

#Part B
start = 0
n = len (tocut)
p1 = ['']
p2 = ['']
frags = []


while (tocut):
    seqanalysis = tocut.pop()
    rand = random.randint(minlen, maxlen)
    
    p1 =seqanalysis [0:rand]    
    p2 =seqanalysis [rand:len(seq)]
    
    # Update the coverage
    for i in range(start, start+rand):
        coverage[i] += 1
        
    # Print out the pieces
    print 'p1',p1
    print 'p2',p2
    
    
    #Part B
    if len(p2) <= minlen :
        #Make the p2 part be to the latter part of the sequence 
        #(fill up p2 to make it min length)
        p2 = seqanalysis [len(seqanalysis)-minlen:len(seqanalysis)]
        frags.append (p2)
        
        print ('-------Min length route\n')
         # Update the coverage
        for i in range(start + len(seqanalysis)-minlen,start + len(seqanalysis)):
            coverage[i] += 1

    #Part C
    frags.append (p1)    
    if len(p2) >= maxlen :
        tocut.append(p2)
        start += rand
        print ('******Append P2 to cut\n')
    
    else:
        start = 0
        

    
#Part D
print ('----------------------------------')
print frags
print coverage
#z = genfrags.genfrags (seq, minlen, maxlen, requiredCoverage)


    










