fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for i in line.rstrip().split():
        lst.append(i)
lst = list(set(lst))
lst.sort()
print(lst)
