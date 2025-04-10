# In python we can make our data persistent by saving them to files

open("lista della spesa.txt", "w") # "w" stands for write
# If the file is not present, it is going to create it from scratch
# # The file is going to be created relative to the folder we currently are
# open("W:/Repository/Programming-Principles/lezione 12/lezione 12.py", "w") # we can use absolute path too

# The open function creates a stream, a channel where data flow (from the program to the file)
# The open function also returns a File object

file = open("lista della spesa.txt", "w")
print(file)
file.write("testMessage") # This overrides the content
file.write("caffé") # This will cause issues, because the cp1252 standard encoding does not support accents
file = open("lista della spesa.txt", "w", encoding="utf-8") # now it will work
file.write("caffé")

file.close() # We need to do this everytime we open a stream!!!

# There is also another way that closes automatically

with open("lista della spesa.txt", "r", encoding="utf-8") as file:
    content = file.read() # Reads all the content of a variable
    # If the file does not exist we get a fileNotFoundError when we try to read

# Generally, the errors relative to the open functions are of type IOError

with open("lista della spesa.txt", "r", encoding="utf-8") as file:
    for line in file.readlines:
        print(line) # readlines creates a list of all lines


with open("lista della spesa.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line) # in the latest versions the file object lines can also be looped like this


with open("lista della spesa.txt", "w", encoding="utf-8") as file:
    file.writelines(["ceci\n", "mele\n"]) # We need to put \n otherwise it will write everything on the same line

with open("python logo.png", "rb") as file: # rb stands for read binary. By deafault r is equal to rt (read text)
    image = file.read()
with open("python logo.png", "rb") as file: 
    image_data_lines = file.readlines() # This returns binary lines for binary
print(len(image_data_lines)) # This is the total number of lines
print(type(image_data_lines[0])) # <class 'bytes'>

with open("python logo_copy.png", "wb") as file: # wb stands for write binary
    image = file.writelines(image_data_lines)
# or also
with open("python logo_another_copy.png", "wb") as file: 
    for line in image_data_lines[0:150]:
        file.write(line)

# Sequential access: reading file line by line/byte by byte
with open("lista della spesa.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
# Different from random access: The read starts from an offsetted point
with open("lista della spesa.txt", "r", encoding="utf-8") as file:
    file.seek(2) #this means that the read will start from 2nd character 
    print(file.read(20)) #this means that we will read only 20 characters

shopping_list = {"pere":5, "arance":2, "mele":8}
import json
with open("lista_spesa.json", "w", encoding="utf-8") as file:
    json.dump(shopping_list, file)

with open("lista_spesa.json", "r", encoding="utf-8") as file:
    read_shopping_list = json.load(file)
print(content) 