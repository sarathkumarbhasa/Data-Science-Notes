1. pd.Series()

What it does:
Creates a one-dimensional labeled array — like a single column of data.

Example:

import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40], name="Marks")

print(s)


Output:

0    10
1    20
2    30
3    40
Name: Marks, dtype: int64


✅ Think of a Series as an Excel column with index numbers on the left.

🧱 2. pd.DataFrame()

What it does:
Creates a table — a 2D labeled data structure with rows and columns.

Example:

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "City": ["New York", "Paris", "London"]
}

df = pd.DataFrame(data)
print(df)


Output:

      Name  Age      City
0    Alice   24  New York
1      Bob   27     Paris
2  Charlie   22    London


✅ Think of a DataFrame as an Excel sheet with rows and columns.

📍 3. df.loc[]

What it does:
Selects data by label (name) of row/column.

Example:

# Select row with label 1
print(df.loc[1])

# Select specific cell (row 1, column "City")
print(df.loc[1, "City"])


Output:

Name      Bob
Age        27
City    Paris
Name: 1, dtype: object

Paris


✅ .loc[] = “location by name”.

📏 4. df.iloc[]

What it does:
Selects data by position (index number).

Example:

# Select first row
print(df.iloc[0])

# Select value in 2nd row, 3rd column
print(df.iloc[1, 2])


Output:

Name      Alice
Age          24
City    New York
Name: 0, dtype: object

Paris


✅ .iloc[] = “integer location”.

🗑️ 5. df.drop()

What it does:
Removes rows or columns.

Example:

# Drop the "Age" column
df1 = df.drop("Age", axis=1)
print(df1)

# Drop row with index 1
df2 = df.drop(1)
print(df2)


Output:

      Name      City
0    Alice  New York
1      Bob     Paris
2  Charlie    London

      Name  Age      City
0    Alice   24  New York
2  Charlie   22    London


✅ axis=1 → drop column, axis=0 → drop row.

🏷️ 6. df.rename()

What it does:
Renames column(s) or row index(es).

Example:

df_renamed = df.rename(columns={"Name": "Full Name"})
print(df_renamed)


Output:

  Full Name  Age      City
0     Alice   24  New York
1       Bob   27     Paris
2   Charlie   22    London

🧹 7. df.dropna()

What it does:
Removes rows with missing (NaN) values.

Example:

df2 = pd.DataFrame({
    "Name": ["Alice", "Bob", None],
    "Age": [24, None, 22]
})

print(df2.dropna())


Output:

    Name   Age
0  Alice  24.0


✅ Rows with missing data are dropped.

💧 8. df.fillna()

What it does:
Fills missing values with a specified value.

Example:

print(df2.fillna("Unknown"))


Output:

      Name      Age
0    Alice     24.0
1      Bob  Unknown
2  Unknown     22.0


✅ Great for replacing NaN with 0, "N/A", or averages.

🔁 9. df.drop_duplicates()

What it does:
Removes duplicate rows.

Example:

df3 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Alice"],
    "Age": [24, 27, 24]
})

print(df3.drop_duplicates())


Output:

    Name  Age
0  Alice   24
1    Bob   27


✅ Keeps only the first occurrence by default.

⚙️ 10. df.apply()

What it does:
Applies a function to each row or column.

Example:

# Add 10 to each Age
df["Age_plus_10"] = df["Age"].apply(lambda x: x + 10)
print(df)


Output:

      Name  Age      City  Age_plus_10
0    Alice   24  New York           34
1      Bob   27     Paris           37
2  Charlie   22    London           32


✅ Very powerful for quick calculations or transformations.

🔗 11. pd.merge()

What it does:
Combines two DataFrames based on a common column (like a database JOIN).

Example:

df_a = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
df_b = pd.DataFrame({"ID": [1, 2, 4], "Score": [90, 80, 70]})

merged = pd.merge(df_a, df_b, on="ID", how="inner")
print(merged)


Output:

   ID   Name  Score
0   1  Alice     90
1   2    Bob     80


✅ how can be 'inner', 'left', 'right', or 'outer'.

📄 12. pd.read_csv()

What it does:
Reads a CSV file into a DataFrame.

Example:

df = pd.read_csv("data.csv")
print(df.head())


✅ Use when importing data from Excel-like .csv files.

📘 13. pd.read_excel()

What it does:
Reads an Excel file into a DataFrame.

Example:

df = pd.read_excel("data.xlsx")
print(df.head())


✅ Needs the openpyxl library installed.

🌐 14. pd.read_json()

What it does:
Reads data from a JSON file or JSON string.

Example:

df = pd.read_json('{"Name":["Alice","Bob"],"Age":[24,27]}')
print(df)


Output:

    Name  Age
0  Alice   24
1    Bob   27

⏰ 15. pd.to_datetime()

What it does:
Converts a column or list into datetime objects.

Example:

dates = pd.to_datetime(["2024-01-01", "2024/02/01", "March 3, 2024"])
print(dates)


Output:

DatetimeIndex(['2024-01-01', '2024-02-01', '2024-03-03'], dtype='datetime64[ns]', freq=None)


✅ Makes date handling much easier for analysis.

🔤 16. df.astype()

What it does:
Changes the data type of a column.

Example:

df["Age"] = df["Age"].astype(float)
print(df.dtypes)


Output:

Name     object
Age      float64
City     object
dtype: object


✅ Useful when you need to convert data for math or merging.
