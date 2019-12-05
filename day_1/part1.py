def calcRocketFuel(mass):
    return int(mass / 3) - 2

def calcFuelForModules(modules):
    sum = 0
    for module in modules:
        sum += calcRocketFuel(int(module))
    return sum


file = open("modules.txt", "r")
modules = file.readlines()

print(calcFuelForModules(modules))