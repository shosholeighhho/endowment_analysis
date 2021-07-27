import requests
import pandas as pd
import os


base_url = 'https://s3.amazonaws.com/irs-form-990/'
url_suffix = '_public.xml'


all_ids = list(pd.read_csv('../index_2021.csv', index_col=False).OBJECT_ID)
all_ids.extend(list(pd.read_csv('../index_2020.csv', index_col=False).OBJECT_ID))

all_ids.reverse()
all_ids = all_ids[385000:]
for num in all_ids:
    if os.path.isfile(f'../data/file_{num}.xml'):
        continue
    url = base_url + str(num) + url_suffix
    try:
    	resp = requests.get(url)
    except:
    	continue
    print(f'file_{num}.xml')
    with open(f'../data/file_{num}.xml', 'wb') as foutput:
    	foutput.write(resp.content)