# Import necessary library
import pandas as pd
import re

"""
The blow function can extract the following firm details from the html tags:
Position, Names (pass in the list starting from the 4th item), Motors, Reviews,
Prices, Employess, Year founded, and Location 
"""
def extract_detail(name, tag_lst):
    lst = [tag.text for tag in tag_lst]
    print(f"The number of firm {name} extracted is {len(lst)}")
    return pd.Series(lst)

""" The below are individual functions to extract each firm details"""

def extract_position(tag_lst):
    pos_lst = [pos.text for pos in tag_lst]
    print(f"The number of firm pos extracted is {len(pos_lst)}")
    return pd.Series(pos_lst)

def extract_names(tag_lst):
    names_lst = [name.text for name in tag_lst[3:]]
    print(f"The number of firm name extracted is {len(names_lst)}")
    return pd.Series(names_lst)

def extract_motors(tag_lst):
    motor_lst = [motor.text for motor in tag_lst]
    print(f"The number of firm motor extracted is {len(motor_lst)}")
    return pd.Series(motor_lst)

def extract_reviews(tag_list):
    review_lst = [review.text for review in tag_list]
    print(f"The number of review extracted is {len(review_lst)}")
    return pd.Series(review_lst)

def extract_progress_values(tag_lst):    
    service_pct = [percent[1].text for percent in enumerate(tag_lst) if percent[0]%2 ==0]
    platform_pct = [percent[1].text for percent in enumerate(tag_lst) if percent[0]%2 ==1]       
    print(f"The number of service percent is {len(service_pct)}")
    print(f"The number of platform percent is {len(platform_pct)}")
    return pd.Series(service_pct), pd.Series(platform_pct) 

def exttract_prices(tag_lst):    
    price_lst = [price.text for price in tag_lst]
    print(f"The number of price extracted is {len(price_lst)}")
    return pd.Series(price_lst)

def extract_employees(tag_lst):
    emps_lst = [emp.text for emp in tag_lst]
    print(f"The number of employees extracted is {len(emps_lst)}")
    return pd.Series(emps_lst)

def extract_founded_year(tag_lst):    
    year_lst = [year.text for year in tag_lst]
    print(f"The number of year extracted is {len(year_lst)}")
    return pd.Series(year_lst)

def extract_locations(tag_lst):
    firm_lst = [firm.text for firm in tag_lst]
    print(f"The number of locations extracted is {len(firm_lst)}")
    return pd.Series(firm_lst)

"""
NEW FUNCTIONS: Extract company URLs and emails
Added by: Enhanced Scraper
"""

def extract_company_urls(bs):
    """
    Extract company website URLs from the BeautifulSoup object
    
    Args:
        bs: BeautifulSoup object of the parsed HTML page
        
    Returns:
        pd.Series: Series containing company website URLs
    """
    company_urls = []
    
    # Find all company names (skip first 3 which are navigation elements)
    company_names = bs.find_all('span', {'itemprop': 'name'})[3:]
    
    # For each company, find the associated website URL
    for name_tag in company_names:
        # Navigate up to find the company card container
        container = name_tag.find_parent('div', {'class': re.compile(r'providers.*|company.*|firm.*')})
        if not container:
            # Try broader search - go up the DOM tree
            container = name_tag.find_parent('div')
            # Keep going up until we find a substantial container
            for _ in range(5):
                if container and len(str(container)) > 1000:
                    break
                if container:
                    container = container.find_parent('div')
        
        url = "N/A"
        if container:
            # Look for external links (company websites)
            links = container.find_all('a', href=True)
            for link in links:
                href = link['href']
                # Company websites are external links not pointing to goodfirms
                if href.startswith('http') and 'goodfirms.co' not in href:
                    url = href
                    break
        
        company_urls.append(url)
    
    print(f"The number of company URLs extracted is {len(company_urls)}")
    return pd.Series(company_urls)

def extract_company_profile_urls(bs):
    """
    Extract GoodFirms profile URLs for each company
    
    Args:
        bs: BeautifulSoup object of the parsed HTML page
        
    Returns:
        pd.Series: Series containing GoodFirms profile URLs
    """
    profile_urls = []
    company_names = bs.find_all('span', {'itemprop': 'name'})[3:]
    
    for name_tag in company_names:
        # Find the link that wraps or is near the company name
        parent_link = name_tag.find_parent('a', href=True)
        if parent_link and '/company/' in parent_link['href']:
            profile_url = parent_link['href']
            if not profile_url.startswith('http'):
                profile_url = 'https://www.goodfirms.co' + profile_url
            profile_urls.append(profile_url)
        else:
            profile_urls.append("N/A")
    
    print(f"The number of profile URLs extracted is {len(profile_urls)}")
    return pd.Series(profile_urls)

def extract_company_emails(bs):
    """
    Extract company email addresses from the BeautifulSoup object
    Note: Email addresses are typically not displayed on listing pages
    This function returns "N/A" for all entries as a placeholder
    
    Args:
        bs: BeautifulSoup object of the parsed HTML page
        
    Returns:
        pd.Series: Series containing company email addresses (or "N/A")
    """
    company_names = bs.find_all('span', {'itemprop': 'name'})[3:]
    
    # Email addresses are not typically shown on listing pages
    # Would need to visit individual company profile pages to extract emails
    # For now, return N/A for all companies
    emails = ["N/A"] * len(company_names)
    
    print(f"The number of company emails extracted is {len(emails)} (Note: Emails not available on listing page)")
    return pd.Series(emails)

