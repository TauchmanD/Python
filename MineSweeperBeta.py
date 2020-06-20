import random as rn
import os
def clear():
    os.system('cls')
def createPlans(velikost, bombs, plan, bombsPlan):
    for y in range(velikost):
        bombs.append([])
        plan.append([])
        bombsPlan.append([])
        for x in range(velikost):
            bombs[y].append(0)
            plan[y].append("-")


def drawBombField(bombs, plan, bombsPlan, velikost):
    for y in range(velikost):
        for x in range(velikost):
            if bombs[y][x] == 1:
                bombsPlan[y].append("X")
            else:
                bombsPlan[y].append(plan[y][x])


def bombCount(bombs, velikost):
    count = 0
    for y in range(velikost):
        for x in range(velikost):
            if bombs[y][x] == 1:
                count += 1
    return str(count)

def spawnBombs(bombs, velikost):
    for i in range((25*velikost*velikost)//100):
        bombs[rn.randint(0, velikost-1)][rn.randint(0, velikost-1)] = 1

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

def countBombs(position, velikost):
    count = 0
    sY, sX = position[0]-1, position[1]-1
    if bomby[position[0]][position[1]] == 1:
        clear()
        drawBombField(bomby, plan, bombsPlan, velikost)
        printPlan(bombsPlan, velikost)
        print("Počet bomb: " + bombCount(bomby, velikost))
        print()
        print("BUUUUM")
        return False
    else:
        for y in range(3):
            for x in range(3):
                if not((sY+y < 0 or sY+y > velikost-1) or (sX+x < 0 or sX+x > velikost-1)):
                    if bomby[sY+y][sX+x] == 1:
                        count += 1
                else:
                    pass
        clear()
        plan[position[0]][position[1]] = count
        bomby[position[0]][position[1]] = 5
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
        unsolved = countBombs(position, velikost)
    opak = input("Reset?(y/n): ").lower()
    if opak != "y":
        reset = False