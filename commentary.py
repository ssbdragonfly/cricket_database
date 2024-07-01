import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/india-vs-south-africa-final-1415755/ball-by-ball-commentary"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

commentary_data = []

for comment in soup.find_all('div', class_='commentary-item'):
    over_count = comment.find('div', class_='over-count').text.strip()
    shot_type = comment.find('div', class_='shot-type').text.strip()
    commentary_data.append({'over': over_count, 'shot': shot_type})

df = pd.DataFrame(commentary_data)
df.to_csv('commentary_data.csv', index=False)
