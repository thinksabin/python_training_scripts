__author__ = 'sabin'

#Print the list of drives attached to the server.
import os

volumes = os.popen("mountvol /").read()
print volumes