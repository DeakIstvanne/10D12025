## 1. feladat
##Készíts programot, amely kiírja, hogy hány esetben van az
##interfész bekapcsolt állapotban:
switch="interface ethernet0 up, interface ethernet1 up, interface ethernet3 down"


#2. feladat
##Készíts listát az 192.168.1.1 ip címből úgy, hogy a lista első eleme a 192,
##a második a 168 stb. legyen.
ip="192.168.1.1"



# 3. feladat
##Készíts a listából egy sztringet, amelyben az ip cím helyes formátumban van.
a=['192', '168', '1', '2']


## 4. feladat
## Írasd ki a sztringet úgy, hogy az interface lekapcsolt állapotban
## van. (up helyett down)
a = "Interface Eth0 is up"

# 5. feladat
# Kérd be a felhasználótól a nevét, majd írasd ki csupa nagybetűvel!




# 6. feladat
# Alakítsd át a következő mondatot:
mondat="Szép időnk van ma."

# a) kapitális típusra (minden kezdőbetű nagybetű)

# b) csupa kisbetűre


# c) csupa nagybetűre


# 8. feladat
##Kérdezd meg a felhasználótól, hogy szeret-e programozni. (i/n)
##Akár kicsi, akár nagybetűvel írja a választ, minden esetben az üzenet legyen:
##     ha a válasz i / I(igen): "Örülök."
##     ha a válasz n / N (nem): "Nem baj, majd megszereted."
##    
##Rossz válasz esetén ismételje addig a kérdést, amíg i vagy n betűt nem
## ír a felhasználó.



# 9. feladat
# a)
# Az alábbi lista lehet, hogy hibásan lett felrögzítve, mert a szó elején szóközt tartalmaz.
# Számolja meg, hány hibásan rögzített szó van!

gyumolcsok=["alma"," körte"," szilva"," banán","cseresznye","eper","kivi"," mandarin"," narancs"]
db = 0
for i in gyumolcsok:
     if i.startswith(" ")== True:
          db+=1
print("db:", db)

# b) javítsa ki!




# Az alábbi lista lehet, hogy hibásan lett felrögzítve, mert némely szó végén pont van.
# a) Mely szavak hibásak? Írja ki a képernyőre!
# b) Javítsa ki a hibás szavakat!
zoldsegek=["hagyma.","burgonya","karfiol","sárgarépa.","zeller","karalábé.","petrezselyem."]




# 10. feladat:
# Metódus segítségével írasd ki a sztinget úgy, hogy az összes "a" betű helyett
# "@" karaker legyen.
mond="Szép napunk van ma."


# Kérjen be a felhasználótól egy mondatot, majd vizsgálja meg, hogy van-e írásjel a mondat végén.
# Ha nincs, figyelmeztesse a felhasználót, hogy a mondat helytelen.



# Vágja le a szóközöket a sztringről:
strg=" alma "








