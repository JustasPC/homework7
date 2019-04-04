import random
import json
import datetime

def readFile(filename):
    file = open(filename, "r")
    return file.read()

def writeFile(filename, data):
    file = open(filename, "w")
    file.write(str(data))
    return readFile(filename)


def getScores():
    highscore_data = readFile('highscore.txt')
    scores = json.loads(highscore_data)
    return scores


def addScore(score,name,secret_number):
    score_date = str(datetime.datetime.now())

    score_record = {
        "name":name,
        "number":secret_number,
        "date":score_date,
        "attemps":score
    }
    scores = getScores()
    scores.append(score_record)
    data = json.dumps(scores)
    writeFile('highscore.txt', data)

scores = getScores()

place = 1
print("Sveiki, top rezultatai yra: ")
print("* VIETA**BANDYMAI********DATA*****************_NAME_***Sectret_number__")
for score in scores[:3]:
    print(str(place),"vieta**",score["attemps"],"     *",score["date"],score["name"],'**', score["number"])
    #print(score["date"])
    #print(score["attemps"])
    place+=1



#print("Geriausias rezultatas: " + highscore + ". Permusk jei gali.")
print("-----")
name = input("Koks Jusu vardas?:")
nuo = int(input("Nuo kurio skaiciaus spesim? Kokia intervalo pradzia?"))
iki = int(input("Iki kurio skaiciaus spesim? Kokia intervalo pabaiga?"))
skaicius = random.randint(nuo, iki)
turn = 0
paskutinis_spejimas = 0
# r - read
# w - write (perrasys tai, kas viduje yra)
# a - add write (dades iki to, kas viduje yra)

def checkNumber(numberProvided, numberToGuess):
    if numberProvided == numberToGuess:
        return True
    else:
        return False

while skaicius != paskutinis_spejimas:
    print("Musu skaicius " + str(skaicius))
    turn = turn + 1
    currentTurn = str(turn)
    guess = int(input(currentTurn + " guess. Guess the number:"))

    if checkNumber(guess, skaicius):
        print("Congratulations")
    else:
        print("Try again")
    paskutinis_spejimas = guess

addScore(turn,name, skaicius)

print("Zaidimas baigtas, pabaiga cia")
print("Atspeti tau uztruko " + str(turn) + " spejimus")
