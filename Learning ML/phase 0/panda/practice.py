import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "math": [80, 60, 90, None],
    "science": [90, 70, 95, 85],
    "english": [85, 65, 92, None]
}

df = pd.DataFrame(data)



# 1. Inspect Data
#     head()
#     info()
#     describe()



# print(df.head())
# df.info()
print(df.describe().round(2)) 

# 2. Handle Missing Values

value = df.isnull()
print(value)


df.fillna(df.mean(numeric_only= True), inplace= True)
print(df.head().round(2))


# add column - average of 3 subjects
df["average of three subject"] = (df["math"] + df["science"] + df["english"] ) / 3

print(df.head().round(2))


# 4. Filter - avg > 80 

fitered_data = df[df["average of three subject"] > 80]
print(fitered_data.round(2))


# 5. Sort highest avg first

sorted_val = df.sort_values(by = "average of three subject", ascending=False)
print(sorted_val.round(2))