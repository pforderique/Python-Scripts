# Given a string representing a mRNA strand, outputs original DNA strand and protein formed 
# 
# Piero Orderique
# 2 August 2020

#contains the dictionary for converting codons to proteins
codon_dict = {'AUG':'Met', 'AUA':'Ile', 'AUC':'Ile', 'AUU':'Ile', 
              'AGA':'Arg', 'AGG':'Arg', 'AGC':'Ser', 'AGU':'Ser',
              'ACG':'Thr', 'ACA':'Thr', 'ACC':'Thr', 'ACU':'Thr',
              'AAG':'Lys', 'AAA':'Lys', 'AAC':'Asn', 'AAU':'Asn',
              'UUG':'Leu', 'UUA':'Leu', 'UUC':'Phe', 'UUU':'Phe',
              'UGG':'Trp', 'UGA':'Stop','UGC':'Cys', 'UGU':'Cys',
              'UCG':'Ser', 'UCA':'Ser', 'UCC':'Ser', 'UCU':'Ser',
              'UAG':'Stop','UAA':'Stop','UAC':'Tyr', 'UAU':'Tyr',
              'GUG':'Val', 'GUA':'Val', 'GUC':'Val', 'GUU':'Val',
              'GGG':'Gly', 'GGA':'Gly', 'GGC':'Gly', 'GGU':'Gly',
              'GCG':'Ala', 'GCA':'Ala', 'GCC':'Ala', 'GCU':'Ala',
              'GAG':'Glu', 'GAA':'Glu', 'GAC':'Asp', 'GAU':'Asp',
              'CUG':'Leu', 'CUA':'Leu', 'CUG':'Leu', 'CUU':'Leu',
              'CGG':'Arg', 'CGA':'Arg', 'CGC':'Arg', 'CGU':'Arg',
              'CCG':'Pro', 'CCA':'Pro', 'CCC':'Pro', 'CCU':'Pro',
              'CAG':'Gln', 'CAA':'Gln', 'CAC':'His', 'CAU':'His'}

#contains complimentary bases
dna_to_dna ={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
dna_to_rna = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
rna_to_dna = {'A':'T', 'U':'A', 'C':'G', 'G':'C'}

dna_example = "TGGACTACCGGCAATTAGATAAATTCCGGACTTCATTGCATACC"
dna_ex = 'ACCTGATGGCCGTTAATCTATTTAAGGCCTGAAGTAACGTATGG'

def dna_replication(dna, start=5):
    '''
    dna must be a single strand
    start must be either 5 or 3 indicating 5' to 3' or 3' to 5' respectfully (5' is assumed)
        returns one string representing double stranded dna 
    '''
    DNA = ''
    if int(start) == 5:
        DNA += '5\' '+dna+' 3\'\n3\' '
    elif int(start) == 3:
        DNA += '3\' '+dna+' 5\'\n5\' '
    else:
        raise ValueError ('Invalid start parameter. Use either the number 5 or 3.')

    for base in dna:
        DNA += dna_to_dna[base]
    if int(start) == 5: DNA += ' 5\''
    else: DNA += ' 3\''

    return DNA

def transcriptase(dna, start=5):
    '''
    dna must be a single string
    start must be either 5 or 3 indicating 5' to 3' or 3' to 5' respectfully (5' is assumed)
        returns a single mrna strand
    '''
    mrna = ''
    if int(start) == 5:
        DNA += '5\' '+dna+' 3\'\n3\' '
    elif int(start) == 3:
        DNA += '3\' '+dna+' 5\'\n5\' '
    else:
        raise ValueError ('Invalid start parameter. Use either the number 5 or 3.')
    
    pass

def reverse_transcriptase(mrna):
    '''
    mrna strand (single stranded) to be reverse transcribed back into a single stranded dna molecule
    '''
    dnastring = ''
    pass

def mrna_to_protein(mrna):
    if len(mrna) < 3 or 'AUG' not in mrna:
        return 'No Protein'
    protein = ''
    start = mrna.find('AUG')
    for idx in range(start, len(mrna), 3):
        try:
            codon = mrna[idx:idx+3]
        except:
            break
        if codon_dict[codon] != 'Stop':
            protein+= codon_dict[codon]+'-'
        else:
            protein += codon_dict[codon]
            break
    return protein


print(dna_replication(dna_ex))
# print(mrna_to_protein(mrna))

