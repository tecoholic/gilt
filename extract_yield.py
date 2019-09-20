import csv
from bs4 import BeautifulSoup

with open("yields.html", "r") as f:
    soup = BeautifulSoup(f)

outfile = open("yields.csv", "w")
headings = [h["data-col-name"] for h in soup.table.thead.tr.find_all('th')]
writer = csv.writer(outfile)
writer.writerow(headings)

for row in soup.table.tbody.find_all('tr'):
    cells = row.find_all("td")
    values = [c.string.replace("%", "").replace(",", "") for c in cells]
    writer.writerow(values)

outfile.close()