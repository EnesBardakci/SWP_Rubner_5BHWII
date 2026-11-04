import random
from collections import Counter

farben = ["Herz", "Karo", "Pik", "Kreuz"]
symbole = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

symbol_werte = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Bube": 11, "Dame": 12, "König": 13, "Ass": 14,
}

REFERENZ = {
    "Hohe Karte": 50.1177,
    "Paar": 42.2569,
    "Zwei Paare": 4.7539,
    "Drilling": 2.1128,
    "Straße": 0.3925,
    "Flush": 0.1965,
    "Full House": 0.1441,
    "Vierling": 0.0240,
    "Straight Flush": 0.0015,
}


def erstelle_deck():
    """Erstellt ein Kartenspiel als Liste von Karten (jede Karte ist eine Liste [Symbol, Farbe])."""
    deck = []
    for farbe in farben:
        for symbol in symbole:
            deck.append([symbol, farbe])
    return deck


def ziehe_hand(deck, rng=random):
    """Zieht 5 verschiedene Karten ohne Zurücklegen."""
    return rng.sample(deck, 5)


def gleiche_anzahl(werte):
    """Häufigkeiten gleicher Werte, absteigend sortiert, z.B. [2, 2, 1]."""
    return sorted(Counter(werte).values(), reverse=True)


def ist_paar(werte):
    """Genau ein Paar: die größte Gruppe hat 2 Karten."""
    return gleiche_anzahl(werte)[0] == 2


def ist_drilling(werte):
    """Drei Karten mit gleichem Wert."""
    return gleiche_anzahl(werte)[0] == 3


def ist_zwei_paare(werte):
    """Zwei verschiedene Paare."""
    return gleiche_anzahl(werte)[:2] == [2, 2]


def ist_flush(farben_hand):
    """Alle fünf Karten haben dieselbe Farbe."""
    return len(set(farben_hand)) == 1


def ist_strasse(werte):
    """Fünf aufeinanderfolgende Werte. Auch A-2-3-4-5 zählt."""
    einzigartig = sorted(set(werte))
    if len(einzigartig) != 5:
        return False
    if einzigartig[-1] - einzigartig[0] == 4:
        return True
    return einzigartig == [2, 3, 4, 5, 14]  # Ass als niedrigste Karte


def ist_full_house(werte):
    """Drilling plus Paar."""
    return gleiche_anzahl(werte) == [3, 2]


def ist_vierling(werte):
    """Vier Karten mit gleichem Wert."""
    return gleiche_anzahl(werte)[0] == 4


def ist_straight_flush(werte, farben_hand):
    """Straße und Flush gleichzeitig."""
    return ist_strasse(werte) and ist_flush(farben_hand)


def bewerte(hand):
    """Bestimmt die höchste Kombination einer 5-Karten-Hand."""
    werte = [symbol_werte[symbol] for symbol, _ in hand]
    farben_hand = [farbe for _, farbe in hand]

    if ist_straight_flush(werte, farben_hand):
        return "Straight Flush"
    if ist_vierling(werte):
        return "Vierling"
    if ist_full_house(werte):
        return "Full House"
    if ist_flush(farben_hand):
        return "Flush"
    if ist_strasse(werte):
        return "Straße"
    if ist_drilling(werte):
        return "Drilling"
    if ist_zwei_paare(werte):
        return "Zwei Paare"
    if ist_paar(werte):
        return "Paar"
    return "Hohe Karte"


def simuliere(anzahl=100000, seed=None):
    """Spielt `anzahl` Hände und zählt die Kombinationen."""
    rng = random.Random(seed)
    deck = erstelle_deck()
    zaehler = Counter()
    for _ in range(anzahl):
        zaehler[bewerte(ziehe_hand(deck, rng))] += 1
    return zaehler


if __name__ == "__main__":
    ANZAHL = 100000
    ergebnis = simuliere(ANZAHL, seed=42)
    for kombi, n in ergebnis.most_common():
        print(kombi, n)