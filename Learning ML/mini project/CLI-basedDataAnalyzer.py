# CLI-based Data Analyzer

# 1. Load CSV
# 2. Handle missing values
# 3. Add new feature (average)
# 4. Show:
# top student
# students above threshold
# 5. Print clean output

import pandas as pd


# 1
df = pd.read_csv('Book1.csv')
print(df)

# 2
df.fillna(df.mean(numeric_only=True), inplace= True)

# 3 
df["average"] = ( df["Math"] + df["Science"] ) / 2


# 4

# print(df.head())
# top_Student =  df["average"].max()
# print(top_Student)

# get top student 
top_row = df.loc[df["average"].idxmax()]
print("topper student:\n",top_row)

thresold = 80
above_thre = df[df["average"] > 80]

# 5
print(df.head())
