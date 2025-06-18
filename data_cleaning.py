import pandas as pd

df=pd.read_csv("nvidia_stock_2015_to_2024.csv")

df.drop(columns=["Unnamed: 0"],inplace=True)
df["date"]=pd.to_datetime(df["date"])
df=df.drop_duplicates()
df.sort_values(by="date",inplace=True)
df.reset_index(drop=True,inplace=True)

missing_values=df.isnull().sum()
print("Missing values per column:\n ",missing_values)

if missing_values.sum()==0:
    print("No missing values found in the dataset.")

else:
    print("Missing values are found in the dataset.Consider filling or dropping them.")


print("\n Number of duplicates in the dataset: ",df.duplicated().sum())

print("\n The cleaned dataset preview: \n",df.head())
print(df.head())

df.to_csv("nvidia_stock_cleaned.csv",index=False)
print("\nThe cleaned dataset has been saved as 'nvidia_stock_cleaned.csv'.")
