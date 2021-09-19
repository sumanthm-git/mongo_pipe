import pandas as pd
import numpy as np
from pandas.io import json

#reading the sample CSV
df = pd.read_csv('sales.csv', dtype=object)

#making the _id field for json to use as unique field in MongoDB
df.index = np.arange(1, len(df)+1)
df['_id'] = df.index
copy_index = df.pop('_id')
df.insert(0,'_id',copy_index)

#converting onject to datetime64[ns]
df['Transaction_date'] = pd.to_datetime(df['Transaction_date'])
df['Account_Created'] = pd.to_datetime(df['Account_Created'])
df['Last_Login'] = pd.to_datetime(df['Last_Login'])
#print(df.dtypes)
#print(df)

#encoding df using records formatted json ans using iso dateformat
res = df.to_json(orient='records',date_format='iso')

#loads take file-like object, reads the data from that object and use that string to create a json object
parsed = json.loads(res)
#print(parsed)

#dumps take an json object and produces a string
str_res = json.dumps(parsed, indent=4)
#print(str_res)