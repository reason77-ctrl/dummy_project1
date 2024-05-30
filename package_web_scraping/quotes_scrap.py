import requests
from bs4 import BeautifulSoup
import json
import logging
import os

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Function to get the last successfully processed page
def get_last_page(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                last_page = int(file.read())
                return last_page
            except ValueError:
                return 0
    return 0

# Function to save the last successfully processed page
def save_last_page(filename, page):
    with open(filename, 'w') as file:
        file.write(str(page))

def get_data():
    quotes = []
    author = []
    last_page_file = 'last_page.txt'
    start_page = get_last_page(last_page_file)
    
    for i in range(start_page + 1, 11):
        url = f'https://quotes.toscrape.com/page/{i}/'
        try:
            r = requests.get(url)
            r.raise_for_status()  # Raise HTTPError for bad responses
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error occurred while accessing {url}: {e}")
            break  # Exit the loop to avoid further processing

        try:
            soup = BeautifulSoup(r.text, 'lxml')
            data = soup.find_all('div', 'quote')
            
            for quote_div in data:
                b = quote_div.find('span', 'text')
                if b:
                    quotes.append(b.text)
                else:
                    logging.error(f"Quote text not found on page {i}")
                
                a = quote_div.find('small')
                if a:
                    author.append(a.text)
                else:
                    logging.error(f"Author not found on page {i}")

            # Save the last successfully processed page
            save_last_page(last_page_file, i)
        
        except Exception as e:
            logging.error(f"Error parsing content from {url}: {e}")
            break  # Exit the loop to avoid further processing
    
    result = [{key: value} for key, value in zip(author, quotes)]
    return result

def convo_json():
    result = get_data()
    try:
        with open('quotes3.json', 'w') as data_file:
            json.dump(result, data_file, indent=2) 
    except IOError as e:
        logging.error(f"Error writing to file: {e}")
    return result

# Execute the function
convo_json()

