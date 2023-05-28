# Edit these to change you die sizes (d4, d6, d8)
dieISize = 4
dieJSize = 6
dieKSize = 8

def doesMatch(i, j, k):
    rolls = [i, j, k]
    rolls.sort()
    return rolls[1] == rolls[2] and rolls[0] != rolls[1]

triplesCount = 0
matchCount = 0
totalCount = 0

for i in range(dieISize):
    for j in range(dieJSize):
        for k in range(dieKSize):
            if i == j and j == k:
                triplesCount += 1
            if doesMatch(i,j,k):
                matchCount += 1
            totalCount += 1


matchPercentage = '{0:.1f}'.format((matchCount / totalCount) * 100)
triplesPercentage = '{0:.1f}'.format((triplesCount / totalCount) * 100)
print(f'For die rolls of [d{dieISize}, d{dieJSize}, d{dieKSize}]')
print(f'{triplesCount} / {totalCount} ({triplesPercentage}%) chance of triples')
print(f'{matchCount} / {totalCount} ({matchPercentage}%) chance of 2 die matching and being higher than the 3rd')


