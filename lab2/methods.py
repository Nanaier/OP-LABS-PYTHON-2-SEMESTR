import pickle


def nameoffile():
    name = input("Enter the name of the file: ")
    return name


def isInBase(TeleProg: dict, base: list):
    for prog in base:
        startTime = TeleProg["startTimeHours"]*60 + TeleProg["startTimeMinutes"]
        startTime1 = prog["startTimeHours"]*60 + prog["startTimeMinutes"]
        endTime = TeleProg["endTimeHours"]*60 + TeleProg["endTimeMinutes"]
        endTime1 = prog["endTimeHours"]*60 + prog["endTimeMinutes"]
        if TeleProg["nameOfProgram"] == prog["nameOfProgram"]:
            return True
        elif startTime < startTime1 and endTime > endTime1:
            return True
        elif endTime1 > endTime > startTime1:
            return True
        elif startTime1 < startTime < endTime1:
            return True
        else:
            return False
    return False


def get_input(name):
    list = []
    mode = input("Would you like to append your input? If so, enter a. Otherwise enter w:")
    while True:
        if mode == 'a':
            with open(name, "rb") as file:
                list = pickle.load(file)
            break
        if mode == 'w':
            with open(name, "wb") as file:
                file.truncate()
            break
        while mode != 'a' and mode != 'w':
            mode = input('Enter correct letter:')
    with open(name, "wb") as file:
        print("Enter the input data as [name h:m h:m]\n To end the line | press ---> ENTER\n To end the input | press ---> ENTER twice\n")
        line = input().split()
        while line:
            TeleProg = {
                "nameOfProgram": str(line[0]),
                "startTimeHours": int((line[1].split(':'))[0]),
                "startTimeMinutes": int((line[1].split(':'))[1]),
                "endTimeHours": int((line[2].split(':'))[0]),
                "endTimeMinutes": int((line[2].split(':'))[1])}
            if not isInBase(TeleProg, list):
                list.append(TeleProg)
            else:
                print("Enter not repeating name or not overlapping time")
            line = input().split()
        pickle.dump(list, file)


def lenghtOfProgram(name):
     with open(name, "rb") as fileif:
         temp = pickle.load(fileif)
         for i in range(len(temp)):
             startTime = temp[i]["startTimeHours"]*60 + temp[i]["startTimeMinutes"]
             endTime = temp[i]["endTimeHours"]*60 + temp[i]["endTimeMinutes"]
             length = endTime - startTime
             print("The name:" + temp[i]["nameOfProgram"] + "| the length: " + str(int(length/60)) + " hours and " + str(length % 60) + " minutes\n")


def new_list(name):
    with open(name, "rb") as fileif:
        temp1 = pickle.load(fileif)
        str = []
        for i in range(len(temp1)):
            if temp1[i]["startTimeHours"] >= 9 and (temp1[i]["endTimeHours"] < 18 or (temp1[i]["endTimeHours"] == 18 and temp1[i]["endTimeMinutes"] == 0)):
                str.append(temp1[i])
        with open("output.txt", "wb") as fileof:
            pickle.dump(str, fileof)


def get_format(TeleProg):
    str_startTimeHours = str(TeleProg["startTimeHours"])
    str_startTimeMinutes = str(TeleProg["startTimeMinutes"])
    str_endTimeHours = str(TeleProg["endTimeHours"])
    str_endTimeMinutes = str(TeleProg["endTimeMinutes"])
    if TeleProg["startTimeHours"] < 10:
        str_startTimeHours = '0' + str_startTimeHours
    if TeleProg["startTimeMinutes"] < 10:
        str_startTimeMinutes = '0' + str_startTimeMinutes
    if TeleProg["endTimeHours"] < 10:
        str_endTimeHours = '0' + str_endTimeHours
    if TeleProg["endTimeMinutes"] < 10:
        str_endTimeMinutes = '0' + str_endTimeMinutes
    return str_startTimeHours + ':' + str_startTimeMinutes + ' ' + str_endTimeHours + ':' + str_endTimeMinutes


def print_TeleProg(TeleProg):
    print("Name: " + TeleProg["nameOfProgram"] + " " + get_format(TeleProg))


def out_put(name):
    with open(name, 'rb') as file:
        temp = pickle.load(file)
        for i in range(len(temp)):
            print_TeleProg(temp[i])

