import pandas as pd
import re

# Loading
# Must use latin1 encoding — file contains non-UTF-8 characters
df = pd.read_csv("01_Netflix_2016_2025.csv", encoding="latin1")

print(f"Loaded: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")

df = df.drop_duplicates()


#Clean Genre (Issue 1 — trailing whitespace) 
df["Genre"] = df["Genre"].str.strip()


# Parse Viewership (Issue 2 — mixed units) 
def parse_viewership_number(val):
    match = re.search(r"([\d.]+)M", str(val))
    return float(match.group(1)) if match else None

def parse_viewership_unit(val):
    val = str(val)
    if "Streams" in val:
        return "Streams"
    if "Hours" in val:
        return "Hours"
    if "Views" in val:
        return "Views"
    return "Unknown"

df["Viewership_M"]    = df["Viewership"].apply(parse_viewership_number)
df["Viewership_Unit"] = df["Viewership"].apply(parse_viewership_unit)


# Standardise Release Date (Issue 3) 
df["Release_Date"]  = pd.to_datetime(df["Release Date"], format="%d-%b-%y", errors="coerce")

# Split Duration field (Issue 4)
def extract_duration_minutes(val):
    match = re.search(r"(\d+)\s*min", str(val))
    return int(match.group(1)) if match else None

def extract_season_label(val):
    match = re.match(r"^([^;]+);", str(val))
    return match.group(1).strip() if match else str(val).strip()

df["Duration_Min"]  = df["Duration"].apply(extract_duration_minutes)
df["Season_Label"]  = df["Duration"].apply(extract_season_label)


# Extract Primary Country (Issue 5) 
df["Primary_Country"] = df["Country"].str.split("/").str[0].str.strip()


# IMDb Band — feature engineering 
def imdb_band(score):
    if score >= 8.5:
        return "Excellent"
    elif score >= 7.5:
        return "Good"
    elif score >= 6.5:
        return "Average"
    else:
        return "Below Average"

df["IMDb_Band"] = df["IMDb"].apply(imdb_band)


#  Drop original raw columns, reorder 
df_clean = df.drop(columns=["Viewership", "Release Date", "Duration"])

column_order = [
    "Year", "Title", "Genre", "Country", "Primary_Country",
    "IMDb", "IMDb_Band",
    "Viewership_M", "Viewership_Unit",
    "Release_Date",
    "Duration_Min", "Season_Label",
    "Directors/Creators", "Lead Actors",
]
df_clean = df_clean[column_order]


#  Save 
df_clean.to_csv("netflix_cleaned.csv", index=False)

print(f"\nCleaned dataset saved: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")
print("\nSample output:")
print(df_clean.head(3).to_string())
print("\nColumn summary:")
print(df_clean.dtypes)