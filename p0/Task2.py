"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phones = dict()
for row in calls:
    if row[2][3:10] == "09-2016":
        if row[0] not in phones:
            phones[row[0]] = int(row[3])
        else:
            phones[row[0]] += int(row[3])
        if row[1] not in phones:
            phones[row[1]] = int(row[3])
        else:
            phones[row[1]] += int(row[3])

phoneKey = ''
longest = 0
for key in phones:
    if longest < phones[key]:
        longest = phones[key]
        phoneKey = key

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(phoneKey, longest))
