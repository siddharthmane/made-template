import pandas as pd
from sqlalchemy import create_engine
from io import StringIO
import urllib.request
import re

url = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'
response = urllib.request.urlopen(url)
csv_content = response.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_content),sep=';')
df = df.drop("Status", axis='columns')

Magnitude = ['Laenge', 'Breite']
df[Magnitude] = df[Magnitude].replace({',': '.'}, regex=True)
df[['Laenge', 'Breite']] = df[['Laenge', 'Breite']].apply(pd.to_numeric)

valid_values = ["FV", "RV", "nur DPN"]
df = df[df['Verkehr'].isin(valid_values)]

for x in df.index:
    if df.loc[x, "Laenge"] <= -90:
       df = df.drop(x, inplace=True)
    elif df.loc[x, "Laenge"] >= 90:
        df = df.drop(x, inplace=True)

for x in df.index:
    if df.loc[x, "Breite"] <= -90:
        df = df.drop(x, inplace=True)
    elif df.loc[x, "Breite"] >= 90:
        df = df.drop(x, inplace=True)

pattern = r'^[a-zA-Z]{2}:\d+:\d+(?::\d+)?$'
df = df[df['IFOPT'].astype(str).str.contains(pattern, na=False)]

df = df.dropna()  # Drop rows with empty cells
df['Betreiber_Nr'] =  df['Betreiber_Nr'].astype(int)

db_connection_str = 'sqlite:///trainstops.sqlite'
engine = create_engine(db_connection_str)
df.to_sql('trainstops', con=engine, index=False, if_exists='replace')
engine.dispose()