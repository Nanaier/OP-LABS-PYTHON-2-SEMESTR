def nameoffile():
    name = input()
    return name


def get_input(name):
    mode = input("Would you like to append your input? If so, enter a. Otherwise enter w:")
    if mode == 'a':
        file = open(name, "a")
    if mode == 'w':
        file = open(name, "w")
    while (mode != 'a' and mode != 'w'):
        mode = input('Enter correct letter:')
    print("Enter your text:\n To end the line | press ---> ENTER\n To end the input | press ---> Ctrl + X\n")
    while 1:
        line = input()
        if ord(line[0]) == 24:
            break
        file.write(line + "\n")
    file.close()


def output(name):
    file = open(name, "r")
    print(file.read())


def change(name, newname):
    file = open(name, "r")
    lines = file.readlines()
    newtext = ''
    for line in lines:
        for letter in line:
            if letter != '1' and letter != '0':
                newtext += letter
            if letter == '1':
                newtext += '0'
            if letter == '0':
                newtext += '1'
    newfile = open(newname, "w")
    newfile.write(newtext)
    file.close()
    newfile.close()

print("enter the name of the input file:")
header = nameoffile()
get_input(header)
print('Entered text:\n')
output(header)
print("enter the name of the output file:")
newheader = nameoffile()
change(header, newheader)
print('Changed text:\n')
output(newheader)
