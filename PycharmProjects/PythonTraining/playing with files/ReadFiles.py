__author__ = 'sabin'

## python class to read files ( txt and .gz)

import gzip, sys

filename = sys.argv[1]


def reading_txtFile(filename):
    txtFile = open(filename, 'r')
    read_txtFile = txtFile.read()
    print " reading the content of the file ..."
    print " content of ", filename, " is : \n", read_txtFile
    txtFile.close()

def reading_gzfile(filename):
    gzFile = gzip.open(filename, 'rb')
    read_gzFile = gzFile.read()
    print " "
    print " reading the content of the gzip file ..."
    print " content of ", filename, " is : \n", read_gzFile
    gzFile.close()

if filename.endswith('.txt'):
 reading_txtFile(filename)
else:
 reading_gzfile(filename)






