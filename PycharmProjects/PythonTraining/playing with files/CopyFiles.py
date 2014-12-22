__author__ = 'sabin'

## program to copy the files ( .txt and .gz)

import gzip, sys

filename = sys.argv[1]
newfilename = sys.argv[2]

read_txtFile = ''
def reading_txtFile(filename):
    txtFile = open(filename, 'r')
    read_txtFile = txtFile.read()
    return  read_txtFile

def maketxtFile(newfilename, w):
    new_txtFile = open(newfilename, 'w+')
    writeFile   = new_txtFile.write(w)
    new_txtFile.close()
    print('new copy file named: '), newfilename, ' has been created.'

def reading_gzFile(filename):
    gzFile = gzip.open(filename,'r')
    read_gzFile = gzFile.read()
    return read_gzFile


def makegzFile(newfilename, w):
    new_gzFile = gzip.open(newfilename, 'w+')
    write = new_gzFile.write(w)
    new_gzFile.close()
    print('new copy file named: '), newfilename, ' has been created.'

if filename.endswith('.txt') and newfilename.endswith('.txt'):
    w = reading_txtFile(filename)
    maketxtFile(newfilename, w)
elif filename.endswith('.gz') and newfilename.endswith('.gz'):
    w =reading_gzFile(filename)
    makegzFile(newfilename,w)
elif filename.endswith('.txt') and newfilename.endswith('.gz'):
    w = reading_txtFile(filename)
    makegzFile(newfilename,w)
elif filename.endswith('.gz') and newfilename.endswith('.txt'):
    w = reading_gzFile(filename)
    maketxtFile(newfilename,w)
else:
    print('Error: check File extensions to copy and make')







