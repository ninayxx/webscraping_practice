from urllib.request import urlopen #part of standard python library
from bs4 import BeautifulSoup
import ssl
import csv
#Use requests instead of urllib (see geeks4geeks_requests.py) -- handles certs more gracefully compared to urllib

ssl._create_default_https_context = ssl._create_unverified_context #Bypasses SSL certificate verification

htmldata = urlopen('https://www.geeksforgeeks.org/') #Opens URL and gathers HTML data
soup = BeautifulSoup(htmldata, 'html.parser')

with open('g4g_urllib.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Image Source'])
    
    for item in soup.find_all('img'):
        writer.writerow([item['src']])