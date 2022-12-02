OpponentChoices = { 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors' }
MyChoices = { 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }

points = 0
with open('Day 2\source.txt','r') as file:
    for line in file:
        temp = line.split()
        match MyChoices[temp[1]]:
            case 'Rock':
                points += 1
                if(OpponentChoices[temp[0]] == 'Rock'):
                    points += 3
                elif(OpponentChoices[temp[0]] == 'Paper'):
                    points += 0
                elif(OpponentChoices[temp[0]] == 'Scissors'):
                    points += 6
            case 'Paper':
                points += 2
                if(OpponentChoices[temp[0]] == 'Rock'):
                    points += 6
                elif(OpponentChoices[temp[0]] == 'Paper'):
                    points += 3
                elif(OpponentChoices[temp[0]] == 'Scissors'):
                    points += 0
            case 'Scissors': 
                points += 3
                if(OpponentChoices[temp[0]] == 'Rock'):
                    points += 0
                elif(OpponentChoices[temp[0]] == 'Paper'):
                    points += 6
                elif(OpponentChoices[temp[0]] == 'Scissors'):
                    points += 3
print(points)

    