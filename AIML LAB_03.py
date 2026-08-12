import csv
with open("workload_data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)
header = data[0]
rows = data[1:]
attributes = header[:-1]
target = header[-1]
hypothesis = ["Ø"] * len(attributes)
print("Find-S Algorithm")
print("-" * 50)
for row in rows:
    instance = row[:-1]
    target_value = row[-1]
    if target_value == "Yes":
      for i in range(len(attributes)):
            if hypothesis[i] == "Ø":
                hypothesis[i] = instance[i]
            elif hypothesis[i] != instance[i]:
                hypothesis[i] = "?"

    print("Processed:", row)
    print("Hypothesis:", hypothesis)
    print()
print("-" * 50)
print("Final Most Specific Hypothesis:")
print(hypothesis)