def intCodeInterpreter(sequence):
    index = 0
    while index < len(sequence):
        value = sequence[index]
        if value == 1: # sum
            opIndex1 = sequence[index + 1]
            opIndex2 = sequence[index + 2]
            resIndex = sequence[index + 3]
            sequence[resIndex] = sequence[opIndex1] + sequence[opIndex2]
            index += 4
        elif value == 2: # mult
            opIndex1 = sequence[index + 1]
            opIndex2 = sequence[index + 2]
            resIndex = sequence[index + 3]
            sequence[resIndex] = sequence[opIndex1] * sequence[opIndex2]
            index += 4
        elif value == 99: # end
            break
    
    return sequence[0]


file = open("input.txt", "r")
sequenceString = file.readline()
sequence = [int(x.strip()) for x in sequenceString.split(',')]

print(intCodeInterpreter(sequence))