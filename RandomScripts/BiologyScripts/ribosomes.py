rnaToAminoAcid = {
    "UUU":"Phenylalanine", "UUC":"Phenylalanine", "UUA":"Leucine", 
    "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine",
    "UAU":"Tyrosine", "UAC":"Tyrosine", "UAA":"STOP", "UAG":"STOP",
    "UGU":"Cysteine", "UGC":"Cysteine", "UGA":"STOP", "UGG":"Tryptophan",
    "CUU":"Leucine", "CUC":"Leucine", "CUA":"Leucine", "CUG":"Leucine",
    "CCU":"Proline", "CCC":"Proline", "CCA":"Proline", "CCG":"Proline",
    "CAU":"Histidine", "CAC":"Histidine", "CAA":"Glutamine", "CAG":"Glutamine",
    "CGU":"Arginine", "CGC":"Arginine", "CGA":"Arginine", "CGG":"Arginine",
    "AUU":"Isoleucine", "AUC":"Isoleucine", "AUA":"Isoleucine", "AUG":"Methionine",
    "ACU":"Threonine", "ACC":"Threonine", "ACA":"Threonine", "ACG":"Threonine",
    "AAU":"Asparagine", "AAC":"Asparagine", "AAA":"Lysine", "AAG":"Lysine",
    "AGU":"Serine", "AGC":"Serine", "AGA":"Arginine", "AGG":"Arginine",
    "GUU":"Valine", "GUC":"Valine", "GUA":"Valine", "GUG":"Valine",
    "GCU":"Alanine", "GCC":"Alanine", "GCA":"Alanine", "GCG":"Alanine",
    "GAU":"Aspartic Acid", "GAC":"Aspartic Acid", "GAA":"Glutamic Acid", 
    "GAG":"Glutamic Acid", "UUG":"Leucine",
    "GGU":"Glycine", "GGC":"Glycine", "GGA":"Glycine", "GGG":"Glycine",
    }

def ribosomeSM0(input):
    protein = []
    
    # iterate until find AUG -- start at idx 2
    curr_idx = 0
    for idx in range(0, len(input)-2):
        base = input[idx]
        # check if its a G
        if base == 'G' and input[idx + 1] == 'U' and input[idx + 2] == 'G':
            # break! start counting by 3
            curr_idx = idx
            break
        else:
            protein.append(None)
        curr_idx += 1 
        
    # we found out start codon. Start iterating by threes AUG
    # point it back to the start of the codon
    for idx in range(curr_idx, len(input), 3):
        if idx + 2 < len(input): 
            codon = input[idx : idx + 3]
            amino_acid = rnaToAminoAcid[codon]

            # only append if not a terminating codon
            if amino_acid == 'STOP':
                curr_idx = idx + 3 # update our current index
                break
            else:
                protein.append(amino_acid)
        else:
            curr_idx = idx
            break
            #protein.extend([None for i in range(len(input)-idx)])
            #return protein
            
    # finish off what is left
    for idx in range(curr_idx, len(input)):
        protein.append(None)
        
    return protein
        
def ribosomeSM(input):
    protein = [None, None]
    
    # iterate until find AUG -- start at idx 2
    curr_idx = 2
    for idx in range(2, len(input)):
        base = input[idx]
        # check if its a G --> then check if we hit the AUG start codon
        if base == 'G' and input[idx - 1] == 'U' and input[idx - 2] == 'A':
                # break! start counting by 3
                break
        else:
            protein.append(None)
        curr_idx += 1 
        
    # we found out start codon. Start iterating by threes AUG
    curr_idx -= 2 # point it back to the start of the codon
    for idx in range(curr_idx, len(input), 3):
        if idx + 2 < len(input): 
            codon = input[idx : idx + 3]
            amino_acid = rnaToAminoAcid[codon]

            # only append if not a terminating codon
            if amino_acid == 'STOP':
                curr_idx = idx + 3 # update our current index
                break
            else:
                protein.append(amino_acid)
        else:
            curr_idx = idx
            break

    nones = [None for i in range(curr_idx, len(input))]
    protein.extend(nones)

    return protein

def ribosomeSM_REAL(input):
    protein = [None, None]
    
    # iterate until find AUG -- start at idx 2
    curr_idx = 2
    for idx in range(2, len(input)):
        base = input[idx]
        # check if its a G
        if base == 'G' and input[idx - 1] == 'U' and input[idx - 2] == 'A':
                # break! start counting by 3
                break
        else:
            protein.append(None)
        curr_idx += 1 
        
    # we found out start codon. Start iterating by threes AUG
    curr_idx -= 2 # point it back to the start of the codon
    for idx in range(curr_idx, len(input), 3):
        if idx + 2 < len(input): 
            codon = input[idx : idx + 3]
            amino_acid = rnaToAminoAcid[codon]

            # only append if not a terminating codon
            if amino_acid == 'STOP':
                curr_idx = idx + 3 # update our current index
                break
            else:
                protein.append(amino_acid)
        else:
            curr_idx = idx
            break

    nones = [None for i in range(curr_idx, len(input))]
    protein.extend(nones)

    return protein


def ribosomeSM2(input):
    state = 'PRE-STATE' # PRE-STATE, TRIPLE, POST-STATE
    idx = 0
    protein = []

    while idx < len(input):
        
        # read in char by char
        if state == 'PRE-STATE':
            char = input[idx]
            print(char, idx)

            # if we encounter a G, check if there are chars behind us and if this is AUG
            if char == 'G' and idx >= 2 and input[idx-1] == 'U' and input[idx-2] == 'A':
                # we found the start! go back to the start of AUG and start counting by 3 (TRIPE STATE)
                idx = idx - 2
                state = 'TRIPLE'
                continue
        
            else:
                protein.append(None)
                idx += 1
                continue

        # read in 3 by 3
        elif state == 'TRIPLE':
            # first check if we are NOT in bounds!
            if idx + 2 >= len(input):
                # no codons left. go to post state and stay at this nucleotide
                state = 'POST-STATE'
                continue
            # else read in that codon and translate!
            else:
                codon = input[idx : idx + 3]
                amino_acid = rnaToAminoAcid[codon]
                # check if we hit the stop!
                if amino_acid == 'STOP':
                    # go to POST-STATE
                    idx += 2
                    state = 'POST-STATE'
                    continue
                else:
                    # append new amino acid!
                    protein.append(amino_acid)
                    idx += 3
                    continue
        
        # read in last nucleotides one by one!
        elif state == 'POST-STATE':
            protein.append(None)
            idx += 1
            continue

    return protein

strand = 'ACCGGUCGCCACCAUGGUGAGCAAGGGCGAGGAGCUGUAGCCGGACGUAACGUU'
print(ribosomeSM2(strand))