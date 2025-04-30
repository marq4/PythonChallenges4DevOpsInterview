""" GET content from log, use Counter to get most popular. """

from collections import Counter 
import requests

URL = 'https://public.karat.io/content/urls.txt'

response = requests.get(URL)
#print(response.content)#TMP

urls = response.text.split()
#print(f"{urls = }")#TMP

count = Counter(urls)
#print(f"{count = }")#TMP

winner = count.most_common(1)
#print(f"{winner=}")#TMP
url = winner[0][0]
popularity = winner[0][1]
print(f"The most popular URL is: {url} with {popularity} occurrences. ")

