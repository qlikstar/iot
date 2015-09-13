import hashlib  # Comes with Python.

from OpenSSL.crypto import *
from OpenSSL import crypto



# open it, using password. Supply/read your own from stdin.
p12 = load_pkcs12(file("/Users/sanketmishra/Documents/crypto/b639150c.e7bb.4b53.ae70.3f591f022f49.p12", 'rb').read(),
                  'notasecret')
# get various properties of said file.
# note these are PyOpenSSL objects, not strings although you
# can convert them to PEM-encoded strings.
public_key_bytes = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())  # (signed) certificate object
public_key = public_key_bytes.decode('utf-8')  # private key.
print public_key

print "--------------------------------------"

private_key_bytes = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())
private_key = private_key_bytes.decode('utf-8')  # private key.
print private_key

h = hashlib.sha1()
h.update(public_key)

cert_hash = h.hexdigest()

print 'fingerprint :' + 'F09C52B06CFFAEE4A3723AF04B04CDD5542F2504'
print cert_hash
