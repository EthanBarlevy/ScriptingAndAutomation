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

#JSON

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
