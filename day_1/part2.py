def calcRocketFuel(mass):
    return int(mass / 3) - 2

def calcRocketFuelUpdated(module):
    fuel = calcRocketFuel(module)
    sum = 0
    while fuel > 0:
        sum += fuel
        fuel = calcRocketFuel(fuel)
    return sum

def calcFuelForModulesUpdated(modules):
    sum = 0
    for module in modules:
        sum += calcRocketFuelUpdated(int(module))
    return sum


file = open("modules.txt", "r")
modules = file.readlines()

print(calcFuelForModulesUpdated(modules))