#S04 e5. Print the total number of bases
from pathlib import Path

FILENAME = "../sequences/ADA"
file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
list_contents.pop(0)

print("The total number of bases is: ",len("".join(list_contents)))

#another option

list_contents = file_contents.split("\n")
index = file_contents.find("\n")
file_contents = (file_contents[index:]).replace





