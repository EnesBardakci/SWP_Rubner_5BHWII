import random
from collections import Counter


# Kartendeck erstellen
SUITS: list[str] = ["Hearts", "Diamonds", "Spades", "Clubs"]
VALUES: list[int] = list(range(2, 15))

CARDS: list[tuple[int, str]] = [
    (value, suit)
    for suit in SUITS
    for value in VALUES
]

COMBINATIONS: list[str] = [
    "Royal Flush",
    "Straight Flush",
    "Four of a Kind",
    "Full House",
    "Flush",
    "Straight",
    "Three of a Kind",
    "Two Pair",
    "One Pair",
    "High Card",
]


def combination(hand: list[tuple[int, str]]) -> str:
    """Determines the poker combination of a five-card hand."""

    hand_values: list[int] = [card[0] for card in hand]
    hand_suits: list[str] = [card[1] for card in hand]

    counts: list[int] = sorted(
        Counter(hand_values).values(),
        reverse=True
    )

    same_suit: bool = len(set(hand_suits)) == 1
    sorted_values: list[int] = sorted(set(hand_values))

    # Check for special combinations
    royal_flush: bool = (
        same_suit
        and sorted_values == [10, 11, 12, 13, 14]
    )

    straight: bool = (
        len(sorted_values) == 5
        and (
            sorted_values[-1] - sorted_values[0] == 4
            or sorted_values == [2, 3, 4, 5, 14]
        )
    )

    if royal_flush:
        return "Royal Flush"
    elif same_suit and straight:
        return "Straight Flush"
    elif counts == [4, 1]:
        return "Four of a Kind"
    elif counts == [3, 2]:
        return "Full House"
    elif same_suit:
        return "Flush"
    elif straight:
        return "Straight"
    elif counts == [3, 1, 1]:
        return "Three of a Kind"
    elif counts == [2, 2, 1]:
        return "Two Pair"
    elif counts == [2, 1, 1, 1]:
        return "One Pair"
    else:
        return "High Card"


def simulate_games(number_of_games: int) -> Counter[str]:
    """Simulates poker games and counts each combination."""

    results: Counter[str] = Counter()

    for _ in range(number_of_games):
        hand: list[tuple[int, str]] = random.sample(CARDS, 5)
        result: str = combination(hand)
        results[result] += 1

    return results


def print_results(
    results: Counter[str],
    number_of_games: int
) -> None:
    """Prints the number and percentage of each combination."""

    for name in COMBINATIONS:
        count: int = results[name]
        percentage: float = count / number_of_games * 100

        print(
            f"{name}: {count} times - "
            f"{percentage:.4f} %"
        )


def main() -> None:
    number_of_games: int = 100_000

    results: Counter[str] = simulate_games(number_of_games)
    print_results(results, number_of_games)


if __name__ == "__main__":
    main()