# Web Scraping Top Data Firms - Enhanced Version

## [View Full Project](https://nbviewer.org/github/TelRich/Data-Analytics-Company-Web-Scraping/blob/main/top_da_company.ipynb)

![](newplot.png)

## 🎯 Project Overview

This project scrapes data from GoodFirms website to extract comprehensive information about top data analytics companies. The enhanced version includes additional features for extracting company URLs, locations, and contact information.

## ✨ New Features (Enhanced Version)

This fork adds the following capabilities:

1. **Company Name** - Extract full company names
2. **Company URL** - Extract company website URLs (where available)
3. **Company Geo** - Extract company geographical locations
4. **Company Email** - Placeholder for email extraction (not available on listing pages)
5. **Profile URL** - Extract GoodFirms profile URLs for each company

### Enhanced Data Fields

The enhanced scraper now extracts **12 data fields** per company:

| Field | Description | Availability |
|-------|-------------|--------------|
| Company Name | Official company name | ✓ All companies |
| Company URL | External website URL | ✓ Where available |
| Tagline | Company motto/tagline | ✓ All companies |
| Reviews | Review count and rating | ✓ All companies |
| Service % | Service focus percentage | ✓ All companies |
| Platform % | Platform focus percentage | ✓ All companies |
| Pricing | Hourly rate range | ✓ All companies |
| Employees | Employee count range | ✓ All companies |
| Founded | Year company was founded | ✓ All companies |
| Company Geo | Geographic location(s) | ✓ All companies |
| Profile URL | GoodFirms profile link | ✓ Most companies |
| Company Email | Contact email address | ⚠️ Not available on listing pages |

## 📊 Summary

* The webpage from Goodfirm was successfully accessed and downloaded using Request library
* BeautifulSoup was used to locate and extract the details from the downloaded HTML file
* The extracted details were converted to data frame using Pandas
* The file was cleaned and changed to its right datatype
* The cleaned file was explored for some insights
* **NEW**: Enhanced extraction functions added for company URLs and profile information

## 🔧 Usage

### Running the Enhanced Scraper

```bash
python3 enhanced_scraper_full.py
```

This will:
1. Process all three pages of company listings
2. Extract all 12 data fields for each company
3. Save results to `enhanced_extracted.csv`
4. Display summary statistics

### Using the Enhanced Functions

```python
from bs4 import BeautifulSoup
from functions import extract_company_urls, extract_company_profile_urls, extract_company_emails

# Parse HTML
with open("page1.html", encoding='utf-8', mode='r') as file:
    bs = BeautifulSoup(file, 'lxml')

# Extract new data fields
company_urls = extract_company_urls(bs)
profile_urls = extract_company_profile_urls(bs)
emails = extract_company_emails(bs)
```

## 📈 Findings

* About 30 firms are rated 5 star while 12 are rated between 4.8 - 4.9
* Very few firms (3) has a review above 30
* Most of the firms are located in United States followed by India
* **NEW**: Company website URLs extracted for companies that provide them on listing pages
* **NEW**: GoodFirms profile URLs available for 145 out of 153 companies

## 📁 Files

* `functions.py` - Enhanced extraction functions (updated with new features)
* `enhanced_scraper_full.py` - Complete scraper with all new features
* `enhanced_extracted.csv` - Output file with all extracted data
* `top_da_company.ipynb` - Original Jupyter notebook
* `page1.html`, `page2.html`, `page3.html` - Downloaded HTML pages
* `extracted.csv` - Original extracted data
* `clean_extraction.csv` - Cleaned original data

## 🛠️ Technologies Used

* **Python 3.11**
* **BeautifulSoup4** - HTML parsing
* **Requests** - HTTP requests
* **Pandas** - Data manipulation
* **Plotly** - Data visualization

## 📝 Notes

* Company email addresses are typically not displayed on public listing pages for privacy reasons
* Company URLs are extracted where available; some companies may not have direct website links on the listing page
* Profile URLs can be used to access additional company information on GoodFirms

## 🚀 Enhancements Made

1. Added `extract_company_urls()` function to extract company website URLs
2. Added `extract_company_profile_urls()` function to get GoodFirms profile links
3. Added `extract_company_emails()` function (returns N/A as emails not available on listing pages)
4. Created `enhanced_scraper_full.py` for complete data extraction
5. Updated README with comprehensive documentation

## 👤 Author

Original Project: TelRich  
Enhanced Version: mostdanger

## 📄 License

This project is open source and available for educational purposes.

