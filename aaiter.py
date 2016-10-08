def codons(seq):
    for i in range(0, len(seq), 3):
        yield seq[i:i+3]

def find_orfs(seq):
    frame_a = [i for i in codons(seq)]
    frame_b = [i for i in codons(seq[1:-2])]
    frame_c = [i for i in codons(seq[2:-1])]

    frames = [frame_a, frame_b, frame_c]

    orfs = []
    offset = 0
    for frame in frames:
        starts = []
        stops  = []
        for i in range(len(frame)):
            #if it's the start codon
            if frame[i] == 'ATG':
                starts.append(i)
            #if it's a stop codo
            elif frame[i] in ['TAA','TGA','TAG']:
                stops.append(i)
        for start in starts:
            for stop in stops:
                if start < stop:
                    orfs.append((3*start + offset, 3*(stop+1) + offset))
                    break
        offset += 1
    return orfs

