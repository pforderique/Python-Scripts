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

#contains complimentary bases from mrna to dna (reverse transcriptase)
comp_base = {'A':'T', 'U':'A', 'C':'G', 'G':'C'}

mrna = "AUGCAUAUACAC"

def reverseTranscriptase(mrna):
    pass