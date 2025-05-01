""" Read logfile passed as arg, parse, convert IPs. """

import sys

path = sys.argv[1]

lines = list()
with open(path, 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        if line[0] == '\n':
            continue
        lines.append(line)
#print(lines)#TMP

hex_ips = list()
for line in lines:
    ip = line.split()[2]
    hex_ips.append(ip)
#print(hex_ips)#TMP

cleaned_ips = list()
for ip in hex_ips:
    clean = ip.replace('[', '').replace(']', '').replace('ip-', '')
    cleaned_ips.append(clean)
#print(cleaned_ips)#TMP

# 0A1021E9 -> 10.16.33.233
for ip in cleaned_ips:
    #print(f"{ip = }")#TMP
    result = ''
    for index in range(0, 8, 2):
        pair = ip[index:index+2]
        #print(f"{pair = }")#TMP
        decimal = int(pair[0], 16) * 16 + int(pair[1], 16)
        #print(f"{pair} -> {decimal}")#TMP
        result = result + str(decimal)
        if index < 6:
            result += '.'
    print(f"{ip} -> {result}")

