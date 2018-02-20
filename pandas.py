import pandas as pd
url="http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url)
df=pd.read_csv(url,header=None)
df

headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compressionratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]

 df.column=headers
df.head(10)
df.tail(10)
df.dtypes
df.describe()
df.describe(include="all")

df["symboling"]

df.dropna(subset=["price"],axis=0,inplace=True]
df.dropna()
