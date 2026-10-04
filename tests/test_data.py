import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/transactions.csv')
assert len(df)==6000
assert df['Transaction ID'].is_unique
assert (df['Amount EUR']>0).all()
assert df['Risk Score'].between(0,99).all()
assert df['Alert'].isin([0,1]).all()
print('PASS: transaction dataset checks')
