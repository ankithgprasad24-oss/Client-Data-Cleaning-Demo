import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent

df = pd.read_csv(base_dir / "client_data.csv")

print("Starting client data cleaning...")

original_rows = len(df)

df = df.drop_duplicates()
df = df.reset_index(drop=True)

df["Name"] = df["Name"].str.strip().str.title()
df["Email"] = df["Email"].str.strip()
df["City"] = df["City"].str.strip().str.title()

df["City"] = df["City"].replace({
    "Bengaluru": "Bangalore"
})

missing_values = df.isnull().sum().sum()

df = df.fillna("Not Provided")

df["Phone"] = df["Phone"].apply(
    lambda x: str(int(x)) if x != "Not Provided" else x
)

cleaned_rows = len(df)
duplicates_removed = original_rows - cleaned_rows

df.to_csv(base_dir / "cleaned_client_data.csv", index=False)

print(df)
print()
print("Cleaned file saved as: cleaned_client_data.csv")
print(f"Rows: {original_rows} → {cleaned_rows}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"Missing values filled: {missing_values}")
print("Client data cleaning completed successfully!")