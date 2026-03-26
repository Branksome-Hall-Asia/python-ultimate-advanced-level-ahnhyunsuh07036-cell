# --- task_05_csv_intro.py ---
import csv

# EXAMPLE: Reading the first column (Names)
with open("database.txt", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"User: {row[0]}")

# CHALLENGE: Write code below to print ONLY the balances (row index 2).
# Make sure to add a '$' sign before the number!
# ---------------------------------------------------------
