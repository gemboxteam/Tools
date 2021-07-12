import os
import socket
import readline
import time


#Colour Def
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

#prGreen("Hello, World!")



print("")
print("")
print("   ######  #######  #####   #####   #####     #    #     #")
print("   #     #    #    #     # #     # #     #   # #   ##    #")
print("   #     #    #    #       #       #        #   #  # #   #")
print("   #     #    #    #        #####  #       #     # #  #  #")
print("   #     #    #    #             # #       ####### #   # #")
print("   #     #    #    #     # #     # #     # #     # #    ##")
print("   ######     #     #####   #####   #####  #     # #     #")

print("")
prYellow("                                       Domain Enumerations")
print("")


url = raw_input("Enter Target Url : ")
if url:
    print(url)
else:
    print(url)


inasn = open('data.txt', 'w')
getasn = socket.gethostbyname (url)
os.system("service tor restart")
print("")


prGreen("=========================================================================")
prYellow("[+] Total Digital Assets Findings for " + (url) + " by AS Number :   ")
prGreen("=========================================================================")


findasn = "proxychains curl https://api.hackertarget.com/aslookup/?q=" + (getasn) + " > preasn.txt" + " 2>/dev/null"
os.system(findasn)

nano = open("preasn.txt", "r")
print(nano.read())
nano.close()

#Parsing ASN
assn = "cat preasn.txt |cut -d ',' -f 2 |sed 1d > preasn2.txt"
os.system(assn)

#Remove Quotes
fin = open("preasn2.txt", "rt")
fout = open("asn.txt", "wt")

for line in fin:
    fout.write(line.replace('"', ''))

fin.close()
fout.close()
print("")

#GET CIDR from ASN
print("[+] GET CIDR from ASN...")
cidrr =  open('asn.txt', 'r')
cid = cidrr.read()
cidr = "proxychains curl https://api.hackertarget.com/aslookup/?q=AS" + (cid) + " 2>/dev/null"
os.system(cidr)
print("")

#data = open("data.txt", "r")
#print(data.read())
#data.close()
