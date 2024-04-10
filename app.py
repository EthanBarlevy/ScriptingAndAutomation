'''
year = 1899;

if year > 1900:
    print('great year')
elif year == 1899:
    print('best year') 
else:
    print('less year')

for x in range(0, 10):
    print(x)

list = []
list.append('owo')
list.append('uwu')

for item in list:
    print(item)


i = 100;
x = 0;
while x < i:
    x += 1
    print(x)


while True:
    year = input('Enter year: ')

    try:
        int_year = int(year)
        print(int_year)

        if len(str(int_year)) == 4:
            break
        else:
            print('not a valid year')
            continue
    except:
        print('not a valid year')

tuple = (1775, 'The start of the Revolutionary War')

print(tuple[0])
print(tuple[1])
'''

# JSON

'''
import json

dictionary = {}
dictionary['name'] = 'owo'

print(dictionary)

json_dictionary = json.dumps(dictionary) #dump is for file write, dumps is keep as string
print(json_dictionary)

with open('owo.json', 'w') as f:
    f.write(json.dumps(dictionary, indent=4))

with open('owo.json', 'r') as f:
    input = f.read()
    print(input)
    json_dictionary = json.loads(input)

print(json_dictionary["name"])
'''

# REPL
'''
x = input('>>> ')
print(x)
'''

# Dunder variables / functions

'''
print(__name__)
print(__file__)


class repl_class():
    def __init__(self) -> None:
        print('intiting class')

def start_app():
    print('starting')
    r = repl_class()

# these are kinda like preprocessor functions. they allow for running not top to bottom
if __name__ == '__main__':
    start_app()
'''

# tkinter

import tkinter as tk

'''
x = 0
def btnClick():
    global x
    print('owo')
    #lblInfo.configure(text=f'cool story bro {x}') idk why this doesnt work but oh well

form = tk.Tk()
form.title('Practice')
form.geometry('500x300')

#.pack() puts the items in a list
#.grid(column=X, row=Y) its a grid
#.place(x=X, y=Y) coordinates

lblTitle = tk.Label(form, text='OwO').grid(column=0, row=0)
lblInfo = tk.Label(form, text='cool story bro').grid(column=2, row=0)

btnClick = tk.Button(form, text='click', command=btnClick).grid(column=1, row=1)
entrTest = tk.Entry(form, width=4).grid(column=3, row=1)

form.mainloop()

def change_label_text():
    label.config(text="New Text")

# Create the main window
root = tk.Tk()

# Create a label widget
label = tk.Label(root, text="Original Text")
label.pack()

# Create a button to trigger the label text change
button = tk.Button(root, text="Change Label Text", command=change_label_text)
button.pack()

# Run the Tkinter event loop
root.mainloop()
'''

#virtual enviroments
# python -m venv ve
