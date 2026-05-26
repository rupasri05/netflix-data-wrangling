#  Netflix Global Content Insights — Data Wrangling Project

> **Internship | Data Immersion & Wrangling**
> Cleaning and preparing the Netflix Global Content Insights dataset (2016–2025) for analysis.

---

##  Repository Structure

```
netflix-data-wrangling/
│
├── data/
│   ├── 01_Netflix_2016_2025.csv      # Raw original dataset
│   └── netflix_cleaned.csv           # Final cleaned dataset (output)
│
├── data_dictionary.md                # Column definitions, types & business relevance
├── cleaning_script.py                # Python/Pandas cleaning & transformation script
└── README.md                         # You are here
```

---

##  About the Dataset

| Property | Value |
|---|---|
| Source | Netflix Global Content Data |
| Period | 2016 – 2025 |
| Records | 200 rows |
| Original Columns | 10 |
| Cleaned Columns | 14 |
| File Encoding | latin1 |

The dataset contains Netflix's top-performing shows and films each year, including viewership numbers, IMDb ratings, release dates, duration, genre, country of production, and key cast/crew.

---

##  Data Quality Issues Identified

Six issues were found during profiling:

| # | Issue | Column | Impact |
|---|---|---|---|
| 1 | Non-UTF-8 encoding | Entire file | File fails to load with default settings |
| 2 | Trailing whitespace | `Genre` | 134/200 rows affected; breaks grouping/filtering |
| 3 | Mixed viewership units | `Viewership` | "Streams", "Views", "Hours" — not directly comparable |
| 4 | Non-standard date format | `Release Date` | Two-digit year (`17-Jun-16`) risks century errors |
| 5 | Combined field | `Duration` | Season label and minutes stored together (e.g., `S1; 400 min`) |
| 6 | Multi-value country field | `Country` | Multiple countries in one cell (e.g., `UK/USA`) |

---

##  Cleaning & Transformations Applied

### Fixes
- **Genre** — stripped leading/trailing whitespace from all values
- **Release Date** — parsed from `DD-Mon-YY` string into proper `datetime` format
- **Viewership** — extracted numeric value (millions) and unit type into separate columns
- **Duration** — split into `Duration_Min` (integer minutes) and `Season_Label` (e.g., "S1", "8 Eps")

### Feature Engineering (New Columns)
| New Column | Description | Derived From |
|---|---|---|
| `Viewership_M` | Viewership count in millions (numeric) | `Viewership` |
| `Viewership_Unit` | Unit type: Streams / Views / Hours | `Viewership` |
| `Release_Date` | Standardised date (`YYYY-MM-DD`) | `Release Date` |
| `Duration_Min` | Total runtime in minutes | `Duration` |
| `Season_Label` | Season/episode label (e.g., "S1") | `Duration` |
| `Primary_Country` | First-listed country of production | `Country` |
| `IMDb_Band` | Quality tier: Excellent / Good / Average / Below Average | `IMDb` |

---

##  How to Run

### Prerequisites
Make sure you have Python 3 and pandas installed:
```bash
pip install pandas
```

### Steps
```bash
# 1. Clone this repository
git clone https://github.com/your-username/netflix-data-wrangling.git
cd netflix-data-wrangling

# 2. Place the raw dataset in the data/ folder
#    (01_Netflix_2016_2025.csv)

# 3. Run the cleaning script
python cleaning_script.py

# 4. Output will be saved as:
#    data/netflix_cleaned.csv
```

---

##  Deliverables

- [x] `data_dictionary.md` — full column-level documentation
- [x] `cleaning_script.py` — commented Python/Pandas cleaning script
- [x] `netflix_cleaned.csv` — final analysis-ready dataset
- [x] `README.md` — project overview and instructions

---

##  Tools Used

- **Python 3**
- **Pandas** — data loading, cleaning, transformation
- **re (Regex)** — parsing mixed-format strings (Viewership, Duration)

---

##  Author

**Rupa Sri**
Data Analytics Intern
linkedin.com/in/rupa-sri-561066303 | github.com/rupasri05
