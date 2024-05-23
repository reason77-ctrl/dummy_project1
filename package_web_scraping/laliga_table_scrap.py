from bs4 import BeautifulSoup
import requests
import json
import csv
import pandas as pd

url = BeautifulSoup('https://www.laliga.com/en-GB/laliga-easports/standing', 'html.parser')

response = requests.get(url)

soup = response.text
soup = BeautifulSoup(soup, "lxml")

table_tag = soup.find("div", "show")
# print(table_tag)

tr_header = table_tag.find("div", "styled__StandingTableBody-sc-e89col-5")

table_header = tr_header.find("div", class_="styled__Td-sc-e89col-10")

all_tab_header = table_header.find_next_siblings("div")

heading_data = []
for i in all_tab_header:
    heading_data.append(i.text)


table_contents = table_tag.find_all("div", "styled__StandingTabBody-sc-e89col-0 isRHqh")

final_output = []
for tab_content in table_contents:
    output = []
    for child in tab_content.children:
        output.append(child.text)
    del output[0]
    final_output.append(output)
final_output.insert(0, heading_data)



# with open('corona.csv','w') as f:
#     x = csv.writer(f)
#     for i in b:
#         x.writerow(i)



# df = pd.read_csv('corona.csv', encoding = 'latin1',nrows = 50)

# print(df)

# with open("scrap_data.json", "w") as data_file:
#     json.dump(b, data_file)

