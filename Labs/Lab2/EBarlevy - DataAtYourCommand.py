#use a list of dictionaries
import json
filename = 'db.json'
people = []

def getFormattedData(filename):
    with open(filename, 'r') as f:
        return f.read()

def writeToFile(dictionary, filename):
    currentData = getFormattedData(filename)
    with open(filename, 'w') as f:
        if len(currentData) > 38:
            formattedData = currentData[:-7] + ',' + json.dumps(dictionary, indent=4) + currentData[-7:]
        elif len(currentData) < 38:
            print("Imporoperly formatted file")
            return
        else:
            formattedData = currentData[:-7] + json.dumps(dictionary, indent=4) + currentData[-7:]
        f.write(formattedData)

def readFromFile(filename):
    with open(filename, 'r') as f:
        data = f.read()
        if len(data) > 0:
            return json.loads(data)
        else:
            return 'No json data found'

def createDictionary(fName, lName, phone):
    dictionary = {}
    dictionary['FirstName'] = fName
    dictionary['LastName'] = lName
    dictionary['PhoneNumber'] = phone
    return dictionary

while True:
    print('')
    print('Welcome to the Contact Database!')
    print('')
    print('Commands:')
    print('add [fname] [lname] [phone]   - adda new record')
    print('list                          - lists all records')
    print('find [value]                  - show the first matching record')
    print('del [value]                   - removes the first matching record')
    print('quit                          - quit the program')
    print('')

    command = input(':: ')

    match command[0]:
        case 'a':
            commandList = command.split()
            if len(commandList) == 4:
                writeToFile(createDictionary(commandList[1], commandList[2], commandList[3]), filename)
            else:
                print("Incorrect Number of Parameters")
        case 'l':
            print(readFromFile(filename))
        case 'f':
            
        case 'd':
            print('del')
        case 'q':
            break
        case default:
            print('Invalid Input')