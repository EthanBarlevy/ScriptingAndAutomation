import random

questions = []
points = 0

questions.append((1775, 'the start of the Revolutionary War'))
questions.append((1783, 'the United States Constitution signed'))
questions.append((1865, 'President Lincoln assasinated'))
questions.append((1901, 'Theodore Roosevelt\'s first day in office as the President of the United States'))
questions.append((1939, 'the beginning of World War II'))
questions.append((1975, 'the first computer introduced'))
questions.append((1989, 'the Berlin Wall taken down'))
questions.append((2020, 'the world shut down from COVID-19'))
questions.append((1914, 'the start of World War I'))
questions.append((1789, 'the start of the French Revolution'))

random.shuffle(questions)

while True:
    playGame = input('Play Game (y/n): ')
    if playGame == 'y':
        random.shuffle(questions)
        for question in questions:
            while True:
                answer = input(f'What year was {question[1]}?: ')
                try:
                    intAnswer = int(answer)

                    if len(str(intAnswer)) != 4:
                        print('Invalid year')
                    else:
                        if intAnswer == question[0]:
                            print("Exactly correct! +10pts")
                            points += 10
                            break
                        elif intAnswer <= (question[0] + 5) and intAnswer >= (question[0] - 5):
                            print("Pretty close. +5pts")
                            points += 5
                            break
                        elif intAnswer <= (question[0] + 10) and intAnswer >= (question[0] - 10):
                            print("Not bad. +2pts")
                            points += 2
                            break
                        elif intAnswer <= (question[0] + 20) and intAnswer >= (question[0] - 20):
                            print ("Kind of close. +1pt")
                            points += 1
                            break
                        else:
                            print("Too far off. +0pts")
                            break
                except:
                    print("Invalid year")
                    continue
        print()
        print(f'You got {points} points!')
    else:
        break