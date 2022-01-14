# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s=0
c=0
su = float(s)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue 
    num0 = line.find('0')
    num = line[num0:]
    fn = float(num)
    su = su + fn
    c = c+1
avg = su/c

print("Average spam confidence:",str(avg))
