result = 0
with open('Day 3\source.txt','r') as file:
    for line in file:
        first_half  = line[:len(line)//2]
        second_half = line[len(line)//2:]
        for letter in first_half:
            if(second_half.count(letter)):
                if(ord(letter) >= 97 and ord(letter) <= 122):
                    result += ord(letter) - 96
                    break
                elif(ord(letter) >= 65 and ord(letter) <= 90):
                    result += ord(letter) - 38
                    break
print(result)