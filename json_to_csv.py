import json
import pandas as pd

data = []

def no_default(dct):
    if 'coordinates' in dct:
        return dct['coordinates']
    return dct

this_file = 'trips-2009-raw.json'
# this_file =  'taxi.json'

with open(this_file) as f:
    for line in f:
        if (line.find("{") > -1):
            entry = line[line.find("{"):line.rfind("}")]+"}"
            data.append(json.loads(entry, object_hook=no_default))

pd.DataFrame.from_dict(data).to_csv('taxi_full.csv', index=False)