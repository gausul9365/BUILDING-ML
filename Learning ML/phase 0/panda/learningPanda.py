import pandas as pd 

data = {
  "name" : ["A", "B", "C"],
  "math" : [80, 60, 90],
  "science" : [70, 85, 92]
}

df = pd.DataFrame(data)

# val = df.head()
# print(val)
# print(df.head())
# df.info()

# print(df.describe().round(2))

# val = df["name"]   ----> return series
val = df[df["math"] > 70]

print(val)

# return ---> dataframe
data_in_table = df[["math", "science"]]
print(data_in_table)

print(df.isnull())

df["average"] = (df["math"] + df["science"]) / 2
df["test"] = ("NaN")
print(df.head())


df.sort_values(by="average")

print(df.head())
print("...end...")



