import sys

n = int(sys.argv[1])
log = sys.argv[2]
#print(f"{n=}, {log=}")#TMP

count = 0
with open(log, 'r') as file:
    #print(file.read())#TMP
    while True:
        line = file.readline()
        if not line:
            break
        count += 1
#print(f"{count=}")#TMP

with open(log, 'r') as file:
    while count:
        line = file.readline()
        if count <= n:
            print(line, end='')
        count -= 1

