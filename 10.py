from codontab import STD_RNA_CODON_TAB
from functional import frequencies

if __name__ == '__main__':
    with open('data/10.dat', 'r') as data_file:
        protein_string = data_file.readline().strip() + '*'
        aa_counts = frequencies(STD_RNA_CODON_TAB.values())

        possible_rna_string_ct = 1
        for char in protein_string:
            possible_rna_string_ct *= aa_counts[char]
            possible_rna_string_ct %= 1000000

        print possible_rna_string_ct


