from tkinter import *
from tkinter import ttk
import random

form = Tk()
form.title('A GUI To Remember')
form.geometry('400x300')

questions = []
points = 0

def addQuestions():
    global questions
    questions.clear()
    questions.append((1775, 'the start of the Revolutionary War'))
    questions.append((1783, 'the United States Constitution signed'))
    questions.append((1865, 'President Lincoln assasinated'))
    questions.append((1998, 'Unreal Engine released'))
    questions.append((1939, 'the beginning of World War II'))
    questions.append((1975, 'the first computer introduced'))
    questions.append((1989, 'the Berlin Wall taken down'))
    questions.append((2020, 'the world shut down from COVID-19'))
    questions.append((1914, 'the start of World War I'))
    questions.append((1789, 'the start of the French Revolution'))
    random.shuffle(questions)

addQuestions()

def startGame():
    lblQuestion.config(text=f'What year was {(questions[0])[1]}?')
    lblSubtitle.place_forget()
    btnPlay.place_forget()
    btnCancel.place_forget()
    btnNextQuestion.place_forget()
    lblError.config(text='')
    entrAnswer.delete(0, 'end')
    lblQuestion.place(x=20, y=60)
    entrAnswer.place(x=320, y=60)
    btnSubmit.place(x=150, y=90)
    lblError.place(x=150, y=120)
    lblCurrentScore.place(x=250, y=150)

def submitButton():
    global points
    answer = entrAnswer.get()
    if answer.isdigit() and len(answer) == 4:
        lblError.config(text='')
        if int(answer) == (questions[0])[0]:
            points += 10
            lblError.config(text='Exactly Correct! +10pts')
        elif int(answer) <= (questions[0])[0] + 5 and int(answer) >= (questions[0])[0] - 5:
            points += 5
            lblError.config(text='Pretty close. +5pts')
        elif int(answer) <= (questions[0])[0] + 10 and int(answer) >= (questions[0])[0] - 10:
            points += 2
            lblError.config(text='Not bad. +2pts')
        elif int(answer) <= (questions[0])[0] + 20 and int(answer) >= (questions[0])[0] - 20:
            points += 1
            lblError.config(text='Kind of close. +1pt')
        else:
            lblError.config(text='Quite far off. +0pts')
        btnNextQuestion.place(x=140, y=150)
        lblCurrentScore.config(text=points)
    else:
        lblError.config(text='Invalid Year')

def gameOver():
    lblSubtitle.config(text=f'You earned {points} points!')
    lblSubtitle.place(x=130, y=40)
    lblError.config(text='Want to play again?')
    lblError.place(x=130, y=70)
    lblQuestion.place_forget()
    btnNextQuestion.place_forget()
    entrAnswer.place_forget()
    btnSubmit.place_forget()
    lblCurrentScore.place_forget()
    btnPlay.place(x=100, y=100)
    btnCancel.place(x=200, y=100)
    addQuestions()


def nextQuestionButton():
    global questions
    if len(questions) > 1:
        questions.pop(0)
        startGame()
    else:
        gameOver()

lblTitle = ttk.Label(form, text='A GUI To Remember Quiz')
lblTitle.place(x=120, y=10)
lblSubtitle = ttk.Label(form, text='Want to play a game?')
lblSubtitle.place(x=130, y=40)
btnPlay = ttk.Button(form, text='Yes', command=startGame)
btnPlay.place(x=100, y=70)
btnCancel = ttk.Button(form, text='No', command=form.destroy)
btnCancel.place(x=200, y=70)

lblQuestion = ttk.Label(form)
entrAnswer = ttk.Entry(form, width='4')
btnSubmit = ttk.Button(form, text='Submit', command=submitButton)

lblError = ttk.Label(form)
lblCurrentScore = ttk.Label(form)

btnNextQuestion = ttk.Button(form, text='Next Question', command=nextQuestionButton)
form.mainloop()