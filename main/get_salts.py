from bs4 import BeautifulSoup
# import requests
import sys
import pandas as pd


sys.stdout.reconfigure(encoding='utf-8')


df = pd.read_csv('main/salts.csv', encoding='utf-8-sig', sep='~')
pd.set_option('display.max_columns', None)

def get_medicine_name(general_medicine_name):
    filt = df['Generic Name'].str.contains(general_medicine_name, case=False, na=False) & (df['MRP(in Rs.)'] != "Under Process")
    mini_df = df.loc[filt]
    return mini_df

def get_medicines_group(group_name):
    filt = df['Group Name'].str.contains(group_name, case=False, na=False) & (df['MRP(in Rs.)'] != "Under Process")
    mini_df = df.loc[filt]
    return mini_df





"""

# The following code was used for the creation of salts.html file using the URL below which is the raw data used for the dataset
# It sends a POST request to the said URL to invoke it and provide the raw data for the data set
# The provided raw data was in the form of an HTML document which was copied to salts.html to be used in this project


# URL of the form submission endpoint
url = 'https://janaushadhi.gov.in/SortingView.aspx'

# Headers for the request
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ASP.NET_SessionId=ovf2sekbas5rvxia0vtsiy2n',
    'Origin': 'https://janaushadhi.gov.in',
    'Referer': 'https://janaushadhi.gov.in/SortingView.aspx',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"'
}

# Form data for the POST request
data = {
    '__VIEWSTATE': '/wEPDwUKMTI5Nzk4ODg3NGRkGzUaI7Wd7EBVSmM+H/MAgsjYoaLlNSxAOfjTe8RnVus=',
    '__VIEWSTATEGENERATOR': '8287F55C',
    '__EVENTVALIDATION': '/wEdAAhUBzrDhY5/OzrgxjQLUXts7Vx/6Hzjl1oQ7GNre2WFjGEImxyoblOoObEGtlTt2/PM03OrTA3aZhgYPB6sRmC65++QxfwDvzhrmxLUsU0dgOMaSEHoJOa9om1WXkxclQci/XgaNgQLL8inBuDY7TMrkeC45EeSLC/WEVXavD4b8INhqxIlQ/mtNR6b274SaVL1zYvBO+js6D5E2Wfgf1LT',
    'ctl00$Bppi_body$ddlProduct': 'MRP1 ASC',
    'ctl00$Bppi_body$btnSearch': 'Search'
}

# Send the POST request
response = requests.post(url, headers=headers, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the entire HTML content of the response
    print(response.text)
    
    # Optionally, save the HTML content to a file
    with open('main/salts.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
"""


r"""
# The following code was used for the generation of the salts.csv file which was made from the raw data available in salts.html
# This allows the usage of the pandas module for easier handling of data
with open('main/salts.html', 'r') as file:
    r = file.read()

soup = BeautifulSoup(r, 'html.parser')

count=0
s=''
for data in soup.find_all('td'):
    count +=1 
    content = data.get_text()
    if count % 6 == 0:
        s = s+content+'\n'
    else:
        s = s+content+'~'

with open('main/salts.csv', 'w') as f:
    f.write(s)
"""
