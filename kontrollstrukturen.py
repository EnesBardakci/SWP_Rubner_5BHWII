## Python Kontrollstrukturen Übung

## if, schleifen, break, pass, try-except je ein beispiel
## if:
punkte = 78

if punkte >= 90:
    print("Note 1")
elif punkte >= 75:          ## elif = else if in Java
    print("Note 2")
else:
    print("Schlechter als Note 2")

print('---')

## Schleifen:
## for mit break:
reihe = [1,2,3,4,5,6]
for i in reihe:
    if i == 3:
        break               ## bricht die Schleife sofort ab
    print(i)

print ('---')

## while:
i = 0
while i < 10:
    i += 1
    print(i)

print ('---')

## pass
class Haus:
    pass            ## da passiert nichts weil pass als platzhalter dient für noch nicht implementierte sachen

print ('---')

## try except:
try:                    ## ist wie try, catch in java. except ist hier einfach das catch
    print(91/0)
except ZeroDivisionError:
    print("Division durch 0")
print ('---')

## Bedingte Ausdrücke
## ist dafür da das man sachen kürzer darstellen kann
x = 4
print("ist größer als 5" if x > 5 else "Kleiner als 5")
print ('---')

## Match Case (Switch Case in Java)
note = 2
match note:
    case 1 | 2:
        print("Gut")
    case 3 | 4:
        print("Mittel")
    case _:             ## _ = default in Java
        print("Schlecht")