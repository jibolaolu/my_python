import csv

data = open('pythonusers_1.csv', encoding='utf-8', errors='ignore')
csv_data = csv.reader(data)
data_line = list(csv_data)

for line in data_line[:5]:
    print(line)

#print(data_line[1])
all_emails= []
for aline in data_line[1:]:
    all_emails.append(aline[6])

print(all_emails)

full_names = []
for name in data_line[1:]:
    full_names.append(name[0]+ ' '+name[1])

print(full_names)

#Write to CSV file