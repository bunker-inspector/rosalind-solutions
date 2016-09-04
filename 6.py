from fastamasta import FastaReader
from functional import frequencies

if __name__ == '__main__':
    fr = FastaReader('data/6.fas')
    hi_gc_content = ('', 0.0)

    while True:
        current = fr.readnext()

        if current == None:
            break

        sym_count = frequencies(current[1])
        curr_gc_content = float(sym_count['C'] + sym_count['G']) / float(len(current[1]))

        if curr_gc_content > hi_gc_content[1]:
            hi_gc_content = (current[0], curr_gc_content)

print hi_gc_content[0]
print round(hi_gc_content[1]*100, 6)
