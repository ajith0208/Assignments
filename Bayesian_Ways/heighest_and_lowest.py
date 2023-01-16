import pandas as pd

df = pd.read_csv('data.csv')
df = df.replace(',', '', regex=True)
df['USD ($)'] = df['USD ($)'].astype(float)

h = 0
s = df['USD ($)'][0]
for i in df['USD ($)']:
    if i > h:
        h = i
    else:
        if i <= s:
            s = i

print(f'Heighst Price of Bitcoin in USD : {h}')
print(f'Lowest Price of Bitcoin in USD : {s}')
