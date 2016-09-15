def print_alphabet_tree(order, length, string=''):
    if length == 0:
        print string
    else:
        for char in order:
            print_alphabet_tree(order, length-1, string + char)

if __name__ == "__main__":
    with open("data/13.dat", 'r') as data_file:
        order, size = data_file.readline().strip().split(' '), int(data_file.readline().strip())

        print_alphabet_tree(order, size)

