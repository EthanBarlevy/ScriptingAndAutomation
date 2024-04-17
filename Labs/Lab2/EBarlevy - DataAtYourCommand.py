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
        if person['FirstName'].lower() == value.lower():
            return person
        if person['LastName'].lower() == value.lower():
            return person
        if person['PhoneNumber'] == value:
            return person
    return f'No people found with \'{value}\'.'

def removeRecord(value):
    person = findRecord(value)
    if isinstance(person, str):
        print(person)
        return
    people.remove(person)
    writeToFile(peopleDict, filename)
    print(f'\'{value}\' has been removed.')

while True:
    try:
        with open(filename, 'x') as f:
            f.write()
    except:
        print('')

    fileinfo = readFromFile(filename)
    if not isinstance(fileinfo, str):
        peopleDict = fileinfo
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
                print(f'{commandList[1]} has been added.')
            else:
                print("Incorrect Number of Parameters")
        case 'l':
            for record in people:
                print(record.get("FirstName"))
                print(record.get("LastName"))
                print(record.get("PhoneNumber"))
                print('---------------')
        case 'f':
            commandList = command.split()
            if len(commandList) == 2:
                print(findRecord(commandList[1]))
            else:
                print("Incorrect Number of Parameters")
        case 'd':
            commandList = command.split()
            if len(commandList) == 2:
                removeRecord(commandList[1])
            else:
                print("Incorrect Number of Parameters")
        case 'q':
            break
        case default:
            print('Invalid Input')