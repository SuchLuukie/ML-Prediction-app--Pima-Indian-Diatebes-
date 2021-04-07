import csv
import json

results = []
with open("dataset.csv") as csvfile:
	reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
	for row in reader: # each row is a list
		results.append(row)

def writeJSON(url, data):
	with open(url, "w") as write_file:
		json.dump(data, write_file, indent=4)

targets = []
amount = 0
for row in results:
	amount += 1
	target = row[-1]
	targets.append(target)
	row.remove(target)

print(amount)

dataset = {"data": results, "targets": targets}
writeJSON("./dataset.json", dataset)
