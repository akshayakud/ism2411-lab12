
#Reflection 1:
#Python can automate repetitive tasks and process large amounts of data.
#Excel is easier for visualizing data and making quick manual changes.

#Reflection 2:
#A business could use an append-mode log to record daily sales totals.
#Append mode adds new information without deleting previous records.

import csv
from datetime import datetime

# Exercise 1

INPUT_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"


# Exercise 2

with open(INPUT_FILE, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3

with open(INPUT_FILE, "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    sales_rows = []

    for row in reader:
        print(row)
        sales_rows.append(row)


# Exercise 4

total_revenue = 0

for row in sales_rows:
    product = row[0]
    price = float(row[1])
    quantity = int(row[2])

    order_total = price * quantity
    total_revenue += order_total

    print(f"{product}: {quantity} units × ${price:.2f} = ${order_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5

rows_written = 0

with open(CLEANED_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in sales_rows:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        order_total = price * quantity

        if order_total > 100:
            writer.writerow([product, price, quantity, order_total])
            rows_written += 1

print(f"Rows written: {rows_written} of {len(sales_rows)}")


# Exercise 6

dictreader_total = 0

with open(INPUT_FILE, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        order_total = price * quantity

        dictreader_total += order_total

print(f"DictReader total revenue: ${dictreader_total:.2f}")

# csv.reader uses column positions, while DictReader uses column names.
# DictReader is easier to read when working with CSV files that have headers.


# Exercise 7

sales_summary = {}

with open(INPUT_FILE, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        order_total = price * quantity

        if product in sales_summary:
            sales_summary[product] += order_total
        else:
            sales_summary[product] = order_total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# Exercise 8

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(LOG_FILE, "a") as file:
    file.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")

print("Run successfully added to log file!")
