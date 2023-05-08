'''
nomic setup:
> nomic login
or
> nomic login {NOMIC_API_KEY}
'''

from nomic import atlas
import pandas as pd


df = pd.read_csv('./classification-dataset.csv')

df['id'] = range(1, len(df) + 1)
df = df[['id'] + list(df.columns[:-1])]
data = df.to_dict('records')

project = atlas.map_text(data=data,
                         indexed_field='prompt',
                         id_field='id',
                         name='LM generated evals',
                         description='201 nice sounding incorrerct answers',
                         colorable_fields=['answer_index'],
                         )
