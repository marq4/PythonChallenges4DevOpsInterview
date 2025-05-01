
import random
from collections import Counter

n = int(input())
products = list()
for _ in range(n):
    products.append( input() )

counter = Counter(products)

highest = max(counter.values())
#print(f"{highest=}")#TMP
most_popular = [product for product in counter if counter[product] == highest]
#print(f"{most_popular=}")#TMP

print( random.choice(most_popular) )

