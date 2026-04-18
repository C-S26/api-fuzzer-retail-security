import csv
from datetime import datetime

def log(payload, result):
    with open("results.csv", "a", newline="") as file:
        writer =  csv.writer(file)
        writer.writerow([
         datetime.now(),
         payload,
         result,
         "HIGH" if "Flaw" in result or "Crash" in result else "LOW"
        ])