s1 = "qypy|y(;"
s2 = "}&%8>?p"
s3="#ur}}vz"

key = "HACKINI_KEY"
flag = ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"]

i=0
import string
j=0
for c in s1 :
	flag [i] = chr(ord(c) ^ ord(key[j]))
	j=j+1
	i =i+3
	
	
i=1
j=0

for c in s2 :
	flag [i] = chr(ord(c) ^ ord(key[j]))
	j=j+1
	i =i+3
flag[i] =  chr(int('11',16) ^ ord(key[j]))
print key[j]
i=2
j=0

for c in s3 :
	flag [i] = chr(ord(c) ^ ord(key[j]))
	j=j+1
	i =i+3


s=""

for c in flag :
	s +=c
print s
