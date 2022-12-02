max = 0
sum = 0
with open('Day 1\source.txt','r') as file:
    for line in file:
        if(line == '\n'):
            if(sum > max):
                max = sum
            sum = 0
        else:
            sum += int(line)
print(max)