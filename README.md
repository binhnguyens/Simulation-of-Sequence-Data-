# Simulation-of-Sequence-Data
Computation in Genetic engineer - Repository to understand see how to sequence data with various methods

In this repository, there are various files with the name starting with sim
This repository is done to help and explain the various methods to sequence data.
In each of the files, an arbitrary sequence is created using the line: ['ACTG' for i in range(20)]
That can be replaced by anything you'd like.

# Sim1.py
This file contains various functions such as genfrags and covered.
Genfrags is the function that does the sequencing and covered is a function to help determine the coverage of each gene.
The goal of this file was to simulate something similar to the original DNA sequencing. The method was called Shotgun Sequencing.
The steps go as follow:
1. The fragments were randomly sliced into various fragments
2. The coverage was calculated by recording the position of the nucleobase (coverage is the number of nucleobases counted at one index). This represented the sequencing of the genome
3. This was done until each position covered satisfied the variable "RequireCoverage"

The issues with shot gun method was that the ends of the sequence had a less likely chance of being chosen. This resulted in an average of 20 times the RequireCoverage throughout the sequence.

# Sim1end.py
This file is an abbreviation of the Sim1, instead of taking random positions throughout the sequence, the sequence was focussed on satisfying the coverage in the ends (Beginning and End) before randomly picking from the sequence.

In result, the average coverage of the sequence was about double the RequireCoverage.


# SimCut.py
This file is a method of data sequnecing to represent the new generation of data sequencing. This is an improvement on both the above files.
This method makes three copies of the original sequence (this case it is: ['ACTG' for i in range(20)]. 
The steps of this algorithm is as follows:

1. Take the first copy and cut it
2. This will create two copies named p1 and p2
3. p1 will be between the length required. It will be appnded to the final fragments 
4. p2 will either be too short, too long or just right
5. If p2 is just right, it will be appended to the final fragments
6. If p2 is too short, it will compensate by taking the end of the sequence
7. If p2 is too long, it will be placed back into the to cut function and will be repeated as above

The steps above will be done while counting the coverage.

In result, the coverage average is significantly lower, reducing it to just above the requireCoverage. (In an ideal situation, it would be equal to requireCoverage. Since step 6 requires to compensate, extra sequneces will be added to the final coverage)

