import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import warnings
import subprocess
import os
import re

# Suppress BeautifulSoup XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

# Prevent system sleep using caffeinate
caffeinate_process = subprocess.Popen(["caffeinate", "-d"])  # Keeps Mac awake during script execution

def get_faculty_info(profile_url):
    try:
        # Send a request to the profile page
        response = requests.get(profile_url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the department affiliation
        department_heading = soup.find("dt", class_="heading", string="Department")
        department_section = department_heading.find_next_sibling("dd", class_="detail") if department_heading else None
        department = department_section.get_text(strip=True) if department_section else "Department not found"
        
        # Locate faculty name
        name_section = soup.find("h1", id="faculty_name")
        faculty_name = name_section.find("span", itemprop="name").get_text(strip=True) if name_section else "Name not found"
        
        # Remove degrees from extracted faculty name
        for degree in degrees:
            faculty_name = faculty_name.replace(degree, "").strip()
        
        # Extract nickname if present within quotes or parentheses
        nickname_match = re.search(r'“(.*?)”|\((.*?)\)', faculty_name) 
        nickname = nickname_match.group(1) if nickname_match and nickname_match.group(1) else (nickname_match.group(2) if nickname_match and nickname_match.group(2) else "")
        
        return faculty_name, department, nickname
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching page: {e}", "", ""

def setup_driver():
    service = Service("/opt/homebrew/bin/chromedriver")  # Adjust path if needed
    return webdriver.Chrome(service=service)

driver = setup_driver()

# Base URL
base_url = "https://profiles.utsouthwestern.edu/profile/atoz-search.html?phrase={}&searchType=atoz"
profile_base_url = "https://profiles.utsouthwestern.edu"

# Letters A-Z
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Degrees to remove 
degrees = [
    "M.D., Ph.D., M.B.A.", "M.D., M.S., Ph.D.", "M.D., Ph.D., M.P.H.", "DrPH, M.P.H., M.S.", "M.P.H., Ph.D., M.B.B.S.", "M.D., M.B.A., SC.M.", "M.P.H., Ph.D., M.D.",
    "Ph.D., D.V.M.", "M.P.A.S., DrPH", "D.M.D., M.S.", "L.P.T., D.P.T.", "D.O., M.P.H.", "D.P.T., Ph.D.", "Ph.D., PHARM.D.", "D.D.S., M.D.", "M.D., Pharm.D.", "M.D., M.M.Sc.",
    "M.D., M.S.", "M.D., M.P.H.", "M.P.T., Ph.D.", "D.M.D, Ph.D.", "PHARM.D., Ph.D.", "M.D., M.B.A.", "D.V.M., Ph.D.", "D.V.M., M.S.", "D.D.S., M.D.", "Ph.D., M.S.",
    "M.S., Ph.D.", "D.O., M.S.", "D.O., Ph.D.", "Ph.D., M.P.H.", "M.H.A., Ph.D.", "D.P.M., M.P.H.", "D.O., M.S.", "M.B.A., M.D.", "D.O., P. A.", "M.P.A.S., DMSc",
    "M.P.H., Ph.D.", "J.D., Ph.D.", "O.D., Ph.D.", "M.P.A.S.", "D.D.S., Ph.D.", "M.D., Ph.D.", "PHARM.D., Ph.D.", "Ph.D., R.N.", "L.M.S.W.", "M.S.N.", "M.M.Sc.", "M.S.S.W",
    "M.S.", "Psy.D.", "D.V.M.", "PHARM.D.", "Pharm.D.", "R.N.", "M.B.A.", "P.A.", "J.D.", "DrPH", "D.V.M.", "D.D.S.", "DMSc", "MHS", "D.M.D.",
    "M.A.", "Au.D.", "M.L.I.S.", "D.P.M.", "D.P.T.", "D.O.", "Ed.D.", "D.H.A.", "M.P.H.", "O.D.", "M.Ed.", "C.O.", "Ph.D.", "M.D."
]

# Store extracted data
faculty_data = []

# Loop through each letter
for letter in letters:
    print(f"Scraping letter {letter}...")
    department_not_found_count = 0
    
    try:
        # Load the faculty directory for each letter
        url = base_url.format(letter)
        driver.get(url)

        # Wait for names to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )

        # Scroll multiple times to ensure all names load
        for _ in range(3):  
            try:
                if driver.service.is_connectable():
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(3)
            except Exception as e:
                print(f"Scrolling failed: {e}")
                break

        # Extract faculty names and profile links, filtering out navigation links
        faculty_elements = [
            element for element in driver.find_elements(By.XPATH, "//a[contains(@href, '/profile/')]")
            if "profile" in element.get_attribute("href")  # Only keep actual faculty profiles
        ]

        for element in faculty_elements:
            full_name = element.text.strip()
            
            # Remove degrees
            for degree in degrees:
                full_name = full_name.replace(degree, "").strip()
            
            profile_url = element.get_attribute("href")
            if not profile_url.startswith("http"):
                profile_url = profile_base_url + profile_url  # Ensure correct URL prefix

            # Split last name, first name
            if "," in full_name:
                last_name, first_name = full_name.split(",", 1)
                first_name = first_name.strip()
                last_name = last_name.strip()
            else:
                last_name, first_name = full_name, ""

            # Fetch faculty name, department, and nickname using the profile page
            name_compare, department, nickname = get_faculty_info(profile_url)
            
            # Compare extracted name to first + last name
            is_same = "Yes" if name_compare.lower() == f"{first_name} {last_name}".lower() else "No"
            
            if department != "Department not found":
                faculty_data.append(["University of Texas Southwestern Medical Center", first_name, "", last_name, nickname, department, profile_url, name_compare, is_same])
            else:
                department_not_found_count += 1
        
        print(f"Extracted {len(faculty_elements)} names for letter {letter}")
        print(f"{department_not_found_count} profiles had 'Department not found' for letter {letter}")
        time.sleep(2)
    
    except Exception as e:
        print(f"Error occurred for letter {letter}: {e}")
        driver.quit()
        driver = setup_driver()

# Close browser
driver.quit()

# Save to Excel
save_path = "/Users/elliehozhabri/Documents/Scripts/UTSW_Faculty_Names.xlsx"
df = pd.DataFrame(faculty_data, columns=["University", "First", "Middle", "Last", "Nickname", "Department", "Link", "Name Compare", "IsSame"])
df.to_excel(save_path, index=False)

# Stop preventing sleep
caffeinate_process.terminate()

print(f"Excel file created: {save_path}")
