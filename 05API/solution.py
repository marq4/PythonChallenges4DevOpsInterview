
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)
print(f"{response = }")#TMP
#data = response.text

data = response.json()
print(f"{data = }")#TMP

