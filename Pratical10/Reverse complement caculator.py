def Reverse_complement_caculator(dna):
    #define a function to output the reverse sequence
    reverse_dna = [] # define the list of the reverse sequence
    for i in dna:
        if i == 'A':
            reverse_dna .append('T')
        elif i == 'T:':
            reverse_dna .append('A')
        elif i == 'C':
            reverse_dna .append('G')
        elif i == 'a':
             reverse_dna.append('T')
        elif i == 't:':
             reverse_dna.append('A')
        elif i == 'c':
             reverse_dna.append('G')
        elif i == 'g':
            reverse_dna.append('C')
        else:
            reverse_dna .append('C')
            # For every base of the origin DNA 'ATGC' and 'atgc' to transform
    reverse_dna = reverse_dna[::-1] # reverse the order of result
    reverse_DNA=''.join(reverse_dna) # transform list to str
    return reverse_DNA
dna_input = input('What is the origin DNA sequence?>>>') #Let user to input the origin DNA
print (Reverse_complement_caculator(dna_input)) # print the result
#example
#What is the origin DNA sequence?>>>AtgcaGatC(AtgcaGatC is the input data
#GCTCTGCCT(It is the result)







