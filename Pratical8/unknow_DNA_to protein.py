import os
import re # import package
from itertools import count
from shlex import join


def DNA_to_protein(seq):  # define a function to read and traslate the DNA
    translation_table = {'TTT': 'F',  # input the traslate table from DNA to protein
                         'TTC': 'F',
                         'TTA': 'L',
                         'TTG': 'L',
                         'CTT': 'L',
                         'CTC': 'L',
                         'CTA': 'L',
                         'CTG': 'L',
                         'ATT': 'I',
                         'ATC': 'I',
                         'ATA': 'J',
                         'ATG': 'M',
                         'GTT': 'V',
                         'GTC': 'V',
                         'GTA': 'V',
                         'GTG': 'V',
                         'TCT': 'S',
                         'TCC': 'S',
                         'TCA': 'S',
                         'TCG': 'S',
                         'CCT': 'P',
                         'CCC': 'P',
                         'CCA': 'P',
                         'CCG': 'P',
                         'ACT': 'T',
                         'ACC': 'T',
                         'ACA': 'T',
                         'ACG': 'T',
                         'GCT': 'A',
                         'GCC': 'A',
                         'GCA': 'A',
                         'GCG': 'A',
                         'TAT': 'Y',
                         'TAC': 'Y',
                         'TAA': 'O',
                         'TAG': 'U',
                         'CAT': 'H',
                         'CAC': 'H',
                         'CAA': 'Q',
                         'CAG': 'Z',
                         'AAT': 'N',
                         'AAC': 'B',
                         'AAA': 'K',
                         'AAG': 'K',
                         'GAT': 'D',
                         'GAC': 'D',
                         'GAA': 'E',
                         'GAG': 'E',
                         'TGT': 'C',
                         'TGC': 'C',
                         'TGA': 'X',
                         'TGG': 'W',
                         'CGT': 'R',
                         'CGC': 'R',
                         'CGA': 'R',
                         'CGG': 'R',
                         'AGT': 'S',
                         'AGC': 'S',
                         'AGA': 'R',
                         'AGG': 'R',
                         'GGT': 'G',
                         'GGC': 'G',
                         'GGA': 'G',
                         'GGG': 'G'}
    protein = ''
    for i in range(0, len(seq), 3):  # read the seq every 3 letters
        protein = protein + translation_table[seq[i:i + 3]]  # plus every amino acid one by one

    return protein
os.chdir("D://Desktop")
gene_pool=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
result = open("protein.fa", 'w')
gene = []  # gene seq list of tuple
  # gene length
description = ''  # gene description
gene_name = ''  # gene name
protein_length=0
protein= ''
for line in gene_pool:
        if re.match(">", line):  # judge whether to initialise parameters and output
            if description:  # when meet the result line and parameters are not empty, output
                result.write("{0}\t{1}\n".format(gene_name, str(protein_length)))
                # write the gene name and length with the given form
                for i in protein:  # output seq line by line
                    result.write(i)
                protein = ''
                protein_length = 0
                description = ''
                gene_name = ''

            if re.findall("unknown function", line):  # we don't use elif here to avoid a skip of two neighboring
                # unknowns
                description = line  # if the gene is unknown, description
                gene_name = re.search(r'(>.+?)(?:_| )', line).group(1)  # gene name
                continue
        if re.findall("unknown function", description):
            gene.append(line)
             # count the length of gene, -1 is for \n
            list=[x.strip() for x in gene]
            a=''.join(list)
            protein=DNA_to_protein(a)+'\n'
            protein_length= len(protein.encode('utf-8'))-1
            print (protein)


gene_pool.close()
result.close()
