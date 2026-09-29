"""Kontrollstrukturen am Beispiel einer kleinen Notenverwaltung"""

schueler = {"Anna": 92, "Ben": 55, "Clara": 78, "David": "abwesend", "Eva": 34}


# 1) if / elif / else: Punkte -> Note
def note_fuer(punkte):
    if punkte >= 90:
        return 1
    elif punkte >= 75:
        return 2
    elif punkte >= 60:
        return 3
    elif punkte >= 50:
        return 4
    else:
        return 5


# 2) for + try-except: alle Schueler durchgehen, ungueltige Werte abfangen
print("=== Notenliste ===")
noten = {}
for name, punkte in schueler.items():
    try:
        noten[name] = note_fuer(punkte)
        print(f"{name}: {punkte} Punkte -> Note {noten[name]}")
    except TypeError:
        print(f"{name}: keine gueltige Punktzahl ({punkte!r})")


# 3) bedingter Ausdruck: bestanden / nicht bestanden
print("\n=== Ergebnis ===")
for name, note in noten.items():
    status = "bestanden" if note <= 4 else "NICHT bestanden"
    print(f"{name}: {status}")


# 4) match-case: Note -> Text
def note_als_text(note):
    match note:
        case 1:
            return "Sehr gut"
        case 2:
            return "Gut"
        case 3:
            return "Befriedigend"
        case 4:
            return "Genuegend"
        case 5:
            return "Nicht genuegend"
        case _:
            return "Unbekannt"

print("\n=== Notentext ===")
for name, note in noten.items():
    print(f"{name}: {note_als_text(note)}")


# 5) while + break: erste negative Note suchen
print("\n=== Erste negative Note ===")
namen = list(noten)
index = 0
while index < len(namen):
    if noten[namen[index]] == 5:
        print(f"Erste negative Note: {namen[index]}")
        break
    index += 1


# 6) pass: Platzhalter fuer eine spaeter geplante Funktion
def sende_mahnung(name):
    pass  # TODO: spaeter E-Mail an Schueler senden

sende_mahnung("Eva")
