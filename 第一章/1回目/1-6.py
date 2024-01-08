import random

hands = ['グー', 'チョキ', 'パー']
results = {'win':'勝ち','lose':'負け','drow':'あいこ'}

def start_message():
  print('じゃんけんスタート')

def get_my_hand():
  print('自分の手を入力してください')
  return int(input('0:' + hands[0] +',1:' + hands[1] + ',2' + hands[2]))

def get_you_hand():
  return random.randint(0, 2)

def get_hand_name(hand_number):
  return hands[hand_number]

def view_hand(my_hand, you_hand):
  print('自分の手は ' + get_hand_name(my_hand))
  print('相手の手は ' + get_hand_name(you_hand))

def result(hand_diff):
  if hand_diff == 0:
   return  results['drow']
  elif hand_diff == -1 or hand_diff == 2:
    return results['win']
  else:
    return results['lose']

#勝敗のメッセージを表示する関数
def get_result(hand_results):
    return print(hand_results)
  

start_message()

my_hand = get_my_hand()
you_hand = get_you_hand()
hand_diff = my_hand - you_hand
view_hand(my_hand, you_hand)
hand_results = result(hand_diff)
get_result(hand_results)
