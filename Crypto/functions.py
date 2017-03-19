import hashlib
import base64
import os
import conf

def encodeB64():
	print("#Base64 Encode#")
	a = input(">")
	b = base64.b64encode(bytes(a.encode("utf-8")))
	c = len(b) +2
	b = str(b)
	b = b[2:c]
	print("\"{a}\" encoded in base64 : {b}".format(a=a,b=b))

def decodeB64():
	print("#Base64 Decode#")
	a = input(">")
	conf.cls()
	try:
		b = base64.b64decode(bytes(a.encode("utf-8")))
		c = len(b) +2
		b = str(b)
		b = b[2:c]
		print("\"{a}\" \ndecoded from base64 : {b}".format(a=a,b=b))
	except:
		print("#Error: \"{a}\" is not base64#".format(a=a))

def encrypting(hashtype):
	print("#{hashtype} Encrypting#".format(hashtype=hashtype.upper()))
	a = hashlib.new(hashtype)
	b = input(">")
	b = b.encode('utf-8')
	a.update(b)
	c = a.digest()
	a = a.hexdigest()
	
	if conf.param['Digest'] == 'both':
		print("Hexadecimal : {a} \nDigest : {c}".format(a=a,c=c))
	elif conf.param['Digest'] == 'hex':
		print("Hexadecimal : {a}".format(a=a))
	elif conf.param['Digest'] == 'digestOnly':
		print("Digest : {c}".format(c=c))
	else:
		print("Hexadecimal : {a} \nDigest : {c}".format(a=a,c=c))

