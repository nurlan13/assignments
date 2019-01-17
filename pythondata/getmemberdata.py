# Sam and Nurlan
# Read superherees.json
import json
with open('superheroes.json', 'r') as f:
    squad = json.load(f)
members = squad['members']
print(members)

# Write a CSV file
import csv

with open('superheroesbonus.csv', 'w') as f:
	writer = csv.writer(f)
	# Write Header 
	writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])
# Loop over members nad write one row
	for member in members:
		powers= member['powers']
		for power in powers:
			writer.writerow([member['name'],member['age'], member['secretIdentity'], power,squad['squadName'], squad['homeTown'], squad['formed'], squad['secretBase'], squad['active']])
