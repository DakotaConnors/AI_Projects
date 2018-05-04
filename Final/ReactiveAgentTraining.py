import pickle

training_file = 'RvWMA_1000_4x4.bin'

def loadGameStrings():
    gameStrings = []
    try:
        input_file = open(training_file, 'rb')
        try:
            gameStrings = pickle.load(input_file)
        except (EOFError):
            print("SOMETHING WENT WRONG WHILE LOADING")
    except (FileNotFoundError):
        pass
    #for g in gameStrings:
    #    print(g)
    return gameStrings

def Training(gameStrings):
    moveSets = []
    moveScores = []
    counter = 0
    for g in gameStrings:
        #if counter % 100 == 0: print(str(counter) + ' games analyzed\n' + str(len(moveSets)) + ' total rows in training set')
        winner = g[len(g)-1]
        if winner == 'x': score = 1
        elif winner == 'o': score = -1
        elif winner == 'd': score = 0
        g = g[:-1]
        while len(g) >=6:
            omove = g[0:3]
            xmove = g[3:6]
            g = g[6:]
            foundIt = False
            tempCounter = 0
            for move in moveSets:
                if ((omove in move) and (xmove in move)):
                    foundIt = True
                    moveScores[tempCounter] += score
                tempCounter += 1
            if not(foundIt):
                move = omove + xmove
                moveSets.append(move)
                moveScores.append(score)
        counter += 1
    return moveSets, moveScores

if __name__ == '__main__':
    moveSets, moveScores = Training(loadGameStrings())
    for i in range(len(moveSets)):
        #print(moveSets[i], moveScores[i])
        output_file = open(('ReactiveTraining_' + training_file), "wb")
        pickle.dump(moveSets, output_file)
        pickle.dump(moveScores, output_file)
        output_file.close()
