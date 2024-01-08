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
    reslat = my_hand - you_hand

    if reslat == 2 or reslat == -1:
        print('あなたの勝ちです')
    elif reslat == 0:
        print('あいこです')
    else:
        print('あなたの負けです')

start()
my_hand_result = get_my_hand()
your_hand_result = get_your_hand()
Calc(my_hand_result, your_hand_result)

