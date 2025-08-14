# Writing to a file

# Opening file in write mode
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This file is created using Python.\n")

print("Data written to 'example.txt' successfully.")
