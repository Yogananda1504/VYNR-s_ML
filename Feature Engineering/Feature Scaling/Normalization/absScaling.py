import csv
import random

random.seed(0)

with open('absScaling.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Feature1', 'Feature2', 'Feature3'])
    for _ in range(20):
        row = [random.choice([0, random.uniform(-10, 10)]) for _ in range(3)]
        writer.writerow(row)