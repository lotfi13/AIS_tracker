import pandas as pd

df = pd.read_json ('out.jsonl')
df.to_csv ('listcsv.csv', index = None)
