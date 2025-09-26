# Ez a 2025 kozepszintu erettsegi 5. feladata
# https://dload-oktatas.educatio.hu/erettsegi/feladatok_2025tavasz_kozep/k_digkult_25maj_fl.pdf

# region Feladat 1
print("1. feladat")
bemenet = input("Adja meg az aktivitasat: ")
# endregion

mozgasok = {"U": 1, "G": 1, "F": 2, "K": 10}

hasSwim = False
hasWalk = False
hasRun = False
hasCycle = False


megtettTav = 0

for f in bemenet:
    if f in mozgasok:
        megtettTav += mozgasok[f]

        if f == "U":
            hasSwim = True
        if f == "G":
            hasWalk = True
        if f == "F":
            hasRun = True
        if f == "K":
            hasCycle = True


print(megtettTav)

if hasSwim and hasWalk and hasRun and hasCycle:
    print("Jar meg 10 km")
    megtettTav += 10
else:
    print("Nem jar")
