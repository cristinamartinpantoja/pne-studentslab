import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
print("Total people on the databases:", len(person))
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname1'], person['Lastname1'])
termcolor.cprint("Age: ", 'green', end="")
print(person['age1'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber1']

# Print the information on the console, in colors
print()
print("Total people on the databases:", len(person))
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname1'], person['Lastname1'])
termcolor.cprint("Age: ", 'green', end="")
print(person['age1'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber1']

# Print the number of elements in the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

# Print all the numbers
for i, dictnum in enumerate(phoneNumbers):
    termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

    # The element num contains 2 fields: number and type
    termcolor.cprint("\t- Type: ", 'red', end='')
    print(dictnum['type'])
    termcolor.cprint("\t- Number: ", 'red', end='')
    print(dictnum['number'])