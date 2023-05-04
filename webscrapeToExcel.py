#this is a test
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape
url = 'https://www.imdb.com/list/ls024149810/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <div> elements with class "lister-item mode-detail"
movie_divs = soup.find_all('div', class_='lister-item mode-detail')

# Create a CSV file and write the movie titles and years to it
with open('movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
    writer = csv.writer(csvfile)

    writer.writerow(['Rank', 'Title', 'Year', 'Runtime'])  # Write column headers to CSV file
    i = 1

    for div in movie_divs:
        # Extract the title of the movie
        title = div.h3.a.text.strip()
        
        # Extract the year of the movie
        year = div.h3.find('span', class_='lister-item-year').text.strip('()')

        runtime = div.p.find('span', class_='runtime').text.strip()
        rank = str(i)
        # Write the title and year of the movie to the CSV file
        writer.writerow([rank, title, year, runtime])
        i+=1

#reading csv file
csvDataFrame = pd.read_csv('movies.csv')


# putting csv file into excel sheet found in the computer
csvDataFrame.to_excel(r'C:\Users\HarjasSran\OneDrive - AMICO\Documents\MoviesResult.xlsx', sheet_name='Test', index = False)
