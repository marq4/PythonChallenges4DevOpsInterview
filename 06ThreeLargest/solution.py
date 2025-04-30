

raw_in: str = input()
clean = raw_in.replace('[', '')
clean = clean.replace(']', '')
#print(f"{clean = }")#TMP

numbers = [int(n) for n in clean.split(',')]
#print(f"{numbers = }")#TMP


numbers.sort()
result = numbers[-3:]
print(result)


