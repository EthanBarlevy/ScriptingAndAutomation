import json

class Database:
    __filename = ""
    __people = []
    __peopleDict = {}
    __peopleDict["People"] = __people

    def __init__(self, filename):
        self.__filename = filename
        try:
            with open(self.__filename, 'x') as f:
                f.write()
        except:
            print('')
        fileinfo = self.__readFromFile()
        if not isinstance(fileinfo, str):
            self.__peopleDict = fileinfo
            self.__people = self.__peopleDict["People"]

    def __findRecord(self, value):
        for person in self.__people:
            if person['FirstName'].lower() == value.lower():
                return person
            if person['LastName'].lower() == value.lower():
                return person
            if person['PhoneNumber'] == value:
                return person
        return f'No people found with \'{value}\'.'

    def __removeRecord(self, value):
        person = self.__findRecord(value)
        if isinstance(person, str):
            print(person)
            return
        self.__people.remove(person)
        self.__writeToFile()
        print(f'\'{value}\' has been removed.')

    def __readFromFile(self):
        with open(self.__filename, 'r') as f:
            data = f.read()
            if len(data) > 0:
                return json.loads(data)
            else:
                return 'No json data found'

    def __writeToFile(self):
        with open(self.__filename, 'w') as f:
            f.write(json.dumps(self.__peopleDict, indent=4))

    def __createDictionary(self, fName, lName, phone):
        dictionary = {}
        dictionary['FirstName'] = fName
        dictionary['LastName'] = lName
        dictionary['PhoneNumber'] = phone
        return dictionary

    def doSomething(self, command):
        match command[0]:
            case 'a':
                commandList = command.split()
                if len(commandList) == 4:
                    self.__people.append(self.__createDictionary(commandList[1], commandList[2], commandList[3]))
                    self.__writeToFile()
                    print(f'{commandList[1]} has been added.')
                else:
                    print("Incorrect Number of Parameters")
            case 'l':
                for record in self.__people:
                    print(record.get("FirstName"))
                    print(record.get("LastName"))
                    print(record.get("PhoneNumber"))
                    print('---------------')
            case 'f':
                commandList = command.split()
                if len(commandList) == 2:
                    print(self.__findRecord(commandList[1]))
                else:
                    print("Incorrect Number of Parameters")
            case 'd':
                commandList = command.split()
                if len(commandList) == 2:
                    self.__removeRecord(commandList[1])
                else:
                    print("Incorrect Number of Parameters")
            case 'q':
                return True
            case default:
                print('Invalid Input')


def main():
    db = Database("db.json")
    while True:
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

        if (db.doSomething(command) == True):
            break

if __name__ == "__main__":
    main()