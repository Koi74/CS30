import random


def randomnumber():
    min = int(input('min:'))
    max = int(input('max:'))
    print(random.randint(min, max))
    mainInput()


def pick_one():
    print("enter your options separated by a comma and I'll pick one")
    rawstr = input('>')
    strList = rawstr.split(',')
    print(strList[random.randint(0, (len(strList)-1))])
    mainInput()


def NickNameGen():
    names = ["Orange juice","Cowboy", "Human", "Inquisitor", "Parking Valet driver", "Executioner", "Manufacturer", "Amazon dilivery man", "McDonald's employee", "Lawn service salesman"]
    firstname = input('firstname:')
    lastname = input('lastname:')
    print(f'{firstname} the {names[random.randint(0, (len(names)-1))]} {lastname}')
    mainInput()
                


def mainInput():
    print('1: Random Number Generator \n2: Pick4Me \n3: nick name generator')
    menuInput = int(input('>'))
    if menuInput == 1:
        randomnumber()
    elif menuInput == 2:
        pick_one()
    elif menuInput == 3:
        NickNameGen()



mainInput()