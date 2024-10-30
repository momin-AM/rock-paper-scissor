import random
#import time  
def game(ui,ci):
    if ui==ci:
        print('  DRAW !!\n')
    elif (ui==1 and ci==3) or (ui==2 and ci==1) or (ui==3 and ci==2):
        print('```you WON congratulations,,,\n')
    else:
        print('you lost\n')
n=[1,2,3]
words=['rock','paper','scissors']
words1=['0','rock','paper','scissors']
while True:
    try:   
        ci=random.choice(n)
        ui=int(input('1.rock   2.paper    3.scisors(0 to stop): '))
        if ui==0:
            break
        elif ui==1 or ui==2 or ui==3:
            print(f'\nyou : {words1[ui]}')
            # time.sleep(1)
            print(f'\ncomputer : {words[n.index(ci)]}\n')
            # time.sleep(1)
            game(ui,ci)
        else:
            print('please enter valid choice')
    except:
        print('please enter only number')
