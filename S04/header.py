#S04 e3. Print the header
from pathlib import Path

FILENAME = "sequences/RNU6_269P"

file_contents = Path(FILENAME).read_text()
list_contents = file_contents.split("\n")

print(list_contents[0])