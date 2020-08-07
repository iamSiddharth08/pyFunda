name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()

for line in handle:
    
    if line.startswith("From:"):
        line = line.split()
        app = line[1]
        lst.append(app)

counts = dict()

for word in lst:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word]+1


bigcount = None
bigword = None


for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
        
        
print(bigword, bigcount)
