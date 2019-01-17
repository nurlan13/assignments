# Read vegtables.csv into a variable called vegtables.
import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(vegetables) for vegetables in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

print(vegetables)
# Group vegtables by color as a variable vegtables_by_color.
vegetables_by_color = {}
for vegetables_by_color in vegetables:
    color = vegetables['color']
    if color in vegetables_by_color:
        vegetables_by_color[make].append(vegetables)
    else:
        vegetables_by_color = [vegetables]


# Output vegtables_by_color into a json called vegtables_by_color.json.