import os
import re

# import the package
os.chdir("D://Desktop")
cDNA = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r')
result = open("unknown_function.fa", 'w')
# name the parameters
gene = []  # gene seq list of tuple
gene_length = 0  # gene length
description = ''  # gene description
gene_name = ''  # gene name
for line in cDNA:
    if re.match(">", line):  # judge whether to initialise parameters and output
        if description:  # when meet the result line and parameters are not empty, output
            result.write("{0}\t{1}\n".format(gene_name, str(gene_length)))
            # write the gene name and length with the given form
            for i in gene:  # output seq line by line
                result.write(i)
            gene = []
            gene_length = 0
            description = ''
            gene_name = ''
        if re.findall("unknown function", line):  # we don't use elif here to avoid a skip of two neighboring
            # unknowns
            description = line  # if the gene is unknown, description
            gene_name = re.search(r'(>.+?)(?:_| )', line).group(1)  # gene name
            continue
    if re.findall("unknown function", description):
        gene.append(line)
        gene_length = gene_length + len(line) - 1  # count the length of gene, -1 is for \n
result.close()
cDNA.close()
