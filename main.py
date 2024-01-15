from infp.BigNumber import BigNumber

with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        if line[1] == '*':
            print((BigNumber(line[0]) * BigNumber(line[2])).toString())
        elif line[1] == '+':
            print((BigNumber(line[0]) + BigNumber(line[2])).toString())
        elif line[1] == '-':
            print((BigNumber(line[0]) - BigNumber(line[2])).toString())
        elif line[1] == '/':
            print((BigNumber(line[0]) / BigNumber(line[2])).toString())
        elif line[1] == '%':
            print((BigNumber(line[0]) % BigNumber(line[2])).toString())
