# Working with files

"""
    Resources:
        http://www.python-ds.com/python-3-escape-sequences

"""

with open("ninja.txt", "r") as ninja_file:
    contents = ninja_file.read()
    # print(contents)

# Reading a file line-by-line (using a for loop)
path_to_file = r"C:\Users\Sudo\Desktop\SmartNinja\Curso_07_2020\dummy.txt"

with open(path_to_file, "r") as ninja_file:
    ninja_lines = ninja_file.readlines()

    for line in ninja_lines:
        # print(line)
        pass

# Writing to a file
with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello, new file!")

##############################################################################################
