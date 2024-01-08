import random

def start():
    print('じゃんけんが開始されました')

def get_my_hand():
    print('自分の手を入力してください')
    my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
    if my_hand == 0:
        print('あなたはグーを選択されました')
    elif my_hand == 1:
        print('あなたはチョキを選択されました')
    else:
        print('あなたはパーを選択されました')
    return my_hand

def get_your_hand():
    you_hand = random.randint(0, 2)
    if you_hand == 0:
        print('相手はグーを選択されました')
    elif you_hand == 1:
        print('相手はチョキを選択されました')
    else:
        print('相手はパーを選択されました')
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
