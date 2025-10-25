"""
Enhanced Web Scraper for Top Data Analytics Companies
This script extends the original scraper to include:
- Company Name
- Company URL (website)
- Company Geo (location)
- Company Email (placeholder as not available on listing page)

Author: Enhanced by mostdanger
Date: October 2025
"""

import requests as r
from bs4 import BeautifulSoup
import pandas as pd
from functions import *

# URL links for the three pages
url_link = [
    'https://www.goodfirms.co/big-data-analytics/data-analytics',
    'https://www.goodfirms.co/big-data-analytics/data-analytics?page=2',
    'https://www.goodfirms.co/big-data-analytics/data-analytics?page=3'
]

print("=" * 60)
print("Enhanced Web Scraper for Data Analytics Companies")
print("=" * 60)

# Download pages (commented out - using existing HTML files)
# print("\nDownloading pages...")
# access = [r.get(url) for url in url_link]
# for page in access:
#     index = access.index(page) + 1
#     with open(f'page{index}.html', mode='wb') as file:
#         file.write(page.content)
# print("Pages downloaded successfully!")

# Initialize lists to store all data
all_names = []
all_motors = []
all_reviews = []
all_service_pct = []
all_platform_pct = []
all_prices = []
all_emps = []
all_years = []
all_locations = []
all_company_urls = []
all_profile_urls = []
all_emails = []

# Process each page
for page_num in range(1, 4):
    print(f"\n{'='*60}")
    print(f"Processing Page {page_num}...")
    print(f"{'='*60}")
    
    with open(f"page{page_num}.html", encoding='utf-8', mode='r') as file:
        bs = BeautifulSoup(file, 'lxml')
    
    # Extract existing data
    print("\nExtracting original data fields...")
    firm_names = bs.find_all('span', {'itemprop': "name"})
    firm_motors = bs.find_all('p', {'class': "profile-tagline"})
    firm_reviews = bs.find_all('span', {'class': "listinv_review_label"})
    progress_value = bs.find_all('div', {'class': "circle-progress-value"})
    firm_prices = bs.find_all('div', {'class': "firm-pricing"})
    firm_emps = bs.find_all('div', {'class': "firm-employees"})
    firm_years = bs.find_all('div', {'class': "firm-founded"})
    firm_locations = bs.find_all('div', {'class': "firm-location"})
    
    # Extract data using existing functions
    names = extract_names(firm_names)
    motors = extract_motors(firm_motors)
    reviews = extract_reviews(firm_reviews)
    ser, pct = extract_progress_values(progress_value)
    prices = exttract_prices(firm_prices)
    emps = extract_employees(firm_emps)
    years = extract_founded_year(firm_years)
    locations = extract_locations(firm_locations)
    
    # Extract NEW data fields
    print("\nExtracting new data fields...")
    company_urls = extract_company_urls(bs)
    profile_urls = extract_company_profile_urls(bs)
    emails = extract_company_emails(bs)
    
    # Append to master lists
    all_names.extend(names.tolist())
    all_motors.extend(motors.tolist())
    all_reviews.extend(reviews.tolist())
    all_service_pct.extend(ser.tolist())
    all_platform_pct.extend(pct.tolist())
    all_prices.extend(prices.tolist())
    all_emps.extend(emps.tolist())
    all_years.extend(years.tolist())
    all_locations.extend(locations.tolist())
    all_company_urls.extend(company_urls.tolist())
    all_profile_urls.extend(profile_urls.tolist())
    all_emails.extend(emails.tolist())

# Create enhanced DataFrame with new columns
print(f"\n{'='*60}")
print("Creating enhanced DataFrame...")
print(f"{'='*60}")

df = pd.DataFrame({
    'Company Name': all_names,
    'Company URL': all_company_urls,
    'Tagline': all_motors,
    'Reviews': all_reviews,
    'Service %': all_service_pct,
    'Platform %': all_platform_pct,
    'Pricing': all_prices,
    'Employees': all_emps,
    'Founded': all_years,
    'Company Geo': all_locations,
    'Profile URL': all_profile_urls,
    'Company Email': all_emails
})

# Save to CSV
output_file = 'enhanced_extracted.csv'
df.to_csv(output_file, index=False)

print(f"\n✓ Data extraction complete!")
print(f"✓ Total companies extracted: {len(df)}")
print(f"✓ Output saved to: {output_file}")

# Display sample data
print(f"\n{'='*60}")
print("Sample Data (First 5 rows):")
print(f"{'='*60}")
print(df.head())

print(f"\n{'='*60}")
print("Column Summary:")
print(f"{'='*60}")
for col in df.columns:
    non_na = df[col][df[col] != "N/A"].count()
    print(f"{col:20s}: {non_na}/{len(df)} entries")

