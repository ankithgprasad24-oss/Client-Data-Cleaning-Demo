# Client Data Cleaning Demo

A simple Python data-cleaning demo that shows how messy customer CSV data can be cleaned and standardized automatically.

## What It Does

- Removes duplicate records
- Cleans name formatting
- Standardizes city names
- Fills missing values with `Not Provided`
- Cleans phone-number formatting
- Creates a cleaned CSV output automatically
- Shows a summary of the cleaning process

## Files

- `client_data.csv` — sample messy client data
- `clean_client_data.py` — Python cleaning script
- `cleaned_client_data.csv` — cleaned output

## Technologies Used

- Python
- Pandas
- pathlib

## Example Result

The sample data contains duplicate and missing values.

After running the script:

- Rows: 6 → 5
- Duplicates removed: 1
- Missing values filled: 2

## How to Run

1. Open `clean_client_data.py`
2. Click the Run button in VS Code
3. The cleaned file will be created automatically as `cleaned_client_data.csv`