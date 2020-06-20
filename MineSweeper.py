import random as rn
import os

#Smazání konzole
def clear():
    os.system('cls')


#Vytvoření 2d polí podle velikosti
def createPlans(velikost, bombs, plan, bombsPlan):
    for y in range(velikost):
        bombs.append([])
        plan.append([])
        bombsPlan.append([])
        for x in range(velikost):
            bombs[y].append(0)
            plan[y].append("-")


#Vyplnění pole po smrti
def drawBombField(bombs, plan, bombsPlan, velikost):
    for y in range(velikost):
        for x in range(velikost):
            if bombs[y][x] == 1:
                bombsPlan[y].append("X")
            else:
                bombsPlan[y].append(plan[y][x])


#Celkový počet bomb
def bombCount(bombs, velikost):
    count = 0
    for y in range(velikost):
        for x in range(velikost):
            if bombs[y][x] == 1:
                count += 1
    return str(count)


#Spawn bomb po mapě
def spawnBombs(bombs, velikost):
    for i in range((10*velikost*velikost)//100):
        bombs[rn.randint(0, velikost-1)][rn.randint(0, velikost-1)] = 1


#Kontrola vyřešení
def checkUnnolve(bombs, velikost):
    for y in range(velikost):
        for x in range(velikost):
            if bombs[y][x] == 0:
                return True
    clear()
    drawBombField(bomby, plan, bombsPlan, velikost)
    printPlan(bombsPlan, velikost)
    print()
    print("Počet bomb: " + bombCount(bomby, velikost))
    print("Vyhrál si!")
    return False


#Vykreslení 2d pole
def printPlan(plan, velikost):
    if velikost >= 11:
        print("  X ", end=" ")
    else:
        print("  X", end=" ")
    for i in range(velikost):
        print(i, end=" ")
    print()
    if velikost >= 11:
        print("Y   ", end=" ")
    else:
        print("Y  ", end=" ")
    for i in range(velikost):
        if i >= 10:
            print(" V", end=" ")
        else:
            print("V", end=" ")
    print()
    for y in range(velikost):
        if y <= 9 and velikost >= 11:
            print(str(y) + ">", end="   ")
        else:
            print(str(y) + ">", end="  ")
        for x in range(velikost):
            if x >= 9:
                print(plan[y][x], end="  ")
            else:
                print(plan[y][x], end=" ")
        print()
    print()


#Spočítání bomb okolo
def countBombsAround(position, velikost):
    count = 0
    sY, sX = position[0] - 1, position[1] - 1
    for y in range(3):
        for x in range(3):
            if not ((sY + y < 0 or sY + y > velikost - 1) or (sX + x < 0 or sX + x > velikost - 1)):
                if bomby[sY + y][sX + x] == 1:
                    count += 1
            else:
                pass
    return count



def play(position, velikost):
    sY, sX = position[0] - 1, position[1] - 1
    if bomby[position[0]][position[1]] == 1:
        clear()
        drawBombField(bomby, plan, bombsPlan, velikost)
        printPlan(bombsPlan, velikost)
        print("Počet bomb: " + bombCount(bomby, velikost))
        print()
        print("BUUUUM")
        return False
    else:
        plan[position[0]][position[1]] = countBombsAround(position, velikost)
        if countBombsAround((position[0],position[1]),velikost) == 0 and (bomby[position[0]][position[1]] != 5):
            bomby[position[0]][position[1]] = 5
            for y in range(3):
                for x in range(3):
                    if not ((sY + y < 0 or sY + y > velikost - 1) or (sX + x < 0 or sX + x > velikost - 1)):
                        checkUnnolve(bomby, velikost)
                        play((sY+y,sX+x),velikost)
        bomby[position[0]][position[1]] = 5
        clear()
        printPlan(plan, velikost)
        print("Počet bomb: " + bombCount(bomby, velikost))
        return checkUnnolve(bomby, velikost)



velikost = int(input("Zadej velikost plochy: "))
reset = True
while reset:
    bomby = []
    plan = []
    bombsPlan = []
    createPlans(velikost, bomby, plan, bombsPlan)
    spawnBombs(bomby, velikost)
    clear()
    printPlan(plan, velikost)
    print("Počet bomb: " + bombCount(bomby, velikost))
    unsolved = True
    while unsolved:
        while True:
            print()
            y = int(input("Zadej Y: "))
            x = int(input("Zadej X: "))
            print()
            if not(x < 0 or x >= velikost or y < 0 or y >= velikost):
                break
        position = (y, x)
        unsolved = play(position, velikost)
    opak = input("Reset?(y/n): ").lower()
    if opak != "y":
        reset = False