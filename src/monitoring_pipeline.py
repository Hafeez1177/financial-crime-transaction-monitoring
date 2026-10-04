from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/transactions.csv')
required=['Transaction ID','Account ID','Timestamp','Country','Channel','Merchant Type','Amount EUR','Risk Score','Alert','Severity']
missing=[c for c in required if c not in df.columns]
if missing: raise ValueError(f'Missing columns: {missing}')
df['Timestamp']=pd.to_datetime(df['Timestamp'],errors='raise')
df['Amount EUR']=pd.to_numeric(df['Amount EUR'],errors='raise')
df['Risk Score']=pd.to_numeric(df['Risk Score'],errors='raise')
df['Alert']=pd.to_numeric(df['Alert'],errors='raise')
df['Review Priority']=pd.cut(df['Risk Score'],[-1,51,69,84,100],labels=['Routine','Medium','High','Critical'])
out=ROOT/'data/processed_transactions.csv'
df.to_csv(out,index=False)
print(f'Processed {len(df):,} transactions')
print(df['Severity'].value_counts().to_string())
