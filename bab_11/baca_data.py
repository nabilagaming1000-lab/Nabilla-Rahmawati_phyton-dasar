
import csv

data = []

with open("nilai.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")
print(data[0])
