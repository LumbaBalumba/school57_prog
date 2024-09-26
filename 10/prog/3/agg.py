import pandas as pd

A = {"student_id": [1, 2, 1, 2], "course_id": [2, 0, 3, 10]}
B = {
    "course_id": [0, 1, 2, 3, 4],
    "name": ["Algo", "Maths", "PE", "Phys", "Chem"],
    "hours": [20, 30, 10, 20, 15],
}

df_a = pd.DataFrame(A)
df_b = pd.DataFrame(B)
print(df_a, df_b, sep="\n")

df_left = pd.merge(df_a, df_b, how="left", on="course_id")
print(df_left, end="\n")

df_right = pd.merge(df_a, df_b, how="right", on="course_id")
print(df_right, end="\n")

df_inner = pd.merge(df_a, df_b, how="inner", on="course_id")
print(df_inner, end="\n")

df_outer = pd.merge(df_a, df_b, how="outer", on="course_id")
print(df_outer, end="\n")


A1 = {"student_id": [0, 3], "course_id": [3, 1]}
df_a1 = pd.DataFrame(A1)

df_a = pd.concat([df_a, df_a1])
print(df_a)
