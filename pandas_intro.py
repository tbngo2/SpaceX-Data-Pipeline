import pandas as pd

data = {

    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy',
    ],
    'launches': [5, 100, 3],

}

df = pd.DataFrame(data)
print(df)

print(df['rocket'])
falcon9_df = df[df['rocket'] == 'Falcon 9']

more_than_5_launches = df[df['launches'] > 5]
print(more_than_5_launches)
df['success_rate'] = [0.4,0.98,1.0]