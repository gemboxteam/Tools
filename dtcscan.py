import os
import readline
import requests
import socket
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



os.system('clear')

url = 'https://raw.githubusercontent.com/ninjabuster/Tools/main/domain-enum.py'
r = requests.get(url)

with open('domain-enum.py', 'wb') as f:
    f.write(r.content)


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
print("                                       Domain Enumerations")
print("")


url = raw_input("Enter Target Url : ")

print("Enter Target Url : " + (url))
os.system('clear')

a = "python3 domain-enum.py -p22,80,443,21,53,3306,445 -o domain.txt -d" + (url)
os.system(a)


#print("")
#print("Done, File Saved as domain.txt . . .")
#print("")

print("")
prYellow("[+] Validate Host Responses . . .")
print("")

time.sleep(2)

# Validate IP HOST
domains_output = 'output.txt'
domains_input = 'domain.txt'

# Create output domains file
open(domains_output, 'w').close()

try:
    # Try to open input domains file
    with open(domains_input, "r") as domains:
        # Fetch domains
        for domain in domains:
            try:
                # Try to resolve IP address
                line = domain.replace("\n", "") + " - " +  socket.getaddrinfo(domain.replace("\n", ""), 80)[0][4][0]
            except Exception, error:
                # Output exception
                line = domain.replace("\n", "") + " - " + "Host Not Responding"
#str(error)

            # Print line
            print line

            # Write line to output domains file
            with open(domains_output, "a") as file:
                file.write(line + "\n")
except Exception, error:
    # Output exception
    print "Error: " + error


time.sleep(1)

print("")
prYellow("[+] Removing Error Hosts From List...")
time.sleep(2)
print("")


#replace duplicates ip
uniqlines = set(open('output.txt').readlines())
uniqlines = open('output.txt', 'w').writelines(set(uniqlines))
print("")

os.remove("domain-enum.py")

time.sleep(2)
print("")

prGreen("=============================================================================================")
prYellow("[+] Total Digital Assets Findings for " + (url) + " by Massive Domains Enumeration :   ")
prGreen("=============================================================================================")
print("")

# read file and print output
infile = open('output.txt')
newopen = open('parsing.txt', 'w')

for line in infile :

    if 'Host' in line:
        line = line.replace('.' , '')
    else:
        newopen.write(line)

newopen.close()
f = open("parsing.txt", "r")
print(f.read())

time.sleep(2)
#Parsing As Valid IP
os.system(r"cat parsing.txt |cut -d ' ' -f 3 > valid-ip.txt")


#Parsing as Valid Domains
os.system(r"cat parsing.txt |cut -d ' ' -f 1 > valid-domains.txt")

print("")
prYellow("   ===> Valid ip Saved as valid-ip.txt")
prYellow("   ===> Valid domains Saved as valid-domains.txt")
print("")

#Get ASN Number
prGreen("=========================================================================")
prYellow("[+] Total Digital Assets Findings for " + (url) + " by AS Number :   ")
prGreen("=========================================================================")


print("")
inasn = open('data.txt', 'w')
getasn = socket.gethostbyname (url)

os.system("service tor restart")

