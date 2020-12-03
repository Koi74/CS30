import random
import math


def RandomNumber():
    min = int(input('min:'))
    max = int(input('max:'))
    try:
        print(random.randint(min, max))
    except ValueError:
        print("invalid values, min must be lower than max")
    AgainMenu(RandomNumber)


def PickOne():
    print("enter your options separated by a comma and I'll pick one")
    StrList = input('>').split(',')
    print(StrList[random.randint(0, (len(StrList)-1))])
    AgainMenu(PickOne)


def NickNameGen():
    names = ["Orange juice","Cowboy", "Human", "Inquisitor", "Parking Valet driver", "Executioner", "Manufacturer", "Amazon dilivery man", "McDonald's employee", "Lawn service salesman"]
    firstname = input('firstname:')
    lastname = input('lastname:')
    print(f'{firstname} the {names[random.randint(0, (len(names)-1))]} {lastname}')
    AgainMenu(NickNameGen)


def PythagInput():
    a = int(input('A:'))
    b = int(input('B:'))
    print(math.sqrt(a**2 + b**2))


def MainInput():
    print('1: Random Number Generator \n2: Pick4Me \n3: nick name generator \n4: pythag calc')
    menuInput = int(input('>'))
    if menuInput == 1:
        RandomNumber()
    elif menuInput == 2:
        PickOne()
    elif menuInput == 3:
        NickNameGen()
    elif menuInput == 4:
        NickNameGen()


def AgainMenu(lastfuncname):
    print('\n1: Again \n2: Menu')
    menuInput = int(input('>'))
    if menuInput == 1:
        lastfuncname()
    elif menuInput == 2:
        MainInput()


MainInput()

