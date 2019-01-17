# Read superherees.json
import json
with open('superheroes.json', 'r') as f:
    squad = json.load(f)
members = squad['members']
print(members)

# Write a CSV file
import csv

with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	# Write Header 
	writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])
	for member in members: 
		writer.writerow([member['name'],member['age'], member['secretIdentity'], str(member['powers']),squad['squadName'], squad['homeTown'], squad['formed'], squad['secretBase'], squad['active']])
# Loop over members nad write one row