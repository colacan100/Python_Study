name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    else:
        sline = line.split()
        timeline = sline[5].split(':')
        hour = timeline[0]
        count[hour]=count.get(hour,0)+1
value=count.items()
nvalue = sorted(value)
for (v,k) in nvalue:
    print(v,k)
