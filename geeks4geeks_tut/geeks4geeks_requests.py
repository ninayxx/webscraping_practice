import requests #needs to be installed using pip 
from bs4 import BeautifulSoup #needs to be installed using pip 
import csv #part of standard python library

url = "https://www.geeksforgeeks.org/" 
r = requests.get(url) #sends HTTP GET request
print(r.status_code) #r.status_code: 200=approved, 403=denied, 404=not found, 500=server error, etc.

soup = BeautifulSoup(r.text, 'html.parser') #reads HTML and parses it by tags

with open('g4g_requests.csv', 'w', newline='') as f: #writes to csv file
    writer = csv.writer(f) #creates CSV writer
    writer.writerow(['Image Source']) #writes column header
    
    for item in soup.find_all('img'): #finds all img tags in HTML 
        writer.writerow([item['src']]) #writes as new row in CSV file