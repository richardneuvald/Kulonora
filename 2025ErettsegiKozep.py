# Ez a 2025 kozepszintu erettsegi 5. feladata
# Forrás: https://dload-oktatas.educatio.hu/erettsegi/feladatok_2025tavasz_kozep/k_digkult_25maj_fl.pdf

# Megjegyzés: A feladat megoldása nem optimális. A kód továbbfejlesztésre szorul,
# mivel nem célszerű minden mozgásformához külön logikai változót bevezetni.

# Bekéri a felhasználótól az aktivitásokat egy szöveges bemenetként
# Például: "UGFK" vagy "UGG"
bemenet = input("Adja meg az aktivitasat: ")

# 🔢 Szótár, amely az egyes mozgásformákhoz tartozó megtett távolságot tárolja
# U = úszás, G = gyaloglás, F = futás, K = kerékpározás
mozgasok = {"U": 1, "G": 1, "F": 2, "K": 10}

# 🧪 Logikai változók, amelyek azt jelzik, hogy az adott mozgásforma szerepelt-e a bemenetben
hasSwim = False  # Úszott-e?
hasWalk = False  # Gyalogolt-e?
hasRun = False  # Futott-e?
hasCycle = False  # Biciklizett-e?

# 📏 Összesített megtett távolság (kezdetben 0, ez a hét eleje)
megtettTav = 0

# 🔁 Végigmegyünk a bemenet karakterein
for f in bemenet:
    # Ha a karakter szerepel a mozgasok szótárban (érvényes mozgásforma)
    if f in mozgasok:
        # Hozzáadjuk a megfelelő távolságot az összesített értékhez
        megtettTav += mozgasok[f]

        # Beállítjuk a megfelelő logikai változót True-ra, ha az adott mozgás megtörtént
        if f == "U":
            hasSwim = True
        if f == "G":
            hasWalk = True
        if f == "F":
            hasRun = True
        if f == "K":
            hasCycle = True

# 📤 Kiírjuk az eddig megtett távolságot
print(megtettTav)

# 🎯 Ha minden mozgásforma szerepelt, akkor jár +10 km bónusz
if hasSwim and hasWalk and hasRun and hasCycle:
    print("Jar meg 10 km")
    megtettTav += 10  # Hozzáadjuk a bónuszt
else:
    print("Nem jar")  # Ha nem volt mindegyik mozgás, nincs bónusz
