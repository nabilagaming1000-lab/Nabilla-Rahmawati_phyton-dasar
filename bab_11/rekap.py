
import csv

data = []

with open("nilai.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

rekap = {}

for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")

for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")
