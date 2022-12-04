result = 0
with open('Day 4\source.txt','r') as file:
    my_list = [x.rstrip().split(',') for x in file]
    for lista in my_list:
        a, b = lista[0].split('-')
        c, d = lista[1].split('-')
        a, b, c, d = int(a), int(b), int(c), int(d)
        first = set(range(a, b+1))
        second = set(range(c, d+1))
        result += 1 if first.intersection(second) else 0
print(result)