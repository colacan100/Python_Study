name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

histogram = dict()

for line in handle:
    if not line.startswith('From:'):
        continue
    else:
        sline = line.split()
        email = sline[1]
        histogram[email] = histogram.get(email,0) + 1

bigcount = None
bigemail = None
for mail,count in histogram.items():
    if bigcount is None or count > bigcount:
        bigemail = mail
        bigcount = count
print(bigemail, bigcount)
