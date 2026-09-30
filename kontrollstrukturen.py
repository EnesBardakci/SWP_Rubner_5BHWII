## Python Kontrollstrukturen Übung

## if, schleifen, break, pass, try-except je ein beispiel
# if/else
x = 10
if x > 5:
    print("x ist größer als 5")
else:
    print("x ist 5 oder kleiner")
print()

# For-Schleife über eine Liste
zahlen = [1, 2, 3]
for z in zahlen:
    print("Zahl:", z)
print()

# While-Schleife bis Bedingung erfüllt ist
count = 0
while count < 3:
    print("Count:", count)
    count += 1
print()

# break
for i in range(10):
    if i == 5:
        print("Abbruch bei i =", i)
        break
    print(i)
print()

# pass
def noch_nicht_fertig():
    pass  # Platzhalter, damit der Code lauffähig bleibt
print("Programm läuft trotzdem weiter")
print()

# try/except/finally
try:
    zahl = int("abc")  # Fehler: "abc" kann nicht in eine Zahl umgewandelt werden
except ValueError:
    print("Das war keine gültige Zahl!")
finally:
    print("Ich werde immer ausgeführt!")
print()

## Bedingte Ausdrücke
## ist dafür da das man sachen kürzer darstellen kann
x = 4
print("ist größer als 5" if x > 5 else "Kleiner als 5")