# Writing to a file
file = open("sample.txt", "w")
file.write("Hello, this is my first file handling program.\n")
file.write("Learning Python for AIML.\n")
file.close()

# Reading from the file
file = open("sample.txt", "r")
content = file.read()
print("File Content:")
print(content)
file.close()
