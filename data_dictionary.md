# Data Dictionary — Netflix Global Content Insights (2016–2025)

**Dataset:** `01_Netflix_2016_2025.csv`
**Rows:** 200 | **Original Columns:** 10 | **Cleaned Columns:** 16
**Source:** Netflix global viewership records (2016–2025)

---

## Original Columns

| Column | Data Type | Description | Business Relevance |
|---|---|---|---|
| `Year` | Integer | Calendar year the content was released/tracked | Trend analysis over time |
| `Title` | String | Name of the Netflix show or film | Unique identifier for content |
| `IMDb` | Float | IMDb rating score (0–10 scale) | Proxy for content quality / audience reception |
| `Viewership` | String (raw) | Raw viewership metric (e.g., "21.7M Streams") — inconsistent units | Core engagement metric |
| `Directors/Creators` | String | Name(s) of directors or show creators | Talent performance analysis |
| `Lead Actors` | String | Lead cast members (comma-separated) | Star power analysis |
| `Release Date` | String (raw) | Original air/release date in `DD-Mon-YY` format | Seasonality and scheduling analysis |
| `Duration` | String (raw) | Season/episode count and total minutes (e.g., "S1; 400 min") | Content length analysis |
| `Country` | String | Country/countries of production (e.g., "UK/USA") | Geographic content strategy |
| `Genre` | String (raw) | Genre(s) of the content — had trailing whitespace | Genre performance analysis |

---

## Cleaned / Engineered Columns

| Column | Data Type | Description | Derived From |
|---|---|---|---|
| `Genre` | String | Genre cleaned of trailing whitespace | `Genre` (original) |
| `Primary_Country` | String | First-listed country of production only | `Country` |
| `IMDb_Band` | String | Categorical rating: Excellent (≥8.5), Good (≥7.5), Average (≥6.5), Below Average | `IMDb` |
| `Viewership_M` | Float | Viewership count in millions (numeric only) | `Viewership` |
| `Viewership_Unit` | String | Unit of viewership: Streams, Hours, or Views | `Viewership` |
| `Release_Date` | Date | Standardised date in `YYYY-MM-DD` format | `Release Date` |
| `Release_Month` | String | Month name of release (e.g., "July") | `Release Date` |
| `Release_Year` | Integer | Year extracted from release date | `Release Date` |
| `Duration_Min` | Integer | Total runtime in minutes (numeric) | `Duration` |
| `Season_Label` | String | Season/episode descriptor (e.g., "S1", "8 Eps") | `Duration` |

---

## Data Quality Issues Found

| Issue | Column | Details |
|---|---|---|
| Trailing whitespace | `Genre` | 134 of 200 rows had trailing spaces |
| Inconsistent units | `Viewership` | Mixed "M Streams", "M Views", "M Hours" — not directly comparable |
| Non-standard date format | `Release Date` | Two-digit year (`17-Jun-16`) — risk of century misinterpretation |
| Mixed format | `Duration` | Combined season label and minutes in one field (e.g., "S1; 400 min") |
| Multi-value field | `Country` | Multiple countries in one cell separated by "/" |
| Encoding issue | File | Required `latin1` encoding (not UTF-8) |

---

## Key Stats (Original Dataset)

- **Total Records:** 200
- **Years Covered:** 2016–2025
- **Missing Values:** None
- **Duplicate Rows:** None
- **IMDb Range:** 4.3 – 9.3 (Mean: 7.70)
- **Countries Represented:** 25 unique country combinations
