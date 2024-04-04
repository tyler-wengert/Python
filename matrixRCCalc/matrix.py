from sys import stdin

def getSize(raw: list) -> int:

    return raw[0][0]

def formatM(raw: list) -> list:
    clean = []
    replacements = {' ': '', '\n': ''}
    
    for line in raw:
        t = line.replace('\n', '')
        clean.append(t.replace(' ', ''))
    
    return clean[1:]

def multiline():
    print("Please input a matrix: ")
    matrix = stdin.readlines()

    size = getSize(matrix)
    clean = formatM(matrix)

    return size, clean

def chkVal(matrix: str, size: int) -> int:
    val = []

    for line in matrix:
        tval = 0
        for char in line:
            tval += int(char)
        val.append(tval)
    
    return val

def compare(rows: list, cols: list):
    crow = 0
    ccol = 0

    for ind, val in enumerate(rows):
        if val % 2 != 0:
            if crow != 0:
                return 0
            crow = ind

    for ind, val in enumerate(cols):
        if val % 2 != 0:
            if ccol != 0:
                return 0
            ccol = ind
            
    if crow == 0 and ccol == 0:
        return 1
    return crow, ccol

def calcParity() -> str:
    
    size, clean = multiline()
    rows = list(zip(*clean, strict=True))

    rowvals = chkVal(clean, size)
    colvals = chkVal(rows, size)

    result = compare(rowvals, colvals)

    if result == 0:
        return 'Corrupt'
    elif result == 1:
        return 'Matrix has parity'
    else:
        print(result)
        return 'Change bit (' + str(result[0]) + ',' + str(result[1]) + ')'
            

print(calcParity())
