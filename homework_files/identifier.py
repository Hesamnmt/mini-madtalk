def identifier_tester(state,input):
    
    if state==0:
        for x in 'abcdefghijklmnopqrstwxyz':
            if (input==x):  
                return 1
    if state==1 :
        for x in 'abcdefghijklmnopqrstwxyz1234567890_':
            if (input==x):
                return 1

def int_tester(state,input):
    
    if state==0 and input == '-':
        return 1
    elif state==0 :
        for x in '123456789':
            if x == input:
                print('inja')
                return 2 
    elif state == 0 and input == '0':
        return 3
    
    elif state==1 :
        for x in '123456789':
            if (input==x):
                return 2    
    elif state==2 :
        for x in '0123456789':
            if x == input :
                print('inja2')
                return 2
    
list_input = list( 'ab = ( amir3ami + abc ) ') 
tokens = list()

def main():
    statesID=0
    statesINT=0
    word = ''
    for x in list_input:
        
        if x==' ':
            if word == 'if':
                tokens.append('/if')
            elif word == 'while':
                tokens.append('/while')
            elif statesID==1 and word != 'if' and word != 'while':
                tokens.append('/id')
            elif (statesINT==2 or statesINT == 3) :
                tokens.append('/num')
            elif word == '(':
                tokens.append('/(')
            elif word == ')':
                tokens.append('/)')
            elif word == '+':
                tokens.append('+')
            elif word == '=':
                tokens.append('/=')
            else :
                tokens.append('/error')
            statesID =0
            statesINT =0
            word = ''
            continue
        statesID = identifier_tester(statesID,x)
        statesINT = int_tester(statesINT,x)
        word = word + x
    print(word)
    
main()

print(tokens)




