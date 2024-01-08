import random

hands = ['グー','チョキ','パー']
results ={'win':'勝ち','lose':'負け','draw':'あいこ'}

#じゃんけんを開始するメッセージを表示する関数
def start_message():
    print('それでは、じゃんけんを開始します')

#自身の手を決める関数
def myhand():
    while True:
        print('あなたの手を入力してください')
        try:
            my_hand = int(input('0:'+ hands[0]+'、1:'+ hands[1] +'、2:'+hands[2]))
            if my_hand == 0 or my_hand == 1 or my_hand == 2:
                return my_hand
            else:
                myhand()
        except ValueError:
            myhand()

#相手の手を決める関数
def youhand():
    you_hand = random.randint(0,2)
    return you_hand

#お互いの手を表示する関数
def view_hand(mh,yh):
    print('あなたの手は' + hands[mh] + 'です')
    print('相手の手は' + hands[yh] + 'です')

#勝敗を決める関数
def result(mh,yh):
    hand_result = mh - yh
    if hand_result == 0:
        return 'draw' 
    elif hand_result == 2 or hand_result == -1:
        return 'win'
    elif hand_result == 1 or hand_result == -2:
        return 'lose'

#勝敗を表示する関数
def view_result(rs):
    print(results[rs]+ 'です')

#あいこだった時に再度play()が実行される
def get_result(rs):
    if rs == 'draw':
        play()
    else:
        pass


#じゃんけんをまとめた関数
def play():
    mh = myhand()
    yh = youhand()
    view_hand(mh,yh)
    rs = result(mh,yh)
    view_result(rs) 
    get_result(rs)

    
start_message()
play()