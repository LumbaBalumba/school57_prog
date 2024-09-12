import pandas as pd

df = pd.read_csv("uni.csv")

for column in df.columns:
    print(column, df[column].dtype)

print(df["Continent"].unique())

df = df[df["Continent"] == "Asia"]

# print(df.isna().sum())

df = df[df["Affiliation"] == "Public"]

# print(df.shape)

# print(df.columns)

# print((df.index + 1 == df["Rank"]).all())

df.drop(columns="Rank", inplace=True)

df["Continent"] = df["Continent"].astype("category")
df["Affiliation"] = df["Affiliation"].astype("category")
df["Distance / In-Person"] = df["Distance / In-Person"].astype("category")

df["Founded"] = df["Founded"].apply(lambda date: int(date))

df.drop(columns="Location", inplace=True)

print(df.head())
