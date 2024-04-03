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

def compare(row: int, col: int):
    pass

def calcParity() -> str:
    
    size, clean = multiline()
    rows = list(zip(*clean, strict=True))

    rowvals = chkVal(clean, size)
    colvals = chkVal(rows, size)

    compare(rowvals, colvals)
        
            

result = calcParity()
