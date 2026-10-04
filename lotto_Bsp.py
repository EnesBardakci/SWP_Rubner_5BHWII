import random

def draw_numbers():
    """
    Zieht 6 verschiedene Zufallszahlen von 1 bis 45.
    Verwendet eine effiziente Tauschmethode, um Duplikate zu vermeiden.
    Rückgabe:
        list[int]: Liste mit den 6 gezogenen Zahlen.
    """
    numbers = list(range(1, 46))
    result = []
    n = 45  # Anzahl der noch verfügbaren Zahlen

    for i in range(6):
        index = random.randint(0, n - 1)
        result.append(numbers[index])
        # Gezogene Zahl ans Ende des aktiven Bereichs tauschen und diesen
        # verkleinern (n -= 1), so kann sie nicht nochmal gezogen werden.
        numbers[index], numbers[n - 1] = numbers[n - 1], numbers[index]
        n -= 1
    return result


def print_draw(result: list):
    """
    Gibt die gezogenen Zahlen aufsteigend sortiert aus.
    Parameter:
        result (list[int]): Liste der gezogenen Zahlen.
    """
    print("Drawn Numbers:", sorted(result))


def statistics(counter: dict, result: list):
    """
    Erhöht für jede gezogene Zahl den Zähler im Dictionary.
    Wird nach jeder Ziehung aufgerufen.
    Parameter:
        counter (dict[int, int]): Zahl -> Häufigkeit.
        result (list[int]): Die Zahlen der aktuellen Ziehung.
    """
    for number in result:
        counter[number] += 1


def simulate(rounds: int):
    """
    Führt 'rounds' Ziehungen durch, aktualisiert nach jeder Ziehung
    die Statistik und gibt am Ende die Häufigkeiten aus.
    Parameter:
        rounds (int): Anzahl der Ziehungen.
    """
    counter = {i: 0 for i in range(1, 46)}

    # Ziehung 'rounds'-mal wiederholen
    for _ in range(rounds):
        result = draw_numbers()
        statistics(counter, result)

    print(f"\nStatistics after {rounds} draws:")
    for number in range(1, 46):
        percent = (counter[number] / (rounds * 6)) * 100  # Wahrscheinlichkeit in Prozent
        print(f"Number {number:2}: {counter[number]:7} times ({percent:5.2f}%)")


def main():
    """
    Hauptprogramm:
    - Eine Ziehung durchführen und ausgeben
    - Statistik für 1000, 10000 und 100000 Ziehungen erstellen
    """
    print_draw(draw_numbers())

    for rounds in (1000, 10000, 100000):
        simulate(rounds)


if __name__ == '__main__':
    main()
