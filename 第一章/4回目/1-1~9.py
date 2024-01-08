import random

hands = ['グー','チョキ','パー']
hands_dec = {'グー':0,'チョキ':1,'パー':2}
results = {'win':'勝利','lose':'敗北','draw':'あいこ'}

def start_message():
    print('じゃんけんスタート')
    
def get_my_hand():
    print('自分の手を入力してください')
    input_message = ''
    index = 0
    for hand in hands:
        input_message += str(index) + ':' + hand
        if index < 2:
            input_message += ', '
            index += 1
    return  input(input_message)


def is_hand(string):
   if string.isdigit():
        number = int(string)
        if number == 0 or number == 1 or number == 2:
            return True
        else:
            return False
   else:
        return False

def get_your_hand():
    choice_your = random.randint(0,2)
    return choice_your

def get_hand_name(hand_number):
    hand_name = hands[hand_number]
    return hand_name

def viwe_hand(my_hand,your_hand):
    print('自分の手は'+hands[my_hand])
    print('相手の手は'+hands[your_hand])

def get_result(hand_diff):
  if hand_diff == 0:
    return 'draw'
  elif hand_diff == -1 or hand_diff == 2:
    return 'win'
  else:
    return 'lose'
   
def view_result(result):
   print(results[result])

def play():
    mh = get_my_hand()
    while not is_hand(mh):
       mh = get_my_hand()
    
    mh = int(mh)
    yh = get_your_hand()
    hand_diff = mh - yh

    viwe_hand(mh,yh)
    result = get_result(hand_diff)
    view_result(result)
    if result == 'draw':
       play()

start_message()      
play()