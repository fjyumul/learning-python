# Open a file from directory
with open("../List and Tuples.txt", "r") as file:
    file_contents = file.readlines()

print(type(file_contents))
print(file_contents)