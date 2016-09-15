def find_last(my_list, term):
    if term in my_list:
        return (len(my_list) - 1) - my_list[::-1].index(term)
    else:
        return -1
