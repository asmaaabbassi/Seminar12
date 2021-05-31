import json
import pandas as pd
import matplotlib.pyplot as plt


with open('data.json') as f:
  data = json.load(f)


rangeList = range (0, 1000)
plt.bar(rangeList, data)
plt.show()

