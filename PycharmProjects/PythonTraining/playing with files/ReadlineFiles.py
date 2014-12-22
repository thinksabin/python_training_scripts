__author__ = 'sabin'

## reads the number and tell the number of lines in the file.

import gzip, sys
filename = sys.argv[1]

def reading_txtFile(filename):
    txtFile = open(filename, 'r')
    line_number = sum(1 for line in txtFile)
    print " Determining numbers of lines in the file ..."
    print " number of lines in ", filename, " is : \n", line_number
    txtFile.close()

def reading_gzfile(filename):
    gzFile = gzip.open(filename, 'rb')
    line_number = sum(1 for line in gzFile)
    print " "
    print " rDetermining numbers of lines in the file ..."
    print " number of lines in ", filename, " is : \n", line_number
    gzFile.close()


if filename.endswith('.txt'):
 reading_txtFile(filename)
else:
 reading_gzfile(filename)