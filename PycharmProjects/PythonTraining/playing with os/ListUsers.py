__author__ = 'sabin'
#Print the list of all users that can log into the computer.

import os, exceptions

no_bin_acc = '/bin/false\n'
bin_acc = '/bin/bash\n'
def readPasswdFile():
    try:
        fp = open("/etc/passwd")
    except exceptions.UserWarning:
        print " no permission Amigo!"
        return "some default data"
    else:
        with fp:
            print "the username who can login are:"
            for n in fp.readlines(1):

                #print n
                nl = n.split(':')
                #print "here", nl
                if bin_acc in nl:
                    print nl[0]
                #if nl
                #user = nl[0]
                #print "username", user
                #acc = nl[-1]
                #print "bin ", acc
                #print acc.strip()
                # if acc.strip() !=  no_bin_acc:
                #     print (user)





            # #print(fp.read())
            # userlist = fp.read().split(':')
            # #nu = userlist[]
            # #print nu
            # #print userlist
            # return fp.read()

# def readPasswdFile():
#     if os.access("/etc/passwd", os.R_OK):
#         with open("/etc/passwd") as fp:
#             s = fp.read()
#             #sl = [fp.read().split(':')]
#             ss = s.split(':')
#
#
#
#             #print ('here')
#             print (ss)
#             return fp.read()
#     else:
#         print " no permission may be"
#     #return "some default data"

readPasswdFile()