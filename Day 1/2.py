temp = 0
elfs = []
with open('Day 1\source.txt','r') as file:
    for line in file:
        if(line == '\n'):
            elfs.append(temp)
            temp = 0
        else:
            temp += int(line)
elfs.sort()
print(sum(elfs[-3::]))