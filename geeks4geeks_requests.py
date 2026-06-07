import requests 
from bs4 import BeautifulSoup 
import csv

url = "https://www.geeksforgeeks.org/" 
r = requests.get(url) 

soup = BeautifulSoup(r.text, 'html.parser') 
for item in soup.find_all('img'):
    print(item['src'])

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Image Source'])
    
    for item in soup.find_all('img'):
        writer.writerow([item['src']])