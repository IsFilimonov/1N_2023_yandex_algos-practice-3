from collections import deque

step = 0
player_1 = deque(map(int, input().split()))
player_2 = deque(map(int, input().split()))

while len(player_1) > 0 and len(player_2) > 0:
    step += 1
    
    card_1 = player_1.popleft()
    card_2 = player_2.popleft()

    if card_1 == 0 and card_2 == 9:
        player_1.append(card_1)
        player_1.append(card_2)    
    elif card_2 == 0 and card_1 == 9:
        player_2.append(card_1)
        player_2.append(card_2)
    elif card_1 > card_2:
        player_1.append(card_1)
        player_1.append(card_2)
    elif card_2 > card_1:
        player_2.append(card_1)
        player_2.append(card_2)

print("{} {}".format(
    "first" if len(player_2) == 0 else "second",
    step
))
