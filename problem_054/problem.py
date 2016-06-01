import sys

def load_hands():
    f = open('poker.txt', 'r')
    values = dict(zip('23456789TJQKA', range(2, 15)))
    cards_list = [line.split() for line in f.readlines()]
    hands = []
    for cards in cards_list:
        p1, p2 = cards[:5], cards[5:]
        hand1, hand2 = [[(values[val], suit) for val, suit in p] for p in [p1, p2]]
        hand1.sort(reverse=True)
        hand2.sort(reverse=True)
        hands.append((hand1, hand2))

    return hands

def combination(hand):
    combos = ['straight flush',
              'four of a kind',
              'full house',
              'flush',
              'straight',
              'three of a kind',
              'two pairs',
              'one pair',
              'high card']
    combo_code = dict(zip(combos, range(len(combos), 0, -1)))
    heights = [card[0] for card in hand]
    distincts_heights = set(heights)
    suits = [card[1] for card in hand]
    distinct_suits = set(suits)

    if len(distincts_heights) == 5 and heights[0] == heights[4] + 4:
        if len(distinct_suits) == 1:
            return (combo_code['straight flush'], heights[0])
        return (combo_code['straight'], heights[0])
    if len(distincts_heights) == 2:
        if heights[0] == heights[3]:
            return (combo_code['four of a kind'], (heights[0], heights[4]))
        if heights[1] == heights[4]:
            return (combo_code['four of a kind'], (heights[1], heights[0]))
        if heights[0] == heights[2]:
            return (combo_code['full house'], heights[0])
        return (combo_code['full house'], heights[2])
    if len(distinct_suits) == 1:
        return (combo_code['flush'], heights[0])
    if len(distincts_heights) == 3:
        three_of_a_kind_found = False
        if heights[0] == heights[2]:
            three_of_a_kind_found = True
            height = heights[0]
            kickers = (heights[3], heights[4])
        if heights[1] == heights[3]:
            three_of_a_kind_found = True
            height = heights[1]
            kickers = (heights[0], heights[4])
        if heights[2] == heights[4]:
            three_of_a_kind_found = True
            height = heights[2]
            kickers = (heights[0], heights[1])
        if three_of_a_kind_found:
            return (combo_code['three of a kind'], kickers)
        if heights[0] == heights[1]:
            if heights[2] == heights[3]:
                return (combo_code['two pairs'], (heights[0], heights[2], heights[3]))
            return (combo_code['two pairs'], (heights[0], heights[3], heights[2]))
        return (combo_code['two pairs'], (heights[1], heights[3], heights[0]))
    if len(distincts_heights) == 4:
        i = 0
        while heights[i] != heights[i + 1]:
            i += 1
        return (combo_code['one pair'], (heights[i], tuple(heights[:i] + heights[i + 2:])))
    return (combo_code['high card'], tuple(heights))
            

hands = load_hands()
for hand1, hand2 in hands:
    print('#######################')
    print(hand1, combination(hand1))
    print(hand2, combination(hand2))
    if combination(hand1) == combination(hand2):
        print(hand1, hand2, combination(hand1), file=sys.stderr)
    print('player 1' if combination(hand1) > combination(hand2) else 'player 2')
    print('#######################')

score = sum([1 if combination(hand1) > combination(hand2) else 0 for hand1, hand2 in hands])
print(score)
