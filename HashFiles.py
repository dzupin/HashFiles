import hashlib
BLOCKSIZE = 65536
hasherMD5 = hashlib.md5()
hasherSHA1 = hashlib.sha1()
hashlib.SHA512 = hashlib.sha512()

#For hashing demo, use source code file
with open('HashFiles.py') as myFile:
    buf = myFile.read(BLOCKSIZE)
    while buf:
        hasherMD5.update(buf.encode('utf-8'))
        hasherSHA1.update(buf.encode('utf-8'))
        hasherSHA512 = hashlib.sha512()
        buf=myFile.read(BLOCKSIZE)
print("MD5 signature   :    " + hasherMD5.hexdigest())
print("SHA1 signature  :   " + hasherSHA1.hexdigest())
print("SHA512 signature: " + hasherSHA512.hexdigest())