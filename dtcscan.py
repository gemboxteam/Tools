import os
import readline
import requests
import socket
import time


url = 'https://raw.githubusercontent.com/ninjabuster/Tools/main/domain-enum.py'
r = requests.get(url)

with open('domain-enum.py', 'wb') as f:
    f.write(r.content)


print ""
url = raw_input("Enter Target Url : ")

a = "python3 domain-enum.py -o output.txt -d" + (url)
os.system(a)

time.sleep(5)
# read domain list and convert to ip
file = open("output.txt","r")

domain_list = []

for x in file.readlines():
        domain_list.append(x.strip())

report = open('ip.txt', 'w')

print ""
print("Getting IP from Domains . . .")
print("=============================")

for y in domain_list:
       report.write(socket.gethostbyname(y) + '\n')

report.close()

time.sleep(2.4)

#replace duplicates ip
uniqlines = set(open('ip.txt').readlines())
uniqlines = open('ip.txt', 'w').writelines(set(uniqlines))

ip = set(open('ip.txt').readlines())
for line in ip:
    separator = "."
    ipNo4Oct = separator.join(line.split(separator, 3)[:-1]) + '.0/24'
    print (ipNo4Oct)
print ""
print "============================="
print("Done, Output stored on ip.txt")
