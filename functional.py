def partition(my_list, chunk_size, fn=lambda:None):
    for i in (range(len(my_list) - chunk_size)):
        yield fn(my_list[i : i+chunk_size])

def frequencies(my_list):
    counts = {}
    for current in my_list:
        counts[current] = counts.get(current, 0) + 1
    return counts
