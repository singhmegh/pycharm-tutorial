import pandas as pd

# pivoting
"""dict = {"keys": ["k1", "k2", "k1", "k2"],
        "Names": ["John", "Ben", "David", "Peter"],
        "Houses": ["red", "blue", "green", "red"],
        "Grades": ["3rd", "8th", "9th", "8th"]}

df = pd.DataFrame(dict)
print(df)
print(df.pivot(index="keys", columns="Names", values=["Houses", "Grades"]))"""

# melting
dict = {"Names": ["John", "Ben", "David", "Peter"],
        "Houses": ["red", "blue", "green", "red"],
        "Grades": ["3rd", "8th", "9th", "8th"]}

df = pd.DataFrame(dict)
print(df)
print(pd.melt(df, id_vars=["Names"], value_vars=["Houses", "Grades"], var_name="Houses&Grades", value_name="values"))
