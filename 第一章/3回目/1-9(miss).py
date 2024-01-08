import random
hands = ['グー','チョキ','パー']
results = {'win':'勝ち','lose':'負け','draw':'あいこ'}

def start_message():
    print('今からじゃんけんを始めます')


#指定の数字また文字列で繰り返し後に正値を入力するとエラー表示されてしまう
def my_hand():
    try:
        print('あなたの手を入力してください')
        myhand = int(input('0:'+hands[0]+',1:'+hands[1]+',2:'+hands[2]))
        if myhand == 0 or myhand == 1 or myhand == 2:
            return myhand
        else:
            my_hand()
    except ValueError:
        my_hand()


def you_hand():
    youhand = random.randint(0,2)
    return youhand

def viwe_hand(get_my_hand,get_you_hand):
    print('あなたの手は'+hands[get_my_hand]+'です')
    print('相手の手は'+hands[get_you_hand]+'です')    

def result(get_my_hand,get_you_hand):
    hand_result = get_my_hand - get_you_hand
    if hand_result == 0:
        return 'draw'
    elif hand_result == 2 or hand_result == -1:
        return 'win'
    else:
        return 'lose'

def view_result(get_result):
    print(results[get_result]+'です')

def chk_result(get_result):
    if get_result == 'draw':
        play()
    else:
        pass


def play():
    get_my_hand = my_hand()
    get_you_hand = you_hand()
    viwe_hand(get_my_hand,get_you_hand)
    get_result = result(get_my_hand,get_you_hand)
    view_result(get_result)
    chk_result(get_result)

start_message()
play()