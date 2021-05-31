import random
import json

data = []
for i in range(0,1000):
	n = random.randint(0,100)
	data.append(n)

with open('data.json', 'w') as f:
    json.dump(data, f)