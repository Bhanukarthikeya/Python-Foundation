import pandas as pd

# print(pd.__version__)

# series = a pandas one dimensional labelled array that can hold any data type
#          thick of it like a single column in a spreadsheet (1-Dimensional)

# data = [100, 102, 104, 200, 202]
# # series = pd.Series(data)
# series = pd.Series(data, index=["a", "b", "c", "d", "e"])
# series = pd.Series(data, index = ["apartment #1","apartment #2","apartment #3"])

# print(series)
# print(series.loc["a"])   # 100
# print(series.loc["b"])   # 102

# series.loc["c"] = 200
# print(series)

# print(series.iloc[0])  # 100
# print(series.iloc[1])  # 102

# print(series[series >= 200])

# dict

# calories = {"Day 1": 1750,
#             "Day 2": 2100,
#             "Day 3": 1700}

# series = pd.Series(calories)
# print(series.loc["Day 1"]) # 1750

# series.loc["Day 3"] += 500

# print(series.loc["Day 3"])

# print(series[series >= 2000]) # Day 2  2100

# DataFrames = A tabular data structure with rows and columns (2-Dimensional)
#              similar to Excel spreadsheet


# data = {
#     "Name": ["Bhanu", "karthikeya", "yadlapalli"],
#     "Age": [18, 19, 20]
# }

# df = pd.DataFrame(data, index=["employee 1", "employee 2", "employee 3"])

# # print(df)
# # print(df.loc["employee 1"])
# # print(df.iloc[0])

# # add a new column

# df["Job"] = ["Manager","cook","cashier"]
# print(df)

# # add a new row
# new_row = pd.DataFrame([{"Name": "palak",
#                          "Age": 28,
#                          "Job": "owner"}], index = ["employee 4"])

# df = pd.concat([df, new_row])
# print(df)

# importing and reading a data file

# CSV file
# df = pd.read_csv("pokemon.csv")
# print(df.to_string())

# JSON file
# df = pd.read_json("pokemon.json")
# print(df.to_strings())

# selection tech

# df = pd.read_csv("pokemon.csv")

# SELECTION BY COLUMN

# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df[["Name","Height","Weight"]].to_string())

# SELECTION BY ROWS

# df = pd.read_csv("pokemon.csv", index_col = "Name")

# print(df.loc["Pikachu",["Height","Weight"]])
# print(df.loc["Mewtwo"])

# print(df.loc["Pikachu":"Mewtwo",["Height","Weight"]]) # slicing

# print(df.iloc[0:11])
# print(df.iloc[0:11:2])

# pokemon = input("enter a pokemon name: ")

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print("pokemon not found")


# filtering = keeping the rows that match the condition

# df = pd.read_csv("pokemon.csv")
# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

# heavy_pokemon = df[df["Weight"] >= 100]
# print(heavy_pokemon)

# leg_pokemon = df[df["Legendary"] == 1]
# print(leg_pokemon)


# water = df[(df["Type1"] == "Water") | (df["Type2"] == "Water") ]
# print(water)

# ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
# print(ff_pokemon)


# aggregation - reduces a set of values into a single summary value
#               used to summarize and analyze data
#               often used with the groupby() function

# df = pd.read_csv("pokemon.csv")
# whole data frame
# print(df.mean(numeric_only= True))

# print(df.sum(numeric_only= True))

# print(df.min(numeric_only= True))

# print(df.max(numeric_only= True))

# print(df.count())

# single column

# print(df["Height"].mean())

# print(df["Height"].sum())

# print(df["Weight"].min())

# print(df["Weight"].max())

# print(df["Type2"].count())

# df = pd.read_csv("pokemon.csv")

# groupby()

# group = df.groupby("Type1")

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())

# data cleaning - the process of fixing/cleaning/removing:
#                 incomplete, incorrect or irrelevant data.
#                 around 75% of work done with pandas is data cleaning

df = pd.read_csv("pokemon.csv")
# 1: drop irrelevant columns
# df = df.drop(columns = ["Legendary","No"])
# print(df)

# 2: Handle missing data

# df = df.dropna(subset= ["Type2"])
# print(df.to_string())

# df = df.fillna({"Type2": "None"})

# print(df.to_string())


# 3: Fix inconsistent values

# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE",
#                                    "Water": "WATER"})

# print(df)

# 4. standardize text

# df["Name"] = df["Name"].str.lower()

# 5. fix data types

# df["Legendary"] = df["Legendary"].astype(bool)

# 6. remove duplicate values

# df = df.drop_duplicates()


# print(df)

print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.shape)        # Number of rows and columns
print(df.columns)      # Column names
print(df.dtypes)       # Data types
print(df.info())       # Dataset structure
print(df.describe())   # Numerical summary


print(df["Name"])                 # One column
print(df[["Name", "Marks"]])      # Multiple columns

print(df.loc[0, "Name"])          # By label
print(df.iloc[0, 1])              # By position

print(df[df["Marks"] > 80])       # Filter rows


print(df.isnull().sum())    # Missing values per column

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df = df.drop_duplicates()








