# 🧠 Változók létrehozása – különböző adattípusok

szoveg = "Ez egy szöveg"  # Szöveges adat (string), idézőjelek közé írjuk
szam = 42  # Egész szám (int)
tort_szam = 3.14  # Tört szám (float)
logikai = True  # Logikai érték (bool): True vagy False

# 🔄 Alternatív lehetőségek változókhoz:
# szoveg2 = 'Másik szöveg'  # Egyes idézőjelek is használhatók
# szam2 = -7                # Negatív egész szám
# tort_szam2 = 0.0          # Nulla mint tört szám
# logikai2 = False          # Hamis érték

# 🖨️ Kiíratás a képernyőre

print("Ez egy beégetett szöveg")  # Mindig ezt írja ki
print(szoveg)  # A változó értékét írja ki

# 🔄 Alternatív kiíratás:
print("A szám értéke:", szam)  # Több elem kiíratása egy sorban
print(f"Tört szám: {tort_szam}")  # f-string: változók beágyazása szövegbe

# ✅ Feltételes elágazás – if, else

igazE = True  # Ez a változó határozza meg, hogy mi történjen

if igazE:  # Lehetne igazE == True
    print("Igaz")  # Ha igazE értéke True
else:
    print("Hamis")  # Ha igazE értéke False

# 🔄 Alternatív feltételvizsgálatok:

if igazE is not True:
    print("Hamis")
else:
    print("Igaz")

if not igazE:  # Rövidített tagadás
    print("Hamis")
else:
    print("Igaz")

# 🧮 Összehasonlítási operátorok példák:

a = 5
b = 10

print("a == b:", a == b)  # Egyenlőség
print("a != b:", a != b)  # Nem egyenlő
print("a < b:", a < b)  # Kisebb
print("a > b:", a > b)  # Nagyobb
print("a <= b:", a <= b)  # Kisebb vagy egyenlő
print("a >= b:", a >= b)  # Nagyobb vagy egyenlő

# 🔁 Bővítés: több feltétel vizsgálata

if a < b and igazE:  # Mindkét feltétel igaz
    print("a kisebb mint b ÉS igazE is igaz")

if a > b or not igazE:  # Legalább az egyik feltétel igaz
    print("a nagyobb mint b VAGY igazE hamis")

# 🧪 Típusvizsgálat – milyen típusú egy változó?

print(type(szoveg))  # <class 'str'>
print(type(szam))  # <class 'int'>
print(type(tort_szam))  # <class 'float'>
print(type(logikai))  # <class 'bool'>
