import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})

# print(df)

# print(df.head(2))


df["A"] += 4

# print(df)


df["B"] *= 3

# print(df)


# print(df["A"][0])


df["C"] = df["B"] * df["A"]


df_col = df[["B", "C"]]

# print(df_new)

df["D"] = df["A"] ** 3

indices = (df["A"] % 2 == 1) ^ (df["D"] > 150)

# print(indices)


# print(df[indices])

# [i][j]
# [i, j]


# print(df)

# del df.loc[1]

df.index += 3

# print(df.loc[1:]["C"])
# print(df.iloc[1:]["C"])

new_column = df["C"].apply(lambda elem: len(elem))

df["E"] = new_column

# print(df)


df_col = df.apply(lambda column: column * 0, axis="columns")
# print(df_col)

# df_row = df.apply(lambda row: {"A": row.A, "B": row.B}, axis="rows")
# print(df_row)


print(df.shape)
print(len(df))
print(len(df.columns), list(df.columns))
