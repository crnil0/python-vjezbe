# program km->milje

print("pozdrav, ovo je program koj preracunava km u milje")
while True:
    print("unesi broj kilometara koji zelis preracunati. unesi samo broj!")
    km=input("kilometri: ")
    km=float(km.replace(",", "."))
    milje=km*0.621371
    print("rezultat: "+str(milje))
    izbor=input("zelis li novi izracun? DA/NE: ")
    if izbor=="NE":
        break
print("hvala na koristenju, dodite nam opet")