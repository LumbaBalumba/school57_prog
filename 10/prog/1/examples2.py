import pandas as pd


df = pd.read_csv("./iris.csv")

df.drop(columns="Unnamed: 0", inplace=True)

print(df.head())

print(df.isna().sum())

# df.fillna(0, inplace=True)
df.fillna(
    {
        "a": df["a"].mean(),
        "b": df["b"].median(),
        "c": df["c"].max(),
        "d": df["d"].min(),
    },
    inplace=True,
)

print(df.isna().sum())


df = df[df["a"] > df["a"].median()]

print(df.shape)


print(df.transpose())
print(df.columns)
