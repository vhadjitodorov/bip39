import sys
from hashlib import sha256

#https://github.com/massmux/HowtoCalculateBip39Mnemonic#readme
#https://github.com/hatgit/BIP39-Mnemonic-Tools/blob/master/README.md


#Load 12 words from input to list
seedwords = sys.argv[1:] 
print 'Argument List:', str(seedwords)
if len(seedwords) == 12:

#Load 2048 wordlist from file
    with open('english.txt') as f:
	    wordlist = f.read().splitlines()

#Check if the words are in the list
    if set(seedwords).issubset(wordlist):
        print "kur"
    else:
        print "no kur"

#Convert strings to binary
    binwords = []
    for word in seedwords:
        binwords.append ("{0:011b}".format(wordlist.index(word)))
    print str(binwords)

#Concatenate strings
    binstring = ''.join(binwords)
    print 'bin words concat (all 132 ch): ' + (binstring)

#Cut to 128 bits (12 words are 132)
    cutbinstring = binstring[:128]
    print 'bin words concat (cut to 128): ' + (cutbinstring)

#Convert BIN string go HEX
    hexstring = hex(int(cutbinstring, 2))[2:34]
    print 'hex: ' +  (hexstring)

#Calculate SHA256 of the 128 bits of entropy	
    entropy_bytearray = bytearray.fromhex(hexstring)  # *convert no padded hex string to bytearray
    hashcode = sha256(entropy_bytearray).hexdigest()  # *compute the sha256 hash of the bytearray as a hex digest
    print 'hash: ' + (hashcode)

#Get the checksum from first character of the hash
    checksum = (bin(int(hashcode[:1],16)))[2:6]
    print 'checksum bin: ' + (checksum)

	
#Check if the words order is correct - checksum is OK
    binchecksum = binstring[121:128] + (checksum)
    print "last word bin: " + binchecksum
    if binwords[11] != binchecksum:
        print "This is NOT a valid set of 12 words!"
    else:
        print "This is a valid set of 12 words!"


#elseif reverse the list and check again
#elseif push the array 12 position and check again
#elseif swap consecutive words and check again
#else do 12! check 

#calculate all the generated combinations with right checksum




#check the networks for wallets with them

else:
    print "Wrong number of arguments: " + str(len(seedwords))
