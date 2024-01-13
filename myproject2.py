# Dna analyzer tool 
# length analysis of dna sequence
def find_dna_sequence_length(dna_sequence):
    return len(dna_sequence)

user_dna_sequence = "ATGCATGCGGCGCGCGTATATATGCGCTAGATATGCATGCATGC"
sequence_length = find_dna_sequence_length(user_dna_sequence)
print(sequence_length)



# GC content analyses of input dna sequence 

gc_count = user_dna_sequence.count("G") + user_dna_sequence.count("C")
GC_content = (gc_count/sequence_length)*100
print(GC_content)

# Motif finding in a dna sequence 
import re
def find_motif_in_dna_sequence(dna_sequence, motif):
    motif_positions = [match.start() for match in re.finditer(motif, dna_sequence)]
    return motif_positions
user_dna_sequence = "ATGCATGCGGCGCGCGTATATATGCGCTAGATATGCATGCATGC"
find_motif = find_motif_in_dna_sequence(user_dna_sequence,"ATGC" )
print(find_motif)

# Complementary sequence of given input sequence 

def find_complementary_sequence_in_dna_sequence(dna_sequence):
    dict = {"A":"T", "G":"C", "C":"G","T":"A"}
    complementary_sequence = [dict[base] for base in dna_sequence]
    return ''.join(complementary_sequence)
user_dna_sequence = "ATGCATGCGGCGCGCGTATATATGCGCTAGATATGCATGCATGC"
find_complentary = find_complementary_sequence_in_dna_sequence(user_dna_sequence, )
print(find_complentary)
