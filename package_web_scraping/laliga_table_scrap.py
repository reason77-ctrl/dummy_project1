from requests_html import HTMLSession
import json

s = HTMLSession()

url = 'https://www.laliga.com/en-GB/laliga-easports/standing'

r = s.get(url)

table = r.html.find('.show')[0]




table_data = [[c.text for c in row.find('.styled__TextStyled-sc-1mby3k1-0')[2:]] for row in table.find('.styled__StandingTabBody-sc-e89col-0')]

table_header = [[c.text for c in row.find('.styled__TextStyled-sc-1mby3k1-0')[1:]] for row in table.find('.styled__StandingTabHeader-sc-e89col-7')][0]

result = [dict(zip(table_header, t)) for t in table_data]

with open('table.json', 'w') as data_file:
    json.dump(result, data_file, indent=2)


