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
sequenceOriginal = [int(x.strip()) for x in sequenceString.split(',')]

finalNoun = 0
finalVerb = 0

for noun in range(100):
    for verb in range(100):
        sequence = list(sequenceOriginal)
        sequence[1] = noun
        sequence[2] = verb
        if intCodeInterpreter(sequence) == 19690720:
            finalNoun = noun
            finalVerb = verb
            break

print(100 * finalNoun + finalVerb)

