result = 0
with open('Day 3\source.txt','r') as file:
    my_list = [x.rstrip() for x in file]
    for x in range(0, len(my_list), 3):
        for letter in my_list[x]:
            if(my_list[x+1].count(letter) and my_list[x+2].count(letter)):
                if(ord(letter) >= 97 and ord(letter) <= 122):
                    result += ord(letter) - 96
                    break
                elif(ord(letter) >= 65 and ord(letter) <= 90):
                    result += ord(letter) - 38
                    break
print(result)