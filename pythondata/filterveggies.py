# Read vegetables.csv into a variable called vegetables.
import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(vegetables) for vegetables in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

print(vegetables)
# Loop through vegetables and filter down to only green vegtables using a whitelist.
green_vegetables = []
whitelist = ['green']
for green_vegetables in vegetables:
    if vegetables['green'] in whitelist:
        green_vegetables.append(vegetables)

print(green_vegetables)
# Print veggies to the terminal
# Write the veggies to a json file called greenveggies.json