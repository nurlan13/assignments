import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    # Write Header
    writer.writerow(['col1', 'col2'])
    # Write Data 
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])