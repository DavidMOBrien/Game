contents = open('countablePokemon.txt','r')
contentLines = contents.readlines()
for item in range(len(contentLines)):
    contentLines[item] = contentLines[item].strip('\n')
    contentLines[item] = contentLines[item].split(',')

pokeList = ['BUG','DARK','DRAGON','ELECTRIC','FIGHTING','FIRE','FLYING','GHOST','GRASS','GROUND','ICE','NORMAL','POISON','PSYCHIC','ROCK','STEEL','WATER']
pokeDict = {}

for pokeType in pokeList:
    counter = 0
    for pokemon in contentLines:
        if pokeType in pokemon:
            counter +=1
    pokeDict[pokeType] = counter

for pokemon in contentLines:
    if not pokemon[1] in pokeList:
        print(pokemon[0])
    if len(pokemon) == 3:
        if not pokemon[2] in pokeList:
            print(pokemon[0])

for pokemon in contentLines:
    if len(pokemon) == 2 and pokemon[1] == 'NORMAL':
        print(pokemon[0])

print('Total Pokemon: ',len(contentLines))
for pokeType in pokeList:
    print(pokeType,':',pokeDict[pokeType])
