import csv
from token import RARROW

def read_file():
    with open("Csv_graphQl/data.csv") as data:
        data = csv.reader(data, delimiter=',')
        li = []
        i = 0
        for row in data:
            if (i>0):
                li.append({"name":row[0], "city":row[1], "designation":row[2], "experience_in_years":row[3]})
            i += 1
        return li