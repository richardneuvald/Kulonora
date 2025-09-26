szoveg = "szoveg"
szam = 1  # Lehet egesz es tort szam is a python nem tesz kulombseget kozte
logikai = True  # True vagy False erteket vehet fel (0 v 1)


print("ki akarom irni")  # Beegetett szoveg
print(szoveg)  # A valtozo ertket irja ki, nem beegetett


igazE = True


if (
    igazE
):  # Azt nezi meg mindig, hogy a feltetel igazzal ter e vissza, igy nem kotelezo a valtozonev
    print("Igaz")
else:
    print("Hamis")


if igazE is not True:
    print("Hamis")
else:
    print("Igaz")

if not igazE:
    print("Hamis")
else:
    print("Igaz")
