"""
Card Hand Validation
You are provided with a set of cards characterized by suits (+, -, =), values (A, B, C), and counts of these values ranging from 1 to 3. Your goal is to identify a valid hand from the given cards. A valid hand consists of 3 cards where:

All the suits are either the same or all different,
All the values are either the same or all different,
All the counts are either the same or all different.
Example 1:

Input cards:

{ +AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA }
Valid hands could be:

{ +AA, +AA, +AA }
Suit: Same [+ + +]
Value: Same [A A A]
Count: Same [2 2 2]

{ -A, -AA, -AAA }
Suit: Same [- - -]
Value: Same [A A A]
Count: Different [1 2 3]

{ -C, -B, -A }
Suit: Same [- - -]
Value: Different [C B A]
Count: Same [1 1 1]

{ +AA, -AA, =AA }
Suit: Different [+, -, =]
Value: Same [A A A]
Count: Same [2 2 2]
Example 2:

A valid hand can also be:

{ -A, +BB, =CCC }
Suit: Different [+, -, =]
Value: Different [A B C]
Count: Different [1 2 3]
Task:
Write a program to find and return the first valid hand from the provided list of cards. Input will be read from stdin.

For example, given the input:

+AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA
Output any valid hand from this set.
"""

def find_first_validhand(cards):
    from itertools import combinations

    def is_valid_hand(hand):
        suits = [card[0] for card in hand]
        values = [card[1:] for card in hand]
        counts = [len(card) - 1 for card in hand]

        suit_set = set(suits)
        value_set = set(values)
        count_set = set(counts)

        return (len(suit_set) == 1 or len(suit_set) == len(suits)) and (len(value_set) == 1 or len(value_set) == len(values)) and (len(count_set) == 1 or len(count_set) == len(counts))

    for hand in combinations(cards, 3):
        if is_valid_hand(hand):
            return hand

    return None

print(find_first_validhand([ "+AA", "-AA", "+AA", "-C", "-B", "+AA", "-AAA", "-A", "=AA" ]))