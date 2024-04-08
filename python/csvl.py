# Save data into csv file 

import pandas as pd

url = 'file:///home/kyoto_123/Desktop/works/assessment/bincom-dev-center/index.html'
df = pd.read_html(url)[0]  # [0] is the first table in the page

df.to_csv('table.csv', index=False)

print(df.columns)