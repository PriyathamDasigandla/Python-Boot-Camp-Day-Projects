import os, sys, subprocess

#clears the terminal screen, works on Windows and Linux/Mac
def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def get_key():
    #Read a single keypress without waiting for Enter.
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getwch()
    else:
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

#Literally the whole Calculator
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

#Dictionary of operations
operationCat = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

#Function to ensure user input is a float
def hasToBeFloat(promptyDumpty):
    while True:
        try:
            return float(input(promptyDumpty))
        except ValueError:
            print("Please enter a valid number.")

#Main logic
while True:
    clear()
    calculationRuns = True
    print("Welcome to Pythonista!")
    nOne = hasToBeFloat("What's the first number?: ")

    #To continue after the first calculation
    while calculationRuns:
        print(*operationCat, sep="\n")
        #Strictly allowing the user to select an operation from the dictionary
        while True:
            selectedOperation = input("Pick an operation: ")
            if selectedOperation in operationCat:
                break
            else:
                print("Please select a valid operation.")
        #Ensuring the user doesn't divide by zero
        while True:
            nTwo = hasToBeFloat("What's the next number?: ")
            try:
                solvent = operationCat[selectedOperation](nOne, nTwo)
                break
            except ZeroDivisionError:
                print("You can't divide by zero! Please enter a different number.")
        print(f"{nOne} {selectedOperation} {nTwo} = {solvent:.2f}")
        print(f"Press 'y' to continue calculating with {solvent}, or type 'n' to start a new calculation. Or press any key to exit!")
        key = get_key()
        if key.lower() == 'y':
            nOne = solvent
        elif key.lower() == 'n':
            calculationRuns = False
        else:
            print("Fuck You!")  #cuz why not!
            sys.exit()