# Use the file name mbox-short.txt as the file name
fh = open("S:\Edu\Python Data Structures and Algorithms\Python Fundamentals\mbox-short.txt")

counter = 0
tempNum = 0
num = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
        
    tempNum = float(line[21:27])
    num.append(tempNum) 
	
    counter = counter + 1
    
def rets(a):
    s = 0
    for i in a:
        s = s + i
        
    return s
    
avg = 0
res = rets(num)
avg = res/counter
print("Average spam confidence:", avg)