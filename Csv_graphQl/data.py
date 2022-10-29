import csv

def read_file():
    with open("Csv_graphQl/data.csv") as data:
        data = csv.reader(data, delimiter=',')
        li = []
        i = 0
        for row in data:
            i += 1
            if (i>0):
                li.append({"name":row[0], "city":row[1], "designation":row[2], "experience_in_year":row[3]})
        return li

read_file()