from CountNuc import DNAString
from DNAtoolkit import * 
import random
from sequences import *
from utilities import colored

randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(20)]) 


print(validateSeq((randDNAStr)))
print(countNucFreq(randDNAStr))

print(f"Trancripted RNA:\n5'{transcribeDNAtoRNA(randDNAStr)}3' ")
print("\n")
print(f"DNA string +Reverse Complement:\n5'{randDNAStr} 3'")
print(f"  {''.join(['|'for c in range(len(randDNAStr))])}")
print(f"3'{reverseComplement (randDNAStr)} 5'\n")
