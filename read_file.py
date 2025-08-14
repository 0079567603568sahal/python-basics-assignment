python# Reading from a file

# Opening file in read mode
with open("example.txt", "r") as file:
    content = file.read()

print("--- File Content ---")
print(content)
