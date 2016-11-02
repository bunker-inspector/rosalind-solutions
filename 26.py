import urllib2
import sys

if __name__ == "__main__":
    dbdata = urllib2.urlopen('http://www.uniprot.org/uniprot/' + sys.argv[1].strip() + '.txt').read()

    for line in map(lambda line: line[4:], dbdata.split('\n')):
        if "P:" in line:
            sub = line[line.find("P:"):]
            print sub[2:sub.find(';')]
