import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow(["1000", "1", "100"])
    writer.writerow(["2000", "2", "200"])
    writer.writerow(["3000", "3", "300"])
    writer.writerow(["4000", "4", "400"])


with open("data.csv") as file:
    reader = csv.reader(file)
   # print(list(reader))
    for row in reader:
        print(row)
