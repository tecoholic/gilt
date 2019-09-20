import json
import csv

infile = "UTI GILT Fund.json"
outfile = "UTI GILT Fund.csv"

with open(infile) as inf, open(outfile, "w") as ouf:
    data = json.load(inf)
    writer = csv.DictWriter(ouf, fieldnames=["date", "nav"])
    writer.writeheader()
    for item in data:
        writer.writerow(item)

