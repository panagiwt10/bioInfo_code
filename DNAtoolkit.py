import collections
from sequences import *

Nucleotides = ["A", "C", "G", "T"]
DNA_ReverseComplement = {'A': 'T','G':'C','C':'G','T':'A','G':'C'}
import random

Nucleotides = ["A", "C", "G", "T"]


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
           return False
    return tmpseq
    

def countNucFreq(seq):
     tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
     for nuc in seq:
         tmpFreqDict[nuc] +=1
     return tmpFreqDict

    
<<<<<<< HEAD
def transcribeDNAtoRNA(seq):
    return seq.replace("T","U")

def reverseComplement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
=======
>>>>>>> 8300e62a731d35babf71972358f51d4df94f2440
