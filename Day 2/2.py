opponentChoices = { 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors' }
expectedChoices = { 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win' }

points = 0
with open('Day 2\source.txt','r') as file:
    for line in file:
        temp = line.split()
        match expectedChoices[temp[1]]:
            case 'Lose':
                if(opponentChoices[temp[0]] == 'Rock'):
                    points += 3
                elif(opponentChoices[temp[0]] == 'Paper'):
                    points += 1
                elif(opponentChoices[temp[0]] == 'Scissors'):
                    points += 2
            case 'Draw':
                points += 3
                if(opponentChoices[temp[0]] == 'Rock'):
                    points += 1
                elif(opponentChoices[temp[0]] == 'Paper'):
                    points += 2
                elif(opponentChoices[temp[0]] == 'Scissors'):
                    points += 3
            case 'Win':
                points += 6
                if(opponentChoices[temp[0]] == 'Rock'):
                    points += 2
                elif(opponentChoices[temp[0]] == 'Paper'):
                    points += 3
                elif(opponentChoices[temp[0]] == 'Scissors'):
                    points += 1
print(points)

    