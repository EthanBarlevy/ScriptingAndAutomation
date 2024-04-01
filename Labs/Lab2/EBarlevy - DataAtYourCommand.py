#use a list of dictionaries
import json
filename = 'db.json'
people = []
peopleDict = {}
peopleDict["People"] = people

def readFromFile(filename):
    with open(filename, 'r') as f:
        data = f.read()
        if len(data) > 0:
            return json.loads(data)
        else:
            return 'No json data found'

def writeToFile(dictionary, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(dictionary, indent=4))

def createDictionary(fName, lName, phone):
    dictionary = {}
    dictionary['FirstName'] = fName
    dictionary['LastName'] = lName
    dictionary['PhoneNumber'] = phone
    return dictionary

def findRecord(value):
    for person in people:
        if person['FirstName'] == value:
            return person
        if person['LastName'] == value:
            return person
        if person['PhoneNumber'] == value:
            return person
    return f'No people found with \'{value}\'.'

def removeRecord(value):
    person = findRecord(value)
    if isinstance(person, str):
        return person
    people.remove(person)
    print(f'\'{value}\' has been removed.')

while True:
    peopleDict = readFromFile(filename)
    if not isinstance(peopleDict, str):
        people = peopleDict["People"]
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
                people.append(createDictionary(commandList[1], commandList[2], commandList[3]))
                writeToFile(peopleDict, filename)
            else:
                print("Incorrect Number of Parameters")
        case 'l':
            print(readFromFile(filename))
        case 'f':
            commandList = command.split()
            if len(commandList) == 2:
                print(findRecord(commandList[1]))
            else:
                print("Incorrect Number of Parameters")
        case 'd':
            commandList = command.split()
            if len(commandList) == 2:
                #print(findRecord(commandList[1]))
                print('del')
            else:
                print("Incorrect Number of Parameters")
        case 'q':
            break
        case default:
            print('Invalid Input')