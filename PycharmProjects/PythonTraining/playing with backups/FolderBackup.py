__author__ = 'sabin'

#backup folder without simlinks inside it.
# find -type l -delete
# find /usr/local/lib/ -maxdepth 1 -follow  -type l -delete
#openssl enc -aes-256-cbc -e -in filepath -out filepath.enc -pass pass:passkey

import gzip, sys, subprocess, datetime

foldername = sys.argv[1]
replica = sys.argv[2]
passkey = sys.argv[3]

now = datetime.datetime.now()
print now.strftime("%Y-%m-%d-%H-%M-%S")

dtstamp = now.strftime("-%Y-%m-%d-%H-%M-%S")

compress_replica = replica + dtstamp + ".tar.gz"

#copying the folder along with its child folders and files.
ps_copyfolder = subprocess.Popen(['cp', '-r', foldername, replica], stdout=subprocess.PIPE)
ps_copyfolder.wait()

#find and delete the symlinks in the new replicated folder
ps_deletesymlinks = subprocess.Popen(['find', replica, '-type','l', '-delete'])
ps_deletesymlinks.wait()


# compress zip the new backup folder
ps_zip = subprocess.Popen(['tar', '-azcvf',compress_replica,replica])
ps_zip.wait()

#openssl #openssl enc -aes-256-cbc -e -in filepath -out filepath.enc -pass pass:passkey

encrypted_file = compress_replica + ".enc"
ps_passprotect = subprocess.Popen(['openssl', ' enc', '-aes-256-cbc', '-e', '-in',compress_replica, '-out', encrypted_file, '-pass', 'pass:',passkey])
ps_passprotect.wait()


