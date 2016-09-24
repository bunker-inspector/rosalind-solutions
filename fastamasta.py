import urllib2

class FastaReader():
    def __init__(self):
	self._header, self._seq = '', ''

    def __init__(self, filename):
        self._handle = open(filename, 'r')
        self._header, self._seq = '', ''

    def __iter__(self):
        orig_file_loc = self._handle.tell()
        self._handle.seek(0)

        while self.readnext():
            yield self.data()

        self._handle.seek(orig_file_loc)

    def __dict__(self):
        result = {}
        for record in self:
            result[record[0]] = record[1]
        return result

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

    def data(self):
        return self._header, self._seq

    def to_dict(self):
        return dict(self)

    def open(self, filename):
	self._handle = open(filename, 'r')

    def close(self):
	self._handle.close()

def parse_http_fasta(uri):
    return map(lambda line: (line[:line.find('\n')], line[line.find('\n'):].replace('\n', '')), urllib2.urlopen(uri).read().split('\n>'))


