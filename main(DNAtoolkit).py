from DNAtoolkit import * 
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(20)]) 


print(validateSeq(randDNAStr))
print(countNucFreq(randDNAStr))

