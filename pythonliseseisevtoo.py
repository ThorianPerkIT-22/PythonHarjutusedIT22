#Thorian.Perk
#02.11.2022
import math
import random


#ül. 4.3 Peo eelarve














"""

#ül. 4.2 Õunamahla tegemine
def mahlapakkide_arv(o):
        m = round(o*0.4/3)
        return m
 
oun = int(input("Õunte kogus kgs:  "))
print(mahlapakkide_arv(oun))



#ül. 4.1 Bänner

def banner(a):
        a=a.upper()
        return a

print(banner("Osta ja sa ei kahetse!"))


print("!")
a = int(input("Mitu korda soovite reklaamlauset kuvada? "))
b = input("Mida soovite kuvada")
for i in range (a):
            print(b.upper())





#ül. 3.4 Jukebox

fs = int(input("Millist failinime tahate?: "))
fs = open("jukebox.txt", "r")
print(fs.read())


#ül. 3.3 Sissetulekud
a = open("konto.txt", "r")
for line in a:
    if re.search('[-0-9]{1}', line):
        print(a)


#ül.8 Male
nisuterad=0
a=int(input("Sisestage täisarv"))
i = 1
while i <= a:
    i += 1
    x=i*(i+1/2)/2
    nisuterad+=x
print(nisuterad)


#ül.7 Täringud
taringud = int(input("Mitu täringut tahad?"))
for i in range(taringud):
    print(random.randint(1, 6))


#ül.6 Murelikud lapsevanemad
ringid = int(input("Mitu ringi jooksid"))
ring = 0
porgand = 0
while ring < ringid:
    ring +=1
    if ring %2 == 0:
        porgand+=ring
print(f"porgandite koguarv on:{porgand}")


#ül.5 Äratus

kell = int(input())


#ül.0 tervitus
print("Tere maailm!")


#ül.1 aasta liblikas
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on"
lause = str(aasta) + lause_keskosa + liblikas
print (lause)

"""