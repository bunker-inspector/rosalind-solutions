from masstab import MASS_TABLE

if __name__ == '__main__':
    with open('data/10.dat', 'r') as data_file:
        protein_string = data_file.readline().strip()

        weight = 0.0
        for char in protein_string:
            weight += MASS_TABLE[char]

        print round(weight, 3)
