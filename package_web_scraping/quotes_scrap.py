from bs4 import BeautifulSoup
import requests
import json


quotes = []
author = []
for i in range(1,11):
    url = 'https://quotes.toscrape.com/page/' + str(i) + '/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')

    data = soup.find_all('div', 'quote')


    
    for i in data:
        b = i.find('span','text')
        quotes.append(b.text)



    
    for i in data:
        a = i.find('small')
        author.append(a.text)



result = [{key: value} for key, value in zip(author, quotes)]


with open('quotes.json', 'w') as data_file:
    json.dump(result, data_file, indent=2)
    


