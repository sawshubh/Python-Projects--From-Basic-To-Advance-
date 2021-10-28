import random
    
def logic():
    comp_score = 0
    user_score = 0
    print("What's your name")
    name = input()
    while(1):
        print('\n1.Rock\n2.Paper\n3.Scissor\n4.Final score\n')
    #USER INPUT
        inn = int(input())
        if inn == 1:
            print(name +':Rock')
        elif inn == 2:
            print(name +':Paper')
        elif inn == 3:
            print(name +':Scissor')
        elif inn == 4:
            Rico_says = ['Rico:Do penance for 25 days and then try to win against Rico',
                  'Rico:Take early morning cold shower to improve the brain power',
                  'Rico:Go play with some Noob!']
            if comp_score > user_score:
                print('Rico won the Game!')
                print(random.choice(Rico_says))                
                quit()
            elif comp_score < user_score:
                print(name +' won the Game!')
                quit()
            else:
                print('Game is Tied!')
                print('Rico:Finally a worthy opponent')
                quit()           
        else:
            print('INVALID INPUT ..MORON!')
        
        #COMPUTER INPUT
        l = [1,2,3]    
        comp_inn = random.choice(l)    
        if comp_inn == 1:
            print('Rico:Rock')
        elif comp_inn == 2:
            print('Rico:Paper')
        elif comp_inn == 3:
            print('Rico:Scissor')
        #LOGIC OF GAME    
        if inn == 1 and comp_inn == 2:
            comp_score += 1
            print("%s:%d, Rico:%d" %(name,user_score,comp_score))
        elif inn == 1 and comp_inn == 3:
            user_score += 1
            print("%s:%d, Rico:%d" %(name,user_score,comp_score))                
        elif inn == 2 and comp_inn == 1:
            user_score += 1
            print("%s:%d, Rico:%d" %(name,user_score,comp_score))    
        elif inn == 2 and comp_inn == 3:
            comp_score += 1
            print("%s:%d, Rico:%d" %(name,user_score,comp_score))
        elif inn == 3 and comp_inn == 1:
            comp_score += 1
            print("%s:%d, Rico:%d" %(name,user_score,comp_score))
        elif inn == 3 and comp_inn == 2:
            user_score += 1                        
            print("%s:%d, Rico:%d" %(name,user_score,comp_score))
        else:
            print('tie....') 
            
                
#DRIVER PROGRAM
print('***NAMASTE***')
print("LET'S START")
logic()
