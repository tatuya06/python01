import random

def start():
    print('じゃんけんが開始されました')

def get_my_hand():
    print('自分の手を入力してください')
    my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
    return my_hand

def get_your_hand():
    you_hand = random.randint(0, 2)
    return you_hand

def Calc(my_hand, you_hand):
    if my_hand == 0:
        if you_hand == 0:
            print('あいこ')
        elif you_hand == 1:
            print('勝ち')
        elif you_hand == 2:
            print('負け')

    elif my_hand == 1:
        if you_hand == 0:
            print('負け')
        elif you_hand == 1:
            print('あいこ')
        elif you_hand == 2:
            print('勝ち')

    elif my_hand == 2:
        if you_hand == 0:
            print('勝ち')
        elif you_hand == 1:
            print('負け')
        elif you_hand == 2:
            print('あいこ')

start()
my_hand_result = get_my_hand()
your_hand_result = get_your_hand()
Calc(my_hand_result, your_hand_result)

