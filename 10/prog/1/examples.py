from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# print(df.head())


# print(df["sepal length (cm)"].mean())

df["a"] = df["sepal length (cm)"]
df["b"] = df["sepal width (cm)"]
df["c"] = df["petal length (cm)"]
df["d"] = df["petal width (cm)"]

# df = df.drop(
#     columns=[
#         "sepal length (cm)",
#         "sepal width (cm)",
#         "petal length (cm)",
#         "petal width (cm)",
#     ],
# )

df.drop(
    columns=[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ],
    inplace=True,
)

# df = df[(df["a"] >= 5.0) & (df["c"] <= 1.4)]

# print(df.isna().sum())
#
# df.dropna(axis="rows", inplace=True)
#
# print(df.shape)

df.to_csv("iris.csv")
