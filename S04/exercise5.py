from pathlib import Path

FILENAME = "sequences/ADA"
file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
list_contents.pop(0)

print(len("".join(list_contents)))

#another option

list_contents = file_contents.split("\n")
index = file_contents.find("\n")
file_contents = (file_contents[index:]).replace





