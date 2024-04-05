from bs4 import BeautifulSoup

html_content = ""
with open("table.html", "r") as file:
    for line in file.readlines():
        html_content += line

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')
headers = [header.text.strip() for header in table.find_all('th')]
rows = table.find_all('tr')
with open("teamdata.csv", "w") as file:
    file.write(",".join(headers) + "\n")
    print("\t".join(headers))
    for row in rows[1:]:
        data = [cell.text.strip().replace("\\r\\n", " ") for cell in row.find_all('td')]
        file.write(",".join(data) + "\n")
        print("\t".join(data))
