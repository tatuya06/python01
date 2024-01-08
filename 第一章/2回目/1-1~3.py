import random

#じゃんけんを開始するメッセージを表示する関数
def start_message():
    print('それでは、じゃんけんを開始します')

#自身の手を決める関数
def myhand():
    print('あなたの手を入力してください')
    my_hand = int(input('0:グー、1:チョキ、2:パー'))
    return my_hand

#相手の手を決める関数
def youhand():
    you_hand = random.randint(0,2)
    return you_hand

#勝敗を決める関数
def result(mh,yh):
    hand_result = mh - yh
    if hand_result == 0:
        print('あいこです')
    elif hand_result == 2 or hand_result == -1:
        print('あなたの勝ちです')
    elif hand_result == 1 or hand_result == -2:
        print('あなたの負けです')

    
start_message()
mh = myhand()
yh = youhand()
result(mh,yh)

