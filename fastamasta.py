class FastaReader():
    def __init__(self, filename):
        self._handle = open(filename, 'r')
        self._header, self._seq = '', ''

    def readnext(self):
        self._seq = ''
        header_line = self._handle.readline().strip()

        if header_line == '':
            return None

        self._header = header_line[1::]
        while True:
            orig_file_loc = self._handle.tell()
            part_seq = self._handle.readline().strip()

            if part_seq == '':
                break

            if part_seq.startswith('>'):
                    self._handle.seek(orig_file_loc)
                    break
            self._seq += part_seq

        return self._header, self._seq
