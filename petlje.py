# petlje

import random

tajnibroj=random.randint(1,30)

pogodi=0

for x in  range(5):
    pogodi=int(input("pogodi broj izmedu 1 i 30 "))
    if pogodi==tajnibroj:
        print("bravo brate sve znas")
        break
    elif pogodi>tajnibroj:
        print("nope, probaj manji broj")
    elif pogodi<tajnibroj:
        print("nikako, probaj veci broj")
print("kraj programa")
print("trazeni broj u ovoj igri bio je:" +str(tajnibroj))
