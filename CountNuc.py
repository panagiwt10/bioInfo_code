def countNucFreq(seq):
     tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
     for nuc in seq:
         tmpFreqDict[nuc] += 1
     return tmpFreqDict


DNAString = "GGAAGACCTTAGTCGCCCACGTGCCTATAAGAAGTGAAAACGAGCAGCTGGGGTCCATGCCAGCCAACCTCTTACGAGTTGGACAGACCGCCAAAAGCCTCTCCTCTTGATCTGGAACACTTCTCAGATAGAAACGTGGTTACGTTGAAGCCTGCATTGGGTTATGTGGTATACTGTAGTCATTGACCTAATCACAACCGAGGTCGCAACTGTGCAACGAAAAAGCTACATTACCATCATTTTACACCGGTTAGATCCCGCATAGCTGAATTTATAGTAATGCCTCGGCCTTACTGGGCACGATCGTGGACTGCCCGAGACTGGAATACTTACTGTCGTGTCAGGCATGGAGGTCTCTAGCCGTCCAGGCGTGTAAAGGCATGCCCAAGCGTCCACCTTTTCTTCTGGAACGCCCGGTTGCAGAAGCGTAAGGCACTACGACAGGTCATCGTAACGTCTGGTACGACAAGGAGGAGTCCAACTATGGATTGAGTGGCATCCCACGTATGCAGTACTTTTGGAGCCGTGATGGCCAGACTACAATAAAGAGGGCGAGCGTTAACTAGAGCTCTCTGATCTGTGGCGGAACATATTAGTACGGGGCGGGTTGGAAGCTGCCCCCCCTAAACACAATGGACCTCAAGATGCCTGTCACAACAATCAACTCATCCGGTCAGCATGTGGTTGCGCTACGAAGATCTGTTAGGCGTTCGAATGGCTGACCAGGGAATTGCTTGTGTTTAATGCGAGAGGGAGGGATTGTAACCCTTGACAACAATCTCTCACAACTGTCTGCTCGAGCTGTGCCCATACCACACGTCCGATGGCTGTGTGAATTTGTGGAAGACCTTGTGCCTCAGTCGCCGGAGCCTTGGCCTCACGACCGGTGTTCAATA"
result = countNucFreq(DNAString)
print(' '.join([f"{key}:{val}" for key, val in result.items()]))

#εδω ουσιαστικα εκτυπωνεις απο το dnaString
#σε μορφη πινακα τα Α T G C αναλογα ποσα ειναι στην ακολουθια  