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
prYellow(" *============ Massive Domain Enumerations ==============*")
print("")


url = raw_input("Enter Target Url : ")

print("Enter Target Url : " + (url))
os.system('clear')

a = "python3 domain-enum.py -p21,22,23,25,53,67,80,110,111,123,139,143,443,445,465,3000,3306,3389,5900,631,993,995,8008,8080,8081,9001 -o domain.txt -d" + (url)
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

prGreen("==================================================================================================")
prYellow("[+] Total Digital Asset Finding for " + (url) + " by Valid Massive Domain & IP Enumeration:   ")
prGreen("==================================================================================================")
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

#Count IPs for ASN
count = len(open('valid-domains.txt').readlines())
print "[+] Total Valid Domains & IPs  Found :",(count)
print("")


#Get ip for ASN
inasn = open('data.txt', 'w')
getasn = socket.gethostbyname (url)
#os.system("service tor restart")
print("")



prGreen("==============================================================================")
prYellow("[+] ASN Lookup For " + (url) + ": ")
prGreen("==============================================================================")


findasn = "proxychains curl https://api.hackertarget.com/aslookup/?q=" + (getasn) + " > preasn.txt" + " 2>/dev/null"
os.system(findasn)

#nano = open("preasn.txt", "r")
#print(nano.read())
#nano.close()

#Parsing just ASN
assn = "cat preasn.txt |cut -d ',' -f 2 |sed 1d | tail -c +2 | head -c -2  > preasn2.txt"
os.system(assn)

#Remove Quotes
fin = open("preasn2.txt", "rt")
fout = open("asn.txt", "wt")

for line in fin:
    fout.write(line.replace('"', ''))

fin.close()
fout.close()
print("")

who = "whois -h whois.cymru.com " + (getasn)
os.system(who)
print("")

prGreen("==============================================================================")
prYellow("[+] Additional Informations for " + (url) + ": ")
prGreen("==============================================================================")

print("")
shodan = "shodan host " + (getasn)
os.system(shodan)

#remove files
os.remove("output.txt"),
os.remove("preasn.txt")
os.remove("preasn2.txt")
os.remove("asn.txt")
os.remove("data.txt")
os.remove("parsing.txt")
os.remove("valid-ip.txt")
