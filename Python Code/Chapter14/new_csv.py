import csv

# read csv
with open("file.csv", newline="", encoding="cp950") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row[1].title())

# write csv
with open("new.csv", mode="a", newline="", encoding="cp950") as f:
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerows([['d', 'e', 'f']])
