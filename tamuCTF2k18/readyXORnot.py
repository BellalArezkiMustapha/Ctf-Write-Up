import base64

key=[]
original_data  = "El Psy Congroo"
encrypted_data = base64.b64decode("IFhiPhZNYi0KWiUcCls=")
encrypted_flag = base64.b64decode("I3gDKVh1Lh4EVyMDBFo=")
flag=""
size_encrypted_data = len(encrypted_data)

for i in xrange(size_encrypted_data) :
	key.append(ord(encrypted_data[i]) ^ ord(original_data[i]))

size_encrypted_flag = len(encrypted_flag)

for i in xrange(size_encrypted_flag) :
	
	flag+= chr(ord(encrypted_flag[i]) ^ key[i])

print flag

