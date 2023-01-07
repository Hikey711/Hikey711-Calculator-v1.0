def Start():    

    mode = input("What would you like to do?(Square,Divi,Add,Multi,Sub):  ")
    if mode == ("Square"):
        Squared()
    elif mode == ("Divi"):
        Division()
    elif mode == ("Sub"):
        Sub()
    elif mode == ("Add"):
        Add()
    elif mode == ("Multi"):
        Multiply()
    else:
        print ("I do not understand that please retry.")
        Start()


def rr():
    RR = input("Would you like to return to menu?(Yes,No):  ")
    if RR == ("Yes"):
        Start()
    elif RR == ("yes"):
        Start()
    elif RR == ("no"):
        print ("Ok, quitting mathbot")
        exit
    elif RR == ("No"):
        print ("Ok, quitting mathbot")
        exit
    else:
        print ("I do not under stand that, Restarting rr")
        rr()


def Squared():
    Num = 0
    Num = input("What squared number would you like to find?:  ")
    Num = int(Num)
    print (Num * Num)
    rr()


def Division():
    Num = input("select the first number:  ")
    Num2 = input("Select the Second number:  ")
    Num = int(Num)
    Num2 = int(Num2)
    print (Num / Num2)
    rr()


def Sub():
    Num = input("select the first number:  ")
    Num2 = input("Select the Second number:  ")
    Num = int(Num)
    Num2 = int(Num2)
    print (Num - Num2)
    rr()


def Add():
    Num = input("select the first number:  ")
    Num2 = input("Select the Second number:  ")
    Num = int(Num)
    Num2 = int(Num2)
    print (Num + Num2)
    rr()

      
def Multiply():
    Num = input("select the first number:  ")
    Num2 = input("Select the Second number:  ")
    Num = int(Num)
    Num2 = int(Num2)
    print (Num * Num2)
    rr()



Start()