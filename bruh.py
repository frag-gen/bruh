import random

def get_letter():
    alphabet = chr(random.randint(97,122))
    return alphabet

ques= input ( "enter the word")
len1= len(ques)
    
ques_ask=list(ques)
ask= list(ques)

for i in range(len1):
    ques_ask[i]= '_'

count =1 
start= True
while(start):
    for i in range(len1):
        
        ques_ask[i]=get_letter()
    print(' '.join(ques_ask))
    if(ques_ask==ask):
        print("total tries: ", count)
        start = False
    else:
        for i in range(len1):
            ques_ask[i]="_"
        count+=1
