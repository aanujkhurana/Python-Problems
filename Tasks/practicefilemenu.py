f = open("student.txt","w")
f.close()

def enter_record():
    name = None
    f = open("student.txt", "a")
    while True:
        name = input("name: ")
        if name == "":
            f.close()
            break
        city = input("city: ")
        country = input("Country")
        f.writelines(name+","+city+" ,"+country)

def searchbyname():
    name = None
    while True:
        name = input("name: ")
        if name == "":
            break
        count = 0
        f = open("student.txt")
        for line in f:
            if line.startswith(name):
                print(line,end="")
                count += 1
            if count == 0:
                print("not found")

while True:
    print("1.RECORD")
    print("2.SEARCH")
    print("3.QUIT")
    inp = input("Selection")
    if inp == "1": enter_record()
    elif inp == "2": searchbyname()
    elif inp == "3":
        print("bye")
        break
    else:
        continue

        

